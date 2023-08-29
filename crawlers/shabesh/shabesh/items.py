# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from shabesh.utilities.uses import hash_token

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

class ShabeshItem(BaseItem,HomeBaseItem):
    def extract(self,response,stats):
        self['source_id'] = 24
        self['url'] = response.request.url
        token = self['url'].split('/')[4]
        if token : self['token'] = hash_token(token,24)
        self['city'] = 'تهران'

        # Picture
        self['thumbnail'] = response.xpath('(//picture/img/@src)[1]').get()

        # Details
        details = response.xpath('//div[@class="side-info text-center mt-3"]')

        title = details.xpath('.//span[@class="d-block fw-bold font-16 mt-3"]/text()').extract() 
        title = list(map(lambda x: x.strip() , title))
        self['title'] = f'{title[0]} آپارتمان {title[2]} {title[3]}'

        if self['title'].__contains__('فروش') :
            self['price'] = details.xpath('.//span[@class="d-block fw-bold font-20 mt-3"]/text()').get().replace('تومان','').strip()
        else :
            self['deposit'] = details.xpath('.//span[@class="d-block fw-bold font-20 mt-3"]/text()').get().replace('تومان','').strip()
            rent = details.xpath('.//span[@class="d-block fw-bold font-20 mt mt-3"]/text()')
            if rent :
                self['rent'] = details.xpath('.//span[@class="d-block fw-bold font-20 mt mt-3"]/text()').get().replace('تومان اجاره','').strip()
                

        self['area'] = details.xpath('.//descendant::i[@class="icons_shMeter2__FhIjt font-16"]/following-sibling::span/text()').get().strip()
        self['room'] = details.xpath('.//descendant::i[@class="icons_shBed2__R3PVt font-16"]/following-sibling::span/text()').get().strip()
        self['production'] = details.xpath('.//descendant::i[@class="icons_shCalendar__3qrT7 font-16"]/following-sibling::span/text()').get().strip()

        self['floor_covering'] = response.xpath('//div[@class="row mb-5"]/descendant::span[contains(text(),"نوع کفپوش")]/following-sibling::span/text()').get()

        # Desc
        self['description'] = response.xpath('//div[@class="w-100 global_preLine__tKFEh mt-4 mb-4 overflow-hidden "]/text()').get()

        # Feature
        feature = response.xpath('(//h2[contains(text(),"امکانات")]/following-sibling::div)[1]/div')

        parking = feature.xpath('.//span[contains(text(),"پارکینگ")]')
        if parking : self['parking'] = True
        else : self['parking'] = False

        elevator = feature.xpath('.//span[contains(text(),"آسانسور")]')
        if elevator : self['elevator'] = True
        else : self['elevator'] = False

        storeroom = feature.xpath('.//span[contains(text(),"انباری")]')
        if storeroom : self['storeroom'] = True
        else : self['storeroom'] = False

        balcony = feature.xpath('.//span[contains(text(),"بالکن")]')
        if balcony : self['balcony'] = True
        else : self['balcony'] = False
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
