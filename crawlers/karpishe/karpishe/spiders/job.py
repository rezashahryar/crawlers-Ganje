import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['karpishe.com']
    start_urls = ['https://karpishe.com']

    def parse(self, response):
        pass
