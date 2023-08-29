import scrapy

from twonabsh.items import TwonabshItem
from twonabsh.statistics import TwoNabshStats

class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['www.2nabsh.com']
    start_urls = ['https://www.2nabsh.com/%D9%86%D9%82%D8%B4%D9%87-%D8%B3%D8%A7%DB%8C%D8%AA']
    stats = TwoNabshStats()

    def parse(self, response):
        cities = response.xpath('//div[@class="col-6 col-md-4 col-lg-2"]')

        for city in cities :
            href = city.xpath('.//a/@href').get()
            name = city.xpath('.//a/span/text()').get()
            url = f'https://www.2nabsh.com{href}'
            yield scrapy.Request(url=url, callback=self.parse_citymap,meta={'cityName' : name})

    def parse_citymap(self,response):
        sale = response.xpath('(//div[@class="col-12 col-md-6 col-lg-4"])[1]')
        rent = response.xpath('(//div[@class="col-12 col-md-6 col-lg-4"])[2]')

        # sale
        sale_href = sale.xpath('.//a/@href').get()
        sale_url = f'https://www.2nabsh.com{sale_href}'
        yield scrapy.Request(url = sale_url, callback = self.parse_sale , meta = {'cityName' : response.request.meta['cityName']})

        # rent
        rent_href = rent.xpath('.//a/@href').get()
        rent_url = f'https://www.2nabsh.com{rent_href}'

        yield scrapy.Request(url = rent_url, callback = self.parse_rent , meta = {'cityName' : response.request.meta['cityName']})
    
    def parse_sale(self,response):
        city = response.request.meta['cityName']

        if response.request.url.__contains__('ویلا') : return
    
        if city.__contains__('تهران') or city.__contains__('مشهد'):
            homes = response.xpath('//div[@class="sc-1fubugv-0 ebxVIP"]')
            for home in homes :
                home_href = home.xpath('.//figure/a/@href').get()
                home_img = home.xpath('.//descendant::img/@src').get()
                home_url = f'https://www.2nabsh.com{home_href}'
                yield scrapy.Request(url=home_url, callback=self.parse_item , meta = {'cityName' : city , "image" : home_img})    

        homes = response.xpath('//figure[@class="slojh5-1 iBcuQP"]')
        for home in homes :
            home_href = home.xpath('.//div/a[1]/@href').get()
            home_img = home.xpath('.//descendant::span[@class=" lazy-load-image-background blur lazy-load-image-loaded"]/img/@src').get()
            home_url = f'https://www.2nabsh.com{home_href}'
            yield scrapy.Request(url=home_url, callback=self.parse_item , meta = {'cityName' : city , "image" : home_img})

    def parse_rent(self,response):
        city = response.request.meta['cityName']
        two_layer = response.xpath('//div[@class="col-md-6 mt-md-16"]')

        if two_layer :
            for home in two_layer:
                home_href = home.xpath('.//a/@href').get()
                home_img = home.xpath('.//descendant::img/@src').get()
                home_url = f'https://www.2nabsh.com{home_href}'
                yield scrapy.Request(url=home_url, callback=self.parse_item , meta = {'cityName' : city , "image" : home_img})

        else :
            homes = response.xpath('//figure[@class="slojh5-1 iBcuQP"]')
            for home in homes :
                home_href = home.xpath('.//div/a[1]/@href').get()
                home_img = home.xpath('.//descendant::span[@class=" lazy-load-image-background blur lazy-load-image-loaded"]/img/@src').get()
                home_url = f'https://www.2nabsh.com{home_href}'
                yield scrapy.Request(url=home_url, callback=self.parse_item , meta = {'cityName' : city , "image" : home_img})

    def parse_item(self,response):
        is_not_valid = response.xpath('//p[@class="mr-16 text-dark font-weight-bold"][contains(text(),"مدت زیادی از آگهی این ملک گذشته و از سایت حذف شده")]')
        if not is_not_valid :
            item = TwonabshItem()
            
            item.extract(response,self.stats)
            self.stats.item_added()
            yield item