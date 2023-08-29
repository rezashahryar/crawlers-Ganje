import scrapy
import logging

from estekhdam.items import EstekhdamItem
from estekhdam.statistics import EstekhdamStats

from estekhdam.utilities import uses , db_work

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['estekhdam.in']
    start_urls = ['https://estekhdam.in/jobs/']
    stats = EstekhdamStats()

    def parse(self, response):
        for page_index in range(1,6):
            url = f"https://estekhdam.in/jobs/page/{page_index}/"
            yield scrapy.Request(url = url , callback = self.parse_jobs)

    def parse_jobs(self, response):
        jobs = response.xpath('//article')
        for job in jobs:
            job_token = job.xpath('.//@class').get().split(' ')[3].split('-')[1]
            job_url = job.xpath('.//a/@href').get()
            job_title = job.xpath('.//div/div/h2/a/text()').get()
            job_cooperation = job.xpath('.//div/div/p/span[@class="job-type"]/a/span/text()').get()
            job_city = job.xpath('.//div/div/p/span[@class="job-location"]/a/em/text()').get().replace('استخدام','')
            yield scrapy.Request(url = job_url , callback = self.parse_job , meta =
            {   
                "token" : job_token,
                "title" : job_title,
                "cooperation" : job_cooperation,
                "city" : job_city
            })
        # logging.warning("Warning Logging")
        # self.logger.
    def parse_job(self, response):
        item = EstekhdamItem()
        item.extract(response,self.stats)
        self.stats.item_added()

        if item['province'] == 'not_defined' or len(str(item['province'])) == 0 : item['province'] = db_work.get_province(item['city'])['p']
        if uses.is_extracted_item_valid(item['token'],item['city'],item['province']) : yield item