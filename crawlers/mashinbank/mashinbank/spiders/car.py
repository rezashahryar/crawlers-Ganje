import scrapy

from mashinbank.items import MashinbankItem
from mashinbank.statistics import MashinBankStats

class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['mashinbank.com']
    start_urls = ['https://mashinbank.com']
    stats = MashinBankStats()

    def parse(self, response):
        for page_index in range(1,6):
            url = f"https://mashinbank.com/خرید-خودرو?page={page_index}"
            yield scrapy.Request(url=url , callback=self.parse_cars)

    def parse_cars(self,response):
        cars = response.xpath('//div[@class="cars-item"]/div/a')

        for car in cars :
            thumbnail = car.xpath('.//div[@class="cars-img"]/img/@src').get()
            year = car.xpath('.//div[@class="cars-title cars-year"]/text()').get().replace('-','').strip()
            href = car.xpath('.//@href').get()
            url = f"https://mashinbank.com{href}"
            yield scrapy.Request(url=url , callback=self.parse_car, meta={"thumbnail" : thumbnail , "year" : year})

    def parse_car(self,response):
        item  = MashinbankItem()
        item['production'] = response.request.meta['year']
        item['thumbnail'] = response.request.meta['thumbnail']
        item.extract(response,self.stats)
        self.stats.item_added()
        yield item