# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from pyexpat import features
import scrapy
from iranfile.utilities.uses import hash_token

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
    production = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    thumbnail = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    tell = scrapy.Field()
    swap = scrapy.Field()

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self['token'] = -1
        self['source_id'] = -1
        self['time'] = -1
        self['title'] = 'not_defined'
        self['category'] = 'not_defined'
        self['sub_category'] = 'not_defined'
        self['province'] = 'not_defined'
        self['city'] = 'not_defined'
        self['neighbourhood'] = 'not_defined'
        self['production'] = -1
        self['price'] = -1
        self['description'] = 'not_defined'
        self['url'] = 'not_defined'
        self['thumbnail'] = 'not_defined'
        self['latitude'] = -1
        self['longitude'] = -1
        self['tell'] = 'not_defined'
        self['swap'] = None

class HomeBaseItem(scrapy.Item):
    advertiser = scrapy.Field()
    room = scrapy.Field()
    area = scrapy.Field()
    deposit = scrapy.Field()
    rent = scrapy.Field()
    administrative_document = scrapy.Field()
    parking = scrapy.Field()
    elevator = scrapy.Field()
    storeroom = scrapy.Field()
    swap_deposit_rent = scrapy.Field()
    balcony = scrapy.Field()
    estate_floor = scrapy.Field()
    estate_direction = scrapy.Field()
    package = scrapy.Field()
    kitchen = scrapy.Field()
    cooler = scrapy.Field()
    floor_covering = scrapy.Field()

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self['advertiser'] = 'not_defined'
        self['room'] = -1
        self['area'] = -1
        self['deposit'] = -1
        self['rent'] = -1
        self['administrative_document'] = None
        self['parking'] = None
        self['elevator'] = None
        self['storeroom'] = None
        self['swap_deposit_rent'] = None
        self['balcony'] = None
        self['cooler'] = None
        self['package'] = None
        self['estate_floor'] = -1
        self['estate_direction'] = 'not_defined'
        self['kitchen'] = 'not_defined'
        self['floor_covering'] = 'not_defined'

class IranfileItem(BaseItem,HomeBaseItem):
    def extract(self,response,stats):
        self['source_id'] = 23
        self['url'] = response.request.url
        self['token'] = hash_token(response.request.meta['token'],23)
        self['city'] = "تهران"
        self['title'] = response.request.meta['title']

        is_rent = response.request.meta['is_rent']

        if is_rent :
            self['deposit'] = response.request.meta['deposit']
            self['rent'] = response.request.meta['rent']
        else :
            self['price'] = response.request.meta['price']
        # has_price = response.xpath('//div[@class="col-xxs-12 col-xs-4 for-print"][1]/span[1]/text()').get()
        # if has_price :
        #     if has_price.__contains__('قیمت کل'):
        #         self['price'] = response.xpath('//div[@class="col-xxs-12 col-xs-4 for-print"][1]/span[@class="file-data for-print"]/text()').get()

        #     else :
        #         self['deposit'] = response.xpath('//div[@class="col-xxs-12 col-xs-4 for-print"][1]/span[@class="file-data for-print"]/text()').get()
        #         self['rent'] = response.xpath('//div[@class="col-xxs-12 col-xs-4 for-print"][2]/span[@class="file-data for-print"]/text()').get()
        
        # details
        details = response.xpath('//table')

        self['area'] = details.xpath('.//tr[2]/td[2]/text()').get().strip()
        self['room'] = details.xpath('.//tr[3]/td[2]/text()').get().strip()
        self['kitchen'] = details.xpath('.//tr[5]/td[2]/text()').get().strip()
        self['floor_covering'] = details.xpath('.//tr[7]/td[2]/text()').get().strip()
        
        parking = details.xpath('.//tr[9]/td[2]/i/@class').get()
        if parking :
            if parking.__contains__('file-checked'): self['parking'] = True
            else : self['parking'] = False

        storeroom = details.xpath('.//tr[10]/td[2]/i/@class').get()
        if storeroom :
            if storeroom.__contains__('file-checked'): self['storeroom'] = True
            else : self['storeroom'] = False
        
        balcony = details.xpath('.//tr[11]/td[2]/i/@class').get()
        if balcony :
            if balcony.__contains__('file-checked'): self['balcony'] = True
            else : self['balcony'] = False

        # features
        features = response.xpath('//div[@style="display:flex;flex-direction:row;align-items:center;justify-content:flex-start;flex-wrap:wrap;gap:20px 50px"]')

        cooler = features.xpath('.//descendant::span[contains(text(),"کولر")]').get()
        if cooler: self['cooler'] = True
        else : self['cooler'] = False

        elevator = features.xpath('.//descendant::span[contains(text(),"آسانسور")]').get()
        if elevator: self['elevator'] = True
        else : self['elevator'] = False

        package = features.xpath('.//descendant::span[contains(text(),"پکیج")]').get()
        if package: self['package'] = True
        else : self['package'] = False

        # desc
        desc = response.xpath('//div[@id="descriptionContainer"]/div[2]/text()').get()
        if desc : self['description'] = desc

        # Calculate Statistics Of Broken Fields
        if self['title'] == 'not_defined' or self['title'] == '': stats.specify_the_broken_one('title')
        
        # if self['city'] == 'not_defined' or self['city'] == '': stats.specify_the_broken_one('city')
        
        # if self['thumbnail'] == 'not_defined' or self['thumbnail'] == '': stats.specify_the_broken_one('thumbnail')
        
        if self['url'] == 'not_defined' or self['url'] == '': stats.specify_the_broken_one('url')
            
        # if self['production'] == -1 : stats.specify_the_broken_one('production')

        # if self['token'] == -1 : stats.specify_the_broken_one('token')    
        
        # if self['room'] == -1 : stats.specify_the_broken_one('room')    
            
        # if self['area'] == -1 : stats.specify_the_broken_one('area')    

        # if self['price'] == -1: stats.specify_the_broken_one('price')  
        
        # if self['deposit'] == -1: stats.specify_the_broken_one('deposit')

        # if self['rent'] == -1: stats.specify_the_broken_one('rent')
        
        # Broken Items Stats
        stats.calculate_the_broken_stats()
