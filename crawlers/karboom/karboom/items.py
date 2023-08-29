# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from karboom.utilities.uses import hash_token, get_time_stamp


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


class KarboomItem(BaseItem,RecruitmentBaseItem):
    def extract(self,response,stats):
        url = response.request.url
        
        self['source_id'] = 17
        self['time'] = get_time_stamp()
        token = url.split('/')[4]
        if token : self['token'] = hash_token(token,17)

        title = response.xpath("//h1[@class='job-position-title m-t-0']/text()").get()
        #image process
        # image_style = response.xpath("//div[@class='employer-branding-image background-cover position-relative']/@style").get()
        # image = image_style.split("(")[1].replace(')','')

        #salary process
        salary = -1
        salary_span = response.xpath('//div[@class="flex-between-center flex-wrap-wrap"]/descendant::span[contains(text(),"تومان")]/text()').get()
        if salary_span :
            if salary_span.__contains__("تا"): salary = salary_span.split("تا")[0]
            else : salary = salary_span


        #job details 
        job_details = response.xpath('//div[@class="jop-position-info active-tab-data"]/div[1]')

        education = None
        education_xpath = job_details.xpath('.//descendant::span[contains(text(),"مقطع تحصیلی")]/following::div[1]/descendant::span/text()').get()

        if education_xpath :
            if education_xpath.__contains__(','): education = education_xpath.split(',')[0].replace('\n', '').replace('،','')
            else : education = education_xpath.replace('\n', '').replace('،','')

        cooperation = None
        cooperation_xpath = job_details.xpath('.//descendant::span[contains(text(),"نوع همکاری")]/following::div[1]/descendant::span/text()').get()
        
        teleworking = False
        if cooperation_xpath :
            if cooperation_xpath.__contains__("دورکاری") : teleworking = True
        
            if cooperation_xpath.__contains__('،'): cooperation = cooperation_xpath.split(',')[0].replace('\n', '').replace(',','')
            else : cooperation = cooperation_xpath.replace('\n', '').replace('،','')
        
        gender = job_details.xpath('.//descendant::span[contains(text(),"جنسیت")]/following::div[1]/descendant::span/text()').get()

        #process for set insurance and experience
        skills = response.xpath('//h3[contains(text(),"الزامات / مهارت‌ها")]/following-sibling::div/text()').get()
        skills_ul = response.xpath('//h3[contains(text(),"الزامات / مهارت‌ها")]/following-sibling::div[@class="md-text-size"]/ul')
        advantages_insurance = response.xpath('//h3[contains(text(),"مزایای شغلی")]/following-sibling::div[@class="md-text-size"]/ul/li[contains(text(),"بیمه")]')

        insurance = False
        experience = -1

        # insurance
        if advantages_insurance : insurance = True
        elif skills_ul :
            li_insurance = skills_ul.xpath('.//li[contains(text(),"بیمه")]')
            if li_insurance : insurance = True
        elif skills :
            for skill in skills: 
                if skill.__contains__('بیمه') : insurance = True
        
        # experience
        if skills_ul :
            li_experience = skills_ul.xpath('.//li[contains(text(),"سال سابقه")]/text()').get()
            if li_experience:
                for m in li_experience:
                    if m.isdigit():
                        experience = m
                        break
        elif skills:
            for skill in skills: 
                if skill.__contains__('سال سابقه') : 
                    for m in skill:
                      if m.isdigit():
                        experience = m
                        break

        # description
        descs = response.xpath('//h3[contains(text(),"شرح شغل / وظایف")]/following-sibling::div/descendant::node()/text()').extract()
            
        if descs : 
            self['description'] = ' , '.join(descs)
        
        # Storing Data
        if title : self['title'] = title.strip()
        if education : self['education'] = education.strip()
        self['insurnace'] = insurance
        if cooperation : self['cooperation'] = cooperation
        if salary : self['salary'] = salary
        if gender : self['gender'] = gender
        if experience : self['experience'] = experience
        self['teleworking'] = teleworking
        self['url'] = url.strip()
        
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