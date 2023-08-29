# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from jobinja.utilities.uses import hash_token , get_time_stamp

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

class JobinjaItem(BaseItem,RecruitmentBaseItem):
    def extract(self,response,stats):
        # Source_Id , URL , Token
        self["source_id"] = 16
        url = response.request.url
        token = url.split("/")[6]
        if token : self['token'] = hash_token(token , 16)

        # Title
        title = response.xpath('//div[@class="c-jobView__titleText"]')
        title = title.xpath('string()').get()
        self['time'] = get_time_stamp()

        # Details 
        details = response.xpath('//ul[@class="c-jobView__firstInfoBox c-infoBox"]')

        category = details.xpath('.//descendant::h4[contains(text(),"دسته‌بندی شغلی")]/following-sibling::div/span/text()').get()
        cooperation = details.xpath('.//descendant::h4[contains(text(),"نوع همکاری")]/following-sibling::div/span/text()').get()

        if cooperation :
            if cooperation.__contains__('دورکاری') : self['teleworking'] = True

        experience = details.xpath('.//descendant::h4[contains(text(),"حداقل سابقه کار")]/following-sibling::div/span/text()').get()

        salary = details.xpath('.//descendant::h4[contains(text(),"حقوق")]/following-sibling::div/span/text()').get()

        province_city = details.xpath('.//descendant::h4[contains(text(),"موقعیت مکانی")]/following-sibling::div/span/text()').get()
        province = province_city.split("،")[0]
        city = province_city.split("،")[1]

        # Description
        desc = response.xpath('//div[@class="o-box__text s-jobDesc c-pr40p"]//text()').extract()
        if desc :
            desc = ' , '.join(desc)

        # Info
        info = response.xpath('//ul[@class="c-infoBox"]')

        gender = info.xpath('.//descendant::h4[contains(text(),"جنسیت")]/following-sibling::div/span/text()').get()
        education = info.xpath('.//descendant::h4[contains(text(),"حداقل مدرک تحصیلی")]/following-sibling::div/span/text()').get()

        for text in desc :
            if text.__contains__("بیمه") : self['insurnace'] = True

        # Validation
        if salary :
            if salary.__contains__("توافقی"): salary = -1
            else :
                salary = salary.replace('تومان','')
                if salary.__contains__("از") : salary = salary.replace("از",'')
            
            if str(salary).__contains__('کار') : salary = -1

        if gender :
            if gender.__contains__("مرد") or gender.__contains__("آقا") : gender = 'مرد'
            elif gender.__contains__("زن") or gender.__contains__("خانم") : gender = 'زن'
            else : gender = "not_defined"

        if experience :
            if experience.__contains__("مهم نیست"): experience = -1
            else :
                if experience.__contains__("یک") : experience = 1
                elif experience.__contains__("دو") : experience = 2
                elif experience.__contains__("سه") : experience = 3
                elif experience.__contains__("چهار") : experience = 4
                elif experience.__contains__("پنج") : experience = 5
                elif experience.__contains__("شش") : experience = 6
                elif experience.__contains__("هفت") : experience = 7
                elif experience.__contains__("هشت") : experience = 8
                elif experience.__contains__("نه") : experience = 9
                elif experience.__contains__("ده") : experience = 10
        
        if education :
            if education.__contains__("مهم نیست"): education = "not_defined"

        if cooperation :
            if cooperation.__contains__('،'): cooperation = cooperation.split('،')[0]

        # Storing Data
        if url : self['url'] = url.strip()
        if title : self['title'] = title.strip()
        if category : self['category'] = category.strip()
        if cooperation : self['cooperation'] = cooperation.strip()
        if experience : self['experience'] = experience
        if salary : self['salary'] = salary
        if desc : self['description'] = desc
        if gender : self['gender'] = gender
        if education : self['education'] = education
        if province : self['province'] = province.strip()
        if city : self['city'] = city

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