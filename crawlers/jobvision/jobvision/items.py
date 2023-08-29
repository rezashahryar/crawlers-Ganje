# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy , re

from jobvision.utilities.uses import hash_token , get_time_stamp

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

class JobvisionItem(BaseItem,RecruitmentBaseItem):
    def extract(self,response,stats):
        # title , source id , url , token
        if response['isPersian'] :
            title = response['title']
            self['source_id'] = 18
            token = response['id']
            self['url'] = f"https://jobvision.ir/jobs/{token}"
            if token : self['token'] = hash_token(token , 18)
            self['time'] = get_time_stamp()

            # Teleworking
            teleworking = response['isRemote']
            experience = response['requiredRelatedExperienceYears']

            # Category
            category = response['jobCategories'][0]['titleFa']

            # Location
            province = "not_defined"
            try:
                province = response['location']['province']['titleFa']
            except : None
            city = response['location']['city']['titleFa']

            # Cooperation
            cooperation = response['workType']['titleFa']

            if cooperation.__contains__("یا"):
                cooperation = cooperation.split('یا')[0]

            if cooperation.__contains__("/"):
                cooperation = cooperation.split('/')[0].strip()

            # Insurance
            benefits = response['benefits']
            for benfit in benefits:
                if benfit['titleFa'].__contains__('بیمه') : self['insurnace'] = True

            # Salary
            salary = response['salary']
            if salary :
                salary = salary['titleEn']
                if salary :
                    salary = salary.split('-')[0]
                    salary = int(re.search(r'\d+', salary).group())
                
            # Gender
            gender = response['gender']['titleFa']

            if gender.__contains__("تفاوتی ندارد") : gender = 'مرد'
            if gender.__contains__('مرد') or gender.__contains__('آقا') : gender = 'مرد'
            elif gender.__contains__('زن') or gender.__contains__('خانم') : gender = 'زن'
            else : gender = None
        
            # Description
            desc = response['description']

            # Storing Data
            if title : self['title'] = title.strip()
            if city : self['city'] = city.strip()
            if category : self['category'] = category
            if province : self['province'] = province.strip()
            if cooperation : self['cooperation'] = cooperation
            if salary : self['salary'] = str(salary) + "000000"
            if gender : self['gender'] = gender
            if str(experience).isdigit() : self['experience'] = experience
            if teleworking : self['teleworking'] = teleworking
            if desc : self['description'] = desc
            
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
