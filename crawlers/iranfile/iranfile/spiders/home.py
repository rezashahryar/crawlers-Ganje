import scrapy

from iranfile.items import IranfileItem
from iranfile.statistics import IranFileStats

class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['iranfile.ir']
    start_urls = ['https://iranfile.ir']
    stats = IranFileStats()

    def parse(self, response):
        sale_url = "https://iranfile.ir/Search/A4BDC39B-1/%D8%AE%D8%B1%DB%8C%D8%AF_%D8%AA%D9%87%D8%B1%D8%A7%D9%86"
        rent_url = "https://iranfile.ir/Search/81868128-1/%D8%B1%D9%87%D9%86_%D8%A7%D8%AC%D8%A7%D8%B1%D9%87_%D8%AA%D9%87%D8%B1%D8%A7%D9%86"

        yield scrapy.Request(url = sale_url , callback = self.parse_homes , meta = {"is_rent" : False})
        yield scrapy.Request(url = rent_url , callback = self.parse_homes , meta = {"is_rent" : True})

    def parse_homes(self, response):
        homes = response.xpath('//tbody/tr')
        is_rent = response.request.meta['is_rent']
        for home in homes:
            home_url = home.xpath('.//td[2]/a/@href').get()
            home_token = home.xpath('.//@pcode').get()
            rent = 0
            deposit = 0 
            price = 0
            if is_rent :
                rent = home.xpath('.//td[@data-title="مبلغ اجاره"]/a/div/text()').get().strip()
                deposit = home.xpath('.//td[@data-title="مبلغ ودیعه"]/a/div/text()').get().strip()
            else :
                price = home.xpath('.//td[@data-title="قیمت کل"]/a/div/text()').get().strip()
            home_type = home.xpath('.//td[@data-title="نوع ملک"]/a/div/text()').get().strip()
            home_address = home.xpath('.//td[@data-title="آدرس"]/a/div/text()').get().strip()
            title = f"{home_type} {home_address}"
            yield scrapy.Request(url = home_url , callback = self.parse_home, 
            meta =
            {
                "token" : home_token , 
                "title" : title ,
                "rent" : rent,
                "deposit" : deposit,
                "price" : price,
                "is_rent" : is_rent
                })

    def parse_home(self, response):
        item = IranfileItem()
        item.extract(response,self.stats)
        self.stats.item_added()
        yield item