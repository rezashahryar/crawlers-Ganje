import scrapy

from jobinja.items import JobinjaItem
from jobinja.statistics import JobinjaStats
from jobinja.utilities import uses

class JobSpider(scrapy.Spider):
    name = 'Job'
    allowed_domains = ['jobinja.ir']
    start_urls = ['https://jobinja.ir/jobs/']
    stats = JobinjaStats()

    def parse(self, response):
        try:
            jobs = response.xpath('//div[@class="o-listView__itemInfo"]')
            for job in jobs:
                job_url = job.xpath('.//descendant::a[@class="c-jobListView__titleLink"]/@href').get()
                yield  scrapy.Request(url=job_url, callback=self.parse_job)
        except : None

        for page_index in range(1,6):
            url = f"https://jobinja.ir/jobs?&page={page_index}"
            yield scrapy.Request(url = url, callback=self.parse)

    def parse_job(self,response):
        item = JobinjaItem()
        item.extract(response,self.stats)
        self.stats.item_added()
        if uses.is_extracted_item_valid(item['token'],item['city'],item['province']) : yield item