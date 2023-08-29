# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from mashinbank.utilities.uses import hash_token

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


class MashinbankItem(BaseItem,CarBaseItem):
    """Mashin Bank Item"""
    def extract(self,response,stats):
        """Method For Exracting Data"""

        # title , source id, url , token
        title = response.xpath('//h1[@class="car-title mb-2"]/text()').get()

        self['source_id'] = 18
        self['url'] = response.request.url

        token = self['url'].split('/')[4]
        if token : self['token'] = hash_token(token,18)

        # province , city
        province_city = response.xpath('//span[@class="car-city"]/text()').get()
        province_city = list(map(lambda x : x.strip() , province_city.split('،')))

        province = province_city[0]
        city = province_city[1]

        # price 
        price = response.xpath('//p[@class="car-price"]/text()').get()
        
        # details 
        details = response.xpath('//div[@class="row car-info"]')

        consumption = details.xpath('.//div[1]/span/text()').get()
        color = details.xpath('.//div[2]/span/text()').get()
        body_condition = details.xpath('.//div[3]/span/text()').get()

        # info 
        info = response.xpath('//ul[@class="car-details"]')

        chassis_type = info.xpath('.//li[contains(text(),"نوع شاسی")]/span/text()').get()
        gearbox = info.xpath('.//li[contains(text(),"گیربکس")]/span/text()').get()
        fuel = info.xpath('.//li[contains(text(),"نوع سوخت")]/span/text()').get()

        # description
        desc = response.xpath('//pre[@class="car-description"]/text()').get()

        # Storing Data
        if title : self['title'] = title

        if province : self['province'] = province
        if city : self['city'] = city

        if price : 
            price = price.strip()
            if str(price)[0].isdigit() : self['price'] = price
        
        if consumption : 
            if str(consumption)[0].isdigit() : self['consumption'] = consumption
        if color : self['color'] = color
        if body_condition : self['body_condition'] = body_condition

        if chassis_type : self['chassis_type'] = chassis_type
        if gearbox : self['gear_box'] = gearbox
        if fuel : self['fuel'] = fuel

        if desc : self['description'] = desc

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
