import scrapy
import json

from irantalent.items import IrantalentItem
from irantalent.statistics import IranTalentStats

from irantalent.utilities import uses , db_work

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['irantalent.com']
    start_urls = ['https://www.irantalent.com']
    stats = IranTalentStats()

    def parse(self, response):
        for page_index in range(1,6):
            yield scrapy.Request(
                url=f'https://api.irantalent.com/api/v1/employer/position/search-by-slug?page={page_index}',
                callback=self.parse_job,
                method='POST' , 
                headers={'Content-Type': 'application/json'})
    
    def parse_job(self,response): 
        jsons = json.loads(response.body)
        jobs = jsons['data']

        for job in jobs :
            item = IrantalentItem()
            item.extract(job,self.stats)
            self.stats.item_added()
            item['province'] = db_work.get_province(item['city'])['p']
            if uses.is_extracted_item_valid(item['token'],item['city'],item['province']) : yield item