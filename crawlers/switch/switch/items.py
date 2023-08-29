# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from switch.utilities.uses import hash_token

class BaseItem(scrapy.Item):
    token = scrapy.Field()
    source_id = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    production = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    thumbnail = scrapy.Field()
    tell = scrapy.Field()
    swap = scrapy.Field()

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
        self['production'] = -1
        self['price'] = -1
        self['description'] = 'not_defined'
        self['url'] = 'not_defined'
        self['thumbnail'] = 'not_defined'
        self['tell'] = 'not_defined'
        self['swap'] = None
        

class CarBaseItem(scrapy.Item):
    brand = scrapy.Field()
    consumption = scrapy.Field()
    color = scrapy.Field()
    cash_installment = scrapy.Field()
    gear_box = scrapy.Field()
    company = scrapy.Field()
    chassis_type = scrapy.Field()
    model = scrapy.Field()
    body_condition = scrapy.Field()
    fuel = scrapy.Field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['brand'] = 'not_defined'
        self['consumption'] = -1
        self['color'] = 'not_defined'
        self['cash_installment'] = 'not_defined'
        self['gear_box'] = 'not_defined'
        self['company'] = 'not_defined'
        self['chassis_type'] = 'not_defined'
        self['model'] = 'not_defined'
        self['body_condition'] = 'not_defined'
        self['fuel'] = 'not_defined'

class SwitchItem(BaseItem,CarBaseItem):
    def extract(self,response,details,stats):
        self['source_id'] = 21
        self['url'] = response.request.url
        self['token'] = hash_token(details['id'],21)

        # details
        year = details['year']
        price = details['price']
        brand = details['brand']
        model = details['model']
        consumption = details['consumption']
        image = f"https://www.switch.ir/FileServer/api/v1/optimize/{details['image']}/535/300/60"
        title = f'{brand} {model} {year}'

        body_condition = response.xpath('//span["_ngcontent-serverapp-c133"][contains(text(),"وضعیت بدنه:")]/following-sibling::span/text()').get()
        color = response.xpath('//span["_ngcontent-serverapp-c133"][contains(text(),"رنگ بدنه:")]/following-sibling::span/span[2]/text()').get()
        desc = response.xpath('//span["_ngcontent-serverapp-c133"][contains(text(),"توضیحات:")]/following-sibling::span/text()').get()
        
        # Validation
        if price == 0 : price = -1

        # Storing Data
        self['production'] = year
        self['price'] = price
        self['brand'] = brand
        self['model'] = model
        self['consumption'] = consumption
        self['thumbnail'] = image
        self['title'] = title
        self['body_condition'] = body_condition
        self['color'] = color
        self['description'] = desc

        # Calculate Statistics Of Broken Fields
        if self['title'] == 'not_defined' or self['title'] == '': stats.specify_the_broken_one('title')
        
        if self['province'] == 'not_defined' or self['province'] == '': stats.specify_the_broken_one('province')
            
        if self['production'] == -1 : stats.specify_the_broken_one('production')

        if self['token'] == -1 : stats.specify_the_broken_one('token')    
        
        if self['brand'] == 'not_defined' or self['brand'] == '':stats.specify_the_broken_one('brand')
            
        if self['consumption'] == -1: stats.specify_the_broken_one('consumption')

        if self['price'] == -1 : stats.specify_the_broken_one('price')    
        
        if self['color'] == 'not_defined' or self['color'] == '': stats.specify_the_broken_one('color')

        if self['cash_installment'] == 'not_defined' or self['cash_installment'] == '': stats.specify_the_broken_one('cash_installment')

        if self['gear_box'] == 'not_defined' or self['gear_box'] == '': stats.specify_the_broken_one('gear_box')
        
        if self['company'] == 'not_defined' or self['company'] == '': stats.specify_the_broken_one('company')

        if self['chassis_type'] == 'not_defined' or self['chassis_type'] == '': stats.specify_the_broken_one('chassis_type')
        
        if self['model'] == 'not_defined' or self['model'] == '': stats.specify_the_broken_one('model')
        
        if self['body_condition'] == 'not_defined' or self['body_condition'] == '': stats.specify_the_broken_one('body_condition')
            
        if self['fuel'] == 'not_defined' or self['fuel'] == '': stats.specify_the_broken_one('fuel')

        # Broken Statistics
        stats.calculate_the_broken_stats()
