# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import requests
from eestkhdam.utilities.uses import get_time_stamp, hash_token, get_province_center
from scrapy.utils.log import logger


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

class EestkhdamItem(BaseItem, RecruitmentBaseItem):
    def extract(self,is_table,response,stats,href):
        self['source_id'] = 11
        self['token'] = hash_token(href,11)
        self['time'] = get_time_stamp()
        if is_table == True:
            
            table_details_string = response.xpath('.//descendant::table[@class="table table-bordered table-striped"]').xpath('//tbody').extract_first()
            # Cooperation And Teleworking
            if 'نوع قرارداد' in table_details_string:
                if table_details_string.__contains__('تمام وقت') : self['cooperation'] = 'تمام وقت'
                if table_details_string.__contains__('پاره وقت') : self['cooperation'] = 'پاره وقت'
                if table_details_string.__contains__('پروژه ای') : self['cooperation'] = 'پروژه ای'
                if table_details_string.__contains__('توافقی') : self['cooperation'] = 'توافقی'
                if table_details_string.__contains__('کارآموزی') : self['cooperation'] = 'کارآموزی'
                if table_details_string.__contains__('مشاوره ای') : self['cooperation'] = 'مشاوره ای'
                if table_details_string.__contains__('دورکاری') : 
                    self['cooperation'] = 'دورکاری'
                    self['teleworking'] = True
                
            # Education
            if 'تحصیل'in table_details_string:
                if table_details_string.__contains__('دیپلم'): self['education'] = "دیپلم"
                if table_details_string.__contains__('فوق دیپلم'): self['education'] = "فوق دیپلم"
                if table_details_string.__contains__('کاردانی'): self['education'] = "کاردانی"
                if table_details_string.__contains__('لیسانس'): self['education'] = "لیسانس"
                if table_details_string.__contains__('فوق لیسانس'): self['education'] = "فوق لیسانس"

            # Privileges
            if 'بیمه' in  table_details_string:
                self['insurnace'] = True
            
            description = response.xpath('.//descendant::div[re:test(@class,"entry-content.*")]').xpath('string(//p)').extract_first()
            description += '\n' + '\n'.join(response.xpath('.//descendant::table[@class="table table-bordered table-striped"]/tbody/tr/td[1]/text()').extract())
            self['description'] = description

        else :
            # Province , Gender , Experience , Cooperation , Salary
            details = response.xpath('(//div[re:test(@class,"col-md-12.*")])')[1]
            
            province = details.xpath('.//descendant::div[contains(text(),"استان")]/following-sibling::div/span/text()').get()
            if province : self['province'] = province
            
            gender = details.xpath('.//descendant::div[contains(text(),"جنسیت")]/following-sibling::div/span/text()').get()
            if gender : self['gender'] = gender
            
            experience = details.xpath('.//descendant::div[contains(text(),"سابقه کار")]/following-sibling::div/span/text()').get()
            if experience : self['experience'] = experience
            
            cooperation = details.xpath('.//descendant::div[contains(text(),"نوع همکاری")]/following-sibling::div/span/text()').get()
            if cooperation :
                if cooperation.__contains__('دورکاری') : self['teleworking'] = True
                if cooperation.__contains__('،'):cooperation = self['cooperation'].split('،')[0]
                self['cooperation'] = cooperation
            
            salary = details.xpath('.//descendant::div[contains(text(),"حقوق")]/following-sibling::div/span/text()').get()
            if salary :
                if salary.__contains__('تا') : 
                    salary = salary.split("تا")[0]
                    for amount in salary :
                        if amount.isdigit(): salary = amount
                        break
                
                salary = salary.replace('از','')
                salary = salary.replace('میلیون','')
                salary = salary.replace('تومان','')
                self['salary'] = salary.strip()
            
            # Description , Education , Insurance
            description = response.xpath('//h3["font-size-16 font-weight-bold"][contains(text(),"شرایط احراز")]/parent::div//text()').extract()
            for text in description :
                if text.__contains__('حداقل مدرک') or text.__contains__('مدرک') :
                    if text.__contains__('دیپلم'): self['education'] = "دیپلم"
                    if text.__contains__('فوق دیپلم'): self['education'] = "فوق دیپلم"
                    if text.__contains__('کاردانی'): self['education'] = "کاردانی"
                    if text.__contains__('لیسانس'): self['education'] = "لیسانس"
                    if text.__contains__('فوق لیسانس'): self['education'] = "فوق لیسانس"

            self['description'] = " ".join(description)

            if response.xpath('//div[@class="entry-content pro-ad"]//node()[contains(text(),"بیمه")]'): self['insurnace'] = True
                
            # URL 
            self['url'] = response.request.url

        if not str(self['experience']).isdigit(): self['experience'] = 1

        if self['gender'].__contains__("آقا") : self['gender'] = 'مرد'
        elif self['gender'].__contains__("خانم") : self['gender'] = 'زن'

        if self['province'] == "کل کشور" : self['province'] = 'تهران'
        self['city'] = get_province_center(self['province'])

        # try:
        #     vector_text = (self['title'] if self['title'] != 'not_defined' else '') + (self['description'] if self['description'] != 'not_defined' else '')
        #     if vector_text != '':
        #         data = {
        #           "text_list": [
        #                 vector_text
        #             ],
        #         }
        #         r = requests.post('http://10.10.1.35:8001/get_embed', json=data)
        #         if r.status_code == 200:
        #             self['search_pgvector'] = r.text
        # except Exception as e:
        #     logger.critical(str(e))



        if not str(self['salary']).isdigit(): self['salary'] = -1