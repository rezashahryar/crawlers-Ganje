import scrapy
import logging

from eestkhdam.items import EestkhdamItem
from eestkhdam.statistics import EestkhdamStats

class EestekhdamSpider(scrapy.Spider):
    name = 'eestekhdam'
    allowed_domains = ['www.e-estekhdam.com']
    start_urls = ['https://www.e-estekhdam.com']
    stats = EestkhdamStats()
    headers = {'User-Agent': 'ganje bot (+https://ganje.ir)'}
    
    # def parse(self, response):
    #     categories = response.xpath('//div[re:test(@class,"col-md-3 no-padding.*")]/a')

    #     for category in categories:
    #         cat_name = category.xpath('.//text()').get()
    #         href = category.xpath('.//@href').get()

    #         yield response.follow(url=href , callback = self.parse_page , meta = { "cat_name" : cat_name })
    
    def parse(self,response):
        for page_index in range(1,6):
            url = f"https://www.e-estekhdam.com/search?page={page_index}"
            yield scrapy.Request(url = url , callback = self.parse_jobs, headers=self.headers)

    def parse_jobs(self,response):
        jobs = response.xpath('//a[@class="title vertical-top display-inline "]')
        # the_cat_name = response.request.meta['cat_name']
        # the_cat_url = response.request.url

        for job in jobs :
            job_name = job.xpath('.//text()').get()
            href = job.xpath('.//@href').get()
            province = job.xpath('.//following-sibling::div//div[@class="provinces"]/span/text()').get()

            url = f"https://www.e-estekhdam.com/{href}"
            yield scrapy.Request(url= url, callback = self.parse_job, headers=self.headers,
            meta = {
                    "job_name" : job_name , 
                    # "cat_name" : the_cat_name ,
                    "province" : province ,
                    "job_href" : href
                    })

    def parse_job(self,response):
        item = EestkhdamItem()
    
        has_table = response.xpath('//table[@class="table table-bordered table-striped"]')
        
        cat_name = response.xpath('//h2[@class="position-name mt-15 no-margin-bottom text-primary font-weight-bold"]/text()').get()
        province = response.request.meta['province']
        job_href = response.request.meta['job_href'].split('-')[0].replace('/','')
        
        if has_table :           
            jobs = has_table.xpath('.//tbody/tr')
            title = response.xpath('//h1[@class="entry-title"]/a/text()').get()
            
            if title : item["title"] = title
            item['category'] = cat_name
            item['province'] = province
            item['url'] = response.request.url
                        
            item.extract(is_table=True,response=response,stats = self.stats,href=job_href)
            
            self.stats.item_added()
            # Calculate Statistics Of Broken Fields
            self.calc_statistics(item)
            self.stats.calculate_the_broken_stats()

            yield item

        else :
            item.extract(is_table=False,response=response,stats = self.stats,href=job_href)
            title = response.request.meta['job_name']
            item['title'] = title
            item['category'] = cat_name
            
            self.stats.item_added()
            # Calculate Statistics Of Broken Fields
            self.calc_statistics(item)
            self.stats.calculate_the_broken_stats()   
            
            yield item
        
    def calc_statistics(self,item):
        if item['education'] == 'not_defined' or item['education'] == '': self.stats.specify_the_broken_one('education')
                
        if item['insurnace'] == 'not_defined' or item['insurnace'] == '': self.stats.specify_the_broken_one('insurnace')
            
        if item['cooperation'] == 'not_defined' or item['cooperation'] == '':self.stats.specify_the_broken_one('cooperation')
            
        if item['salary'] == -1: self.stats.specify_the_broken_one('salary')

        if item['token'] == -1: self.stats.specify_the_broken_one('token')
            
        if item['gender'] == 'not_defined' or item['gender'] == '': self.stats.specify_the_broken_one('gender')
            
        if item['experience'] == -1: self.stats.specify_the_broken_one('experience')
            
        if item['teleworking'] == 'not_defined' or item['teleworking'] == '': self.stats.specify_the_broken_one('teleworking')

        if item['province'] == 'not_defined' or item['province'] == '': self.stats.specify_the_broken_one('province')   