import scrapy

from karboom.items import KarboomItem
from karboom.statistics import KarboomStats
from karboom.utilities.db_work import get_province
from karboom.utilities.uses import is_extracted_item_valid

class JobSpider(scrapy.Spider):
    name = 'Job'
    allowed_domains = ['karboom.io']
    start_urls = ['https://karboom.io/jobs?q']
    stats = KarboomStats()
    headers = {'User-Agent': 'ganje bot (+https://ganje.ir)'}
    def parse(self, response):
        try:
            jobs = response.xpath('//div[@class="content-column flex-col-between flex-1 overflow-hidden width-75"]')
             # job_urls = response.xpath('//h3[@class="sm-title-size ellipsis-text width-100 m-0"]/a')

            for job in jobs:
                city = job.xpath(".//div/span[@class='pull-right']/text()").get()
                url = job.xpath('.//h3[@class="sm-title-size ellipsis-text width-100 m-0"]/a/@href').get()
                yield scrapy.Request(url = url, callback=self.parse_job,meta={"city" : city}, headers=self.headers)
        except : None

        for page_index in range(1,6):
            url = f'https://karboom.io/jobs?page={page_index}'
            yield scrapy.Request(url = url,callback=self.parse, headers=self.headers)

    # def parse_page(self, response):
    #     jobs = response.xpath('//div[@class="content-column flex-col-between flex-1 overflow-hidden width-75"]')
    #     # job_urls = response.xpath('//h3[@class="sm-title-size ellipsis-text width-100 m-0"]/a')

    #     for job in jobs:
    #         city = job.xpath(".//div/span[@class='pull-right']/text()").get()
    #         url = job.xpath('.//h3[@class="sm-title-size ellipsis-text width-100 m-0"]/a/@href').get()
    #         yield scrapy.Request(url = url, callback=self.parse_job,meta={"city" : city})

    def parse_job(self, response):
        item = KarboomItem()
        item['city'] = response.request.meta["city"]
        item.extract(response,self.stats)
        self.stats.item_added()
        if not (item['description'] == 'not_defined' or len(str(item['description'])) == 0) :
            item['province'] = get_province(item['city'])['p']
            if is_extracted_item_valid(item['token'],item['city'],item['province']) : yield item