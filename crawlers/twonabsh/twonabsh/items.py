# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from twonabsh.utilities.uses import hash_token

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

class TwonabshItem(BaseItem,HomeBaseItem):
    def extract(self,response,stats):
        self['source_id'] = 22
        self['url'] = response.request.url
        token = self['url'].split('/')[6].split('-')[1]
        if token : self['token'] = hash_token(token , 22)

        self['city'] = response.request.meta['cityName']
        self['thumbnail'] = response.request.meta['image']
        # image = response.xpath('(//img[@class="img-cover"])[1]')
        # if image :
        #     self['thumbnail'] = image.xpath('.//@src').get()
        
        title = response.xpath('////h1/address/text()').get()
        if title : self['title'] = title
        
        price = response.xpath('//div[@class="sc-1bo5vg3-4 dAjdrb d-flex align-items-center"]/span[1]/text()').get()
        if not (price.__contains__('رهن') or price.__contains__('اجاره')):
            self['price'] = price
        else :
            deposit = response.xpath('(//div[@class="sc-1bo5vg3-4 dAjdrb d-flex align-items-center"]/span/text())[1]').get()
            if deposit :
                if deposit.__contains__('رهن') : deposit = deposit.replace('رهن','').strip()

            rent = response.xpath('(//div[@class="sc-1bo5vg3-4 dAjdrb d-flex align-items-center"]/span/text())[2]').get()
            if rent :
                if rent.__contains__('اجاره') : rent = rent.replace('اجاره','').strip()

        # details 
        details = response.xpath('//div[@class="mt-8 row"]')

        area = details.xpath('.//descendant::span[contains(text(),"زیربنا")]/following-sibling::span/text()').get()
        if area : self['area'] = area

        bedroom = details.xpath('.//descendant::span[contains(text(),"خواب")]/following-sibling::span/text()').get()
        if bedroom : self['room'] = bedroom

        # features
        features = response.xpath("//h2[contains(text(),'تجهیزات و امکانات')]/following-sibling::div")

        if features.xpath("descendant::span[contains(text(),'پارکینگ')]") : self['parking'] = True
        if features.xpath("descendant::span[contains(text(),'بالکن')]") : self['balcony'] = True
        if features.xpath("descendant::span[contains(text(),'تراس')]") : self['balcony'] = True
        if features.xpath("descendant::span[contains(text(),'انباری')]") : self['storeroom'] = True
        if features.xpath("descendant::span[contains(text(),'پکیج')]") : self['package'] = True
        if features.xpath("descendant::span[contains(text(),'آسانسور')]") : self['elevator'] = True
        if features.xpath("descendant::span[contains(text(),'کولر گازی')]") : self['cooler'] = True
        
        # desc
        desc = response.xpath("//h2[contains(text(),'توضیحات تکمیلی')]/following-sibling::div/text()").extract()
        desc = list(map(lambda x : x.strip() , desc))

        if desc :
            self['description'] = desc

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
