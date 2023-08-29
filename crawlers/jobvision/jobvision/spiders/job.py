import json
import scrapy

from jobvision.items import JobvisionItem
from jobvision.statistics import JobVisionStats
# from jobvision.utilities.db_work import get_province
from jobvision.utilities.uses import is_extracted_item_valid

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['jobvision.ir']
    start_urls = ['https://jobvision.ir']
    headers = {'User-Agent': 'ganje bot (+https://ganje.ir)'}
    stats = JobVisionStats()

    def parse(self, response):
        for page_index in range(1,3):
            form_data = {
                "pageSize" : 30,
                "requestedPage" : page_index,
                "sortBy" : 1,
            }
            yield scrapy.Request(
                url='https://apiemployee.jobvision.ir/api/v1/JobPost/List',
                callback=self.parse_job,
                method='POST' , 
                headers={'Content-Type': 'application/json', 'User-Agent': 'ganje bot (+https://ganje.ir)'},
                body=json.dumps(form_data))
    
    def parse_job(self,response):
        jsons = json.loads(response.body)
        jobs = jsons['data']['jobPosts']

        for job in jobs :
            token = job['id']
            url_detail = f'https://apiemployee.jobvision.ir/api/v1/JobPost/Detail?jobPostId={token}'
            yield scrapy.Request(
                url=url_detail,
                callback=self.parse_job_detail,
                method='GET',
                headers=self.headers                
            )
    
    def parse_job_detail(self,response):
        job_json = json.loads(response.body)
        job = job_json['data']

        item = JobvisionItem()
        item.extract(job,self.stats)
        self.stats.item_added()

        # if item['province'] == 'not_defined' or len(str(item['province'])) == 0 : item['province'] = get_province(item['city'])['p']
        if is_extracted_item_valid(item['token'],item['city'],item['province']) : yield item

    # def parse_job_detail(self,response): 
    #     jsons = json.loads(response.body)
    #     jobs = jsons['data']['jobPosts']

    #     for job in jobs :
    #         item = JobvisionItem()
    #         item.extract(job,self.stats)
    #         self.stats.item_added()
    #         if item['province'] == 'not_defined' or len(str(item['province'])) == 0 : item['province'] = get_province(item['city'])['p']
    #         if is_extracted_item_valid(item['token'],item['city'],item['province'],item['description']) : yield item