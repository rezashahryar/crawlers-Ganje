import scrapy
import json
from quera.items import QueraItem
from quera.statistics import QueraStats
class QueraSpider(scrapy.Spider):
    name = 'Quera'
    allowed_domains = ['quera.org']
    start_urls = ['https://quera.org']
    stats = QueraStats()
    def parse(self, response):
        """
        in this method placed 3 lines of code
        for showing how to extract data with scrapy item
        you can move or modify these codes.
        """
        try:
            jobs = response.xpath("//script[contains(., 'pageProps')]/text()").extract_first()
            jobs = json.loads(jobs)
            jobs = jobs['props']['pageProps']['jobs']['edges']
            for job in jobs:
                url = f"https://quera.org/magnet/jobs/{job['node']['pk']}"
                yield scrapy.Request(url=url,callback=self.parse_job)
        except : None

        for page_index in range(1,6):
            page = f"https://quera.org/magnet/jobs?page={page_index}"
            yield scrapy.Request(url=page,callback=self.parse)
        
    def parse_job(self, response):
        job = response.xpath("//script[contains(., 'pageProps')]/text()").extract_first()
        job = json.loads(job)
        item = QueraItem()
        item.extract(job['props']['pageProps']['job'],self.stats)
        self.stats.item_added()
        yield item
        
    def parse_city(self,response):
        item = response.request.meta['item']
        item['city'] = response.xpath("//div[@class='chakra-stack css-jwkjby']//p[1]/text()[1]").get()
        yield item