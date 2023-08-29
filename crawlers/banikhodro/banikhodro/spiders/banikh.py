import scrapy

from banikhodro.items import BanikhodroItem
from banikhodro.statistics import BaniKhodroStats

class BanikhSpider(scrapy.Spider):
    name = 'banikh'
    allowed_domains = ['www.banikhodro.com']
    start_urls = ['https://www.banikhodro.com']
    stats = BaniKhodroStats()

    def parse(self,response):
        for page_index in range(1,11):
            url = url = f"https://www.banikhodro.com/car/#page{page_index}"
            yield scrapy.Request(url=url, callback=self.parse_cars,dont_filter=True)


    def parse_cars(self, response):
        # try :
        cars_url = response.xpath('//span[@class="photo"]/a')

        for car_url in cars_url :
            thumb = car_url.xpath('.//img/@src').get()
            car_url = car_url.xpath('.//@href').get()
            url = f"https://www.banikhodro.com{car_url}"
            yield scrapy.Request(url=url, callback=self.parse_car,meta = {'thumb' : thumb})
        # except : pass
    

    def parse_car(self,response):
        item = BanikhodroItem()
        item.extract(response=response,stats=self.stats)
        self.stats.item_added()
        
        yield item