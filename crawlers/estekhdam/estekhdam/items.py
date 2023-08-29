# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from estekhdam.utilities.uses import hash_token , get_time_stamp

class BaseItem(scrapy.Item):
    token = scrapy.Field()
    source_id = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    neighbourhood = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    thumbnail = scrapy.Field()
    search_pgvector = scrapy.Field()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['token'] = -1
        self['source_id'] = -1
        self['time'] = -1
        self['title'] = 'not_defined'
        self['category'] = 'not_defined'
        self['sub_category'] = 'not_defined'
        self['province'] = 'not_defined'
        self['city'] = 'not_defined'
        self['neighbourhood'] = 'not_defined'
        self['description'] = 'not_defined'
        self['url'] = 'not_defined'
        self['thumbnail'] = 'not_defined'
        self['search_pgvector'] = 'not_defined'


class RecruitmentBaseItem(scrapy.Item):
    education = scrapy.Field()
    insurnace = scrapy.Field()
    cooperation = scrapy.Field()
    salary = scrapy.Field()
    gender = scrapy.Field()
    experience = scrapy.Field()
    teleworking = scrapy.Field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['education'] = 'not_defined'
        self['insurnace'] = 'not_defined'
        self['cooperation'] = 'not_defined'
        self['salary'] = -1
        self['gender'] = 'not_defined'
        self['experience'] = -1
        self['teleworking'] = 'not_defined'

class EstekhdamItem(BaseItem , RecruitmentBaseItem):
    def extract(self,response,stats):
        meta = response.request.meta
        self['source_id'] = 20
        self['url'] = response.request.url
        self['token'] = hash_token(meta['token'],20)
        self['title'] = meta['title']
        self['city'] = meta['city'].strip()
        self['time'] = get_time_stamp()

        if meta['city'].__contains__(')') :
            self['province'] = meta['city'].split('(')[0].strip()
            self['city'] = meta['city'].split('(')[1].replace(')','').strip()

        if meta['cooperation'] :
            if meta['cooperation'].__contains__('دورکاری'): self['teleworking'] = True

            if meta['cooperation'].__contains__(' و '):
                self['cooperation'] = meta['cooperation'].split(' و ')[0]
            else : self['cooperation'] = meta['cooperation']

        # Details
        detail = response.xpath('//div[@class="job-custom-fields"]')

        salary = detail.xpath('.//descendant::span[@class="value-_noo_job_field_salary cf-select-value"]/text()').get()
        if salary :
            if salary != 'توافقی':
                self['salary'] = salary.split(' ')[0].replace('.','').strip()
                # .replace(' ت ~ به بالا', '').replace('.','').strip()

        education = detail.xpath('.//descendant::span[@class="value-_noo_job_field_experience_level cf-select-value"]/text()').get()
        if education :
            if not education.__contains__('مهم نیست'):
                self['education'] = education
        
        experience = detail.xpath('.//descendant::span[@class="value-_noo_job_field_experience cf-multiple_select-value"]/text()').get()
        if experience :
            for year in experience:
                if year.isdigit() : 
                    self['experience'] = year
                    break

        # Gender , Insurance
        desc = response.xpath('//div[@class="job-desc  "]/hr/following-sibling::node()/text()').extract()

        if response.xpath('//td[contains(text(),"آقا")]') or response.xpath('//td[contains(text(),"مرد")]') : self['gender'] = 'مرد'
        if response.xpath('//td[contains(text(),"خانم")]') or response.xpath('//td[contains(text(),"زن")]') : self['gender'] = 'زن'
        
        if desc :
            for text in desc:
                if text.__contains__('بیمه') : self['insurnace'] = True
            self['description'] = ' , '.join(desc)
            

        # Calculate Statistics Of Broken Fields
        if self['city'] == 'not_defined' or self['city'] == '': stats.specify_the_broken_one('city')
        
        if self['education'] == 'not_defined' or self['education'] == '': stats.specify_the_broken_one('education')
            
        if self['insurnace'] == 'not_defined' or self['insurnace'] == '': stats.specify_the_broken_one('insurnace')
            
        if self['cooperation'] == 'not_defined' or self['cooperation'] == '':stats.specify_the_broken_one('cooperation')
            
        if self['salary'] == -1: stats.specify_the_broken_one('salary')
            
        if self['gender'] == 'not_defined' or self['gender'] == '': stats.specify_the_broken_one('gender')
            
        if self['experience'] == -1: stats.specify_the_broken_one('experience')
            
        if self['teleworking'] == 'not_defined' or self['teleworking'] == '': stats.specify_the_broken_one('teleworking')     

        stats.calculate_the_broken_stats()