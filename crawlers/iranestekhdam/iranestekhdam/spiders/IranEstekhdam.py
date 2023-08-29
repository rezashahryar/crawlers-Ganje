import scrapy

from iranestekhdam.items import IranestekhdamItem
from iranestekhdam.statistics import IranEstkhdamStats
from iranestekhdam.utilities import (uses , db_work)

class IranestekhdamSpider(scrapy.Spider):
    name = 'IranEstekhdam'
    allowed_domains = ['iranestekhdam.ir']
    start_urls = ['https://iranestekhdam.ir/search/']
    stats = IranEstkhdamStats()
    headers = {'User-Agent': 'ganje bot (+https://ganje.ir)'}

    def parse(self, response):
        for page_index in range(1,2):
            url = f"https://iranestekhdam.ir/search?page={page_index}"
            yield scrapy.Request(url = url , callback = self.parse_jobs, headers=self.headers)

    # Get All Jobs Url and Send Request To It
    def parse_jobs(self,response):
        job_urls = response.xpath('//div[@class="col-xl-4"]/a')

        for url in job_urls:
            city = url.xpath('.//descendant::span[@class="state"]/text()').get()
            link = url.xpath('.//@href').get()
            yield scrapy.Request(url = link , callback=self.parse_job , meta = {"city" : city}, headers=self.headers)

    # Get The Job Page And Extract The Datas
    def parse_job(self,response):
        url = response.request.url
        token = url.split('/')[3]
        item = IranestekhdamItem()
        item.extract(response,self.stats,token)
        item['city'] = response.request.meta['city'].strip()
        # if item['city'].__contains__("استان") : item['city'] = 'not_defined'

        self.stats.item_added()
        c_p_details = uses.extract_province_city_iranestekhdam(item['city'])
        if not isinstance(c_p_details, str):
            item['city'] = c_p_details['c']
            item['province'] = c_p_details['p']
        else:
            item['city'] = 'not_defined'
            item['province'] = 'not_defined'
        if uses.is_extracted_item_valid(item['token'],item['city'],item['province']) : yield item