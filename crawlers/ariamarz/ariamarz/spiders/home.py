import scrapy
from bs4 import BeautifulSoup

from ariamarz.items import AriamarzItem
from ariamarz.statistics import AriamarzStats

class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['www.ariamarz.com']
    start_urls = ['https://www.ariamarz.com/cities-sitemap.xml']
    stats = AriamarzStats()
    cities = []

    def parse(self, response):
        xml_text = response.text

        soup = BeautifulSoup(xml_text)
        locs = soup.find_all("loc")

        for city in locs:
            self.cities.append(city.text.split('/')[-1].replace(".xml",""))

        self.cities.append("tabriz")
        self.cities.append("tehran")
        self.cities.append("isfahan")
        self.cities.append("shiraz")
        self.cities.append("karaj")
        self.cities.append("mashhad")
        
        for city in self.cities:
            url = f'https://www.ariamarz.com/buy-apartment/{city}'
            yield scrapy.Request(url = url,callback= self.parse_page , meta = {
                "buy" : True
            })

        for city in self.cities:
            url = f'https://www.ariamarz.com/rent-apartment/{city}'
            yield scrapy.Request(url = url,callback= self.parse_page , meta = {
                "buy" : False
            })

    def parse_page(self,response):
        url = f'{response.request.url}?in=&page=1'
        yield scrapy.Request(url = url , callback=self.parse_homes , meta = {
            "buy" : response.request.meta["buy"]
        })

    def parse_homes(self,response):
        homes = response.xpath('//div[@class="product-plate"]')
        city = response.xpath('//span[@class="ds-breadcrumbs"]/text()').get()
        is_buy = response.request.meta['buy']
        for home in homes :
            item = AriamarzItem()
            item['city'] = city
            item['url'] = response.request.url
            item.extract(home,is_buy,stats=self.stats)
            self.stats.item_added()
            yield item