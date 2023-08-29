# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from irantalent.utilities.uses import hash_token , get_time_stamp

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

class IrantalentItem(BaseItem,RecruitmentBaseItem):
    def extract(self,response,stats):
        # Source Id , Token , Title , URL
        self['source_id'] = 19
        token = response['id']
        if token : self['token'] = hash_token(token,19)
        self['time'] = get_time_stamp()
        title = response['title_farsi']
        self['url'] = f'https://www.irantalent.com/job/posm-manager/{token}'

        # logo = response['brand_data']['logo_url']
        # city = brand_data['location']['title_farsi']
        city = response['location_text_farsi']
        
        # Desc
        desc = response['role_description_farsi']

        # salary
        salary = response['salary_from']

        # cooperation
        cooperation = response['employment_type']['title']

        if cooperation == "Full Time": cooperation = 'تمام وقت'
        elif cooperation == 'Part Time': cooperation = 'پاره وقت'
        elif cooperation == 'Internship': cooperation = 'کارآموزی'


        # Storing Data
        if title : self['title'] = title.strip()
        if city : self['city'] = city.strip()
        # if province : self['province'] = province.strip()
        if cooperation : self['cooperation'] = cooperation
        if salary : self['salary'] = salary
        if desc : self['description'] = desc
        # if logo : self['thumbnail'] = logo
        # if gender : self['gender'] = gender
        # if str(experience).isdigit() : self['experience'] = experience
        # if teleworking : self['teleworking'] = teleworking
        
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
