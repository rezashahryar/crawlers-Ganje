# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from quera.utilities.Normalize import clean_number, remove_extra_character_and_normalize
from quera.utilities.uses import get_production, get_time_stamp, hash_token, get_persian_year
from quera.utilities.db_work import get_province


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


class RecruitmentBaseItem(scrapy.Item):
    education = scrapy.Field()
    insurnace = scrapy.Field()
    cooperation = scrapy.Field()
    salary = scrapy.Field()
    gender = scrapy.Field()
    experience = scrapy.Field()
    teleworking = scrapy.Field()
    search_pgvector = scrapy.Field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['education'] = 'not_defined'
        self['insurnace'] = 'not_defined'
        self['cooperation'] = 'not_defined'
        self['salary'] = -1
        self['gender'] = 'not_defined'
        self['experience'] = -1
        self['teleworking'] = 'not_defined'
        self['search_pgvector'] = 'not_defined'
        

class QueraItem(BaseItem, RecruitmentBaseItem):
    def extract(self, response,stats):
        """
        a method to extract data from response
        this method can be free style implement
        that means you can change arguments for your needs
        """
        self['token'] = hash_token(response['pk'], 13)
        self['source_id'] = 14
        self['time'] = get_time_stamp()
        self['category'] = 'برنامه نویسی'

        self['url'] = f"https://quera.org/magnet/jobs/{response['pk']}"
        self['title'] = response['title']
        try:
            self['city'] = response['city']['name']
        except:
            self['city'] = 'تهران'
        province = get_province(self['city'])
        self['province'] = province['p']
        self['city'] = province['c']
        
        # Gender
        gender = None
        if self['title'].lower().__contains__("آقا") or self['title'].lower().__contains__("male"):gender = 'مرد'
        elif self['title'].lower().__contains__("خانم") or self['title'].lower().__contains__("female"): gender = 'زن'
        self['gender'] = gender
        
        # Insurance
        insurance = False
        if 'بیمه' in response['description'] or 'بیمه' in response['requirements']:
            insurance = True
        self['insurnace'] = insurance

        # Cooperation
        try:
            self['cooperation'] = response['collaboration_type']
        except:
            self['cooperation'] = 'not_defined'

        # Salary
        try:
            salary = response['salary']
            if salary.__contains__("تا") : salary = salary.split('تا')[0]
            self['salary'] = salary
        except:
            self['salary'] = -1

        # Teleworking
        teleworking = False 
        try:
            if response['offers_remote'] : teleworking = True
            self['teleworking'] = teleworking
        except:
            self['teleworking'] = 'not_defined'

        # Description
        try:
            self['description'] = response['requirements']
        except:
            self['description'] = response['description']

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