# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json
from khodro45.utilities.Normalize import clean_number, remove_extra_character_and_normalize
from khodro45.utilities.uses import get_production, get_time_stamp, hash_token, get_persian_year, extract_model_brand

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


class Khodro45CarItem(CarBaseItem, BaseItem):
    def extract(self, response,stats):
        """
        a method to extract data from response
        this method can be free style implement
        that means you can change arguments for your needs
        """
        res = json.loads(response.text)

        self['token'] = hash_token(res['slug'], 13)
        self['source_id'] = 13
        self['time'] = get_time_stamp()
        self['category'] = 'خودرو'
        self['sub_category'] = 'سواری'
        
        self['price'] = res['price']
        self['city'] = res['city']
        self['url'] = response.request.meta["car_url"]
        
        #car properties
        properties = res['car_properties']

        self['brand'] = properties['brand']
        self['model'] = properties['model']
        self['production'] = properties['year']
        self['title'] = f"{self['brand']} {self['model']} {self['production']}"
        
        #car specifications
        specifications = res['car_specifications']
        
        self['consumption'] = specifications['klm']
        self['fuel'] = specifications['fuel']
        self['color'] = specifications['color']
        self['gear_box'] = specifications['gearbox']

        #image
        images = res['car_images']
        self['thumbnail'] = images[0]['file']

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