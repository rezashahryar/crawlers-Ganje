import scrapy

from shabesh.items import ShabeshItem
from shabesh.statistics import ShabeshStats

class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['shabesh.com']
    start_urls = ['https://shabesh.com']
    stats = ShabeshStats()

    def parse(self, response):
        for page_index in range(1,6):
            sale_url = f"https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page={page_index}"
            rent_url = f"https://shabesh.com/search/%D8%B1%D9%87%D9%86-%D8%A7%D8%AC%D8%A7%D8%B1%D9%87/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page={page_index}"

            yield scrapy.Request(url=sale_url, callback=self.parse_homes)
            yield scrapy.Request(url=rent_url, callback=self.parse_homes)

    def parse_homes(self, response):
        homes = response.xpath('//div[@class="list_announceListMode__69v30 mt-2  col-12"]/a')

        for home in homes :
            home_href = home.xpath('.//@href').get()
            home_url = f'https://shabesh.com{home_href}'
            yield scrapy.Request(url = home_url, callback=self.parse_home)

    def parse_home(self, response):
        item = ShabeshItem()
        item.extract(response,self.stats)
        self.stats.item_added()
        yield item