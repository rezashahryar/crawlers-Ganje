# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from iranestekhdam.utilities.uses import hash_token , check_educatuin_is_valid , get_time_stamp

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

class IranestekhdamItem(BaseItem, RecruitmentBaseItem):
    def extract(self,response,stats,token):
        self['source_id'] = 12
        self['token'] = hash_token(token , 12)
        # Title
        title = response.xpath('//h1[@class="d-none d-md-block"]/a/text()').get()
        if title : self['title'] = title
        self['time'] = get_time_stamp()

        # URL
        self['url'] = response.request.url

        # # City
        # city = response.xpath("//div[@class='state']/text()").get()
        # if city : self['city'] = city

        # Details
        details = response.xpath('//div[@class="col-12 col-md-8 col-lg-7"]')

        # Education
        education = details.xpath('.//descendant::i[@class="fal fa-graduation-cap"]/following-sibling::span/text()').get()
        if education : 
            if education.__contains__(','):
                education = education.split(',')[0]

            self['education'] = education.strip().replace('\n','')

        # Experience
        experience = details.xpath('.//descendant::i[@class="fal fa-briefcase"]/following-sibling::span/text()').get()
        exp_amount = ""
        if experience :
            for year in experience:
                if year == "ت" : break
                if year.isdigit():
                     exp_amount += year
                     if len(exp_amount) == 2: break

            self['experience'] = exp_amount

        # Salary
        salary = details.xpath('.//descendant::i[@class="fal fa-credit-card"]/following-sibling::span/text()').get()
        amount = ""
        if salary:
            for m in salary:
                if m == "تا" : break
                if m.isdigit():
                    amount = amount + m
                    if len(amount) == 2 : break
            self['salary'] = amount

        # Gender
        gender = details.xpath('.//descendant::i[@class="fal fa-user"]/following-sibling::span/text()').get()
        if gender : self['gender'] = gender

        # Cooperation
        cooperation = details.xpath('.//descendant::i[@class="fal fa-clock"]/following-sibling::span/text()').get()
        if cooperation : 
            # Teleworking
            if cooperation.__contains__("دورکاری"): self['teleworking'] = True
            if cooperation.__contains__(','):
                cooperation = cooperation.split(',')[0]

            self['cooperation'] = cooperation
        
        # Insurance
        t_datas = response.xpath("//table/descendant::td/text()").extract()
        if t_datas.__contains__("بیمه") : self['insurnace'] = True

        # Description
        desc = response.xpath('//table/descendant::td[contains(text(),"شرایط احراز")]/following::td[@style="text-align: right;"]/text()').extract()
        if desc :
            self['description'] = ' , '.join(desc)
            

        #Validation
        if not str(self['experience']).isdigit() or self['experience'] == -1: self['experience'] = 1

        if self['gender'].__contains__("آقا") or self['gender'].__contains__("مرد") : self['gender'] = 'مرد'
        elif self['gender'].__contains__("خانم") or self['gender'].__contains__("زن") : self['gender'] = 'زن'

        if not str(self['salary']).isdigit() or self['salary'] == -1 : self['salary'] = -1

        if not check_educatuin_is_valid(self['education']) : self['education'] = 'not_defined'
        # Calculate Statistics Of Broken Fields
        

        if self['education'] == 'not_defined' or self['education'] == '': stats.specify_the_broken_one('education')
            
        if self['insurnace'] == 'not_defined' or self['insurnace'] == '': stats.specify_the_broken_one('insurnace')
            
        if self['cooperation'] == 'not_defined' or self['cooperation'] == '':stats.specify_the_broken_one('cooperation')
            
        if self['salary'] == -1: stats.specify_the_broken_one('salary')
            
        if self['gender'] == 'not_defined' or self['gender'] == '': stats.specify_the_broken_one('gender')
            
        if self['experience'] == -1: stats.specify_the_broken_one('experience')
            
        if self['teleworking'] == 'not_defined' or self['teleworking'] == '': stats.specify_the_broken_one('teleworking')     

        stats.calculate_the_broken_stats()   