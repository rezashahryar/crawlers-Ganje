# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json
from banikhodro.utilities.Normalize import clean_number, remove_extra_character_and_normalize
from banikhodro.utilities.uses import get_production, get_time_stamp, hash_token, get_persian_year, extract_model_brand

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


class BanikhodroItem(BaseItem, CarBaseItem):
    # define the fields for your item here like:
    def extract(self,response,stats):
        
        token = response.xpath('//title/text()').get()
        token = token.split(' ')[-1]

        self['token'] = hash_token(token, 13)
        self['source_id'] = 13
        self['time'] = get_time_stamp()
        self['category'] = 'خودرو'
        self['sub_category'] = 'سواری'

        #details 
        details = response.xpath('(//div[@class="inforow newinfo"])[2]')
        
        # title , year , brand , model
        title = details.xpath('.//div[@class="inforight"]//h2')
        year = title.xpath('.//span[@itemprop="releaseDate"]/text()').get()
        brand = title.xpath('.//span[@itemprop="brand"]/text()').get()
        model = title.xpath('.//span[@itemprop="model"]/text()').get()

        title = f"{brand} {model} {year}"

        # property
        properties = details.xpath('.//div[@class="inforight"]/p')

        # price , consumption , gear_box , fuel , body_condition , color , province
        price = properties.xpath('.//span[@itemprop="Offers"]/following-sibling::span/text()').get()
        
        consumption = properties.xpath('.//span[contains(text(),"کارکرد")]/following-sibling::span/text()').get()
        if consumption :
            consumption = consumption.replace('\n','').replace('\r','').replace('کیلومتر' , '').strip()

        gear_box = properties.xpath('.//span[contains(text(),"گیربکس")]/following-sibling::span/text()').get()
        if gear_box :
            gear_box = gear_box.replace('\n','').replace('\r','').strip()

        fuel = properties.xpath('.//span[contains(text(),"سوخت")]/following-sibling::span/text()').get()
        if fuel :
            fuel = fuel.replace('\n','').replace('\r','').strip()

        body_condition = properties.xpath('.//span[contains(text(),"بدنه")]/following-sibling::span/text()').get()
        if body_condition :
            body_condition = body_condition.replace('\n','').replace('\r','').strip()

        color = properties.xpath('.//descendant::f[@itemprop="color"]/text()').get()
        province = properties.xpath('.//span[contains(text(),"استان")]/following-sibling::span/text()').get()

        # description
        description = details.xpath('.//descendant::span[@itemprop="description"]/text()').get()

        # image
        # https://www.banikhodro.com/AdvertiseImages/Cars/159488_6.jpg
        # image = response.xpath("//div[@class='hidden-sm hidden-xs']//div[4]//a[1]//img[1]/@src").get()
        # # thumbnail = f"https://www.banikhodro.com{image}"
        # if not image : 
        #     image = response.xpath('//div[@style="float:left;padding-top:10px;"]/div/img/@src').get()
        thumbnail =  f"https://www.banikhodro.com{response.request.meta['thumb']}"
             
        # URL
        url = response.request.url

        # Extraction
        if title : self['title'] = title
        if year : self['production'] = year
        if brand : self['brand'] = brand
        if model : self['model'] = model

        if price : self['price'] = price
        if consumption : self['consumption'] = consumption
        if gear_box : self['gear_box'] = gear_box
        if fuel : self['fuel'] = fuel
        if body_condition : self['body_condition'] = body_condition
        if color : self['color'] = color
        if province : self['province'] = province

        if description : self['description'] = description

        if thumbnail : self['thumbnail'] = thumbnail

        if url : self['url'] = url

        # Calculate Statistics Of Broken Fields
        if self['title'] == 'not_defined' or self['title'] == '': stats.specify_the_broken_one('title')
        
        if self['province'] == 'not_defined' or self['province'] == '': stats.specify_the_broken_one('province')
            
        if self['production'] == -1 : stats.specify_the_broken_one('production')

        if self['token'] == -1 : stats.specify_the_broken_one('token')    
        
        if self['brand'] == 'not_defined' or self['brand'] == '':stats.specify_the_broken_one('brand')
            
        if self['consumption'] == -1: stats.specify_the_broken_one('consumption')

        if self['price'] == -1: stats.specify_the_broken_one('price')    
        
        if self['color'] == 'not_defined' or self['color'] == '': stats.specify_the_broken_one('color')

        if self['cash_installment'] == 'not_defined' or self['cash_installment'] == '': stats.specify_the_broken_one('cash_installment')

        if self['gear_box'] == 'not_defined' or self['gear_box'] == '': stats.specify_the_broken_one('gear_box')
        
        if self['company'] == 'not_defined' or self['company'] == '': stats.specify_the_broken_one('company')

        if self['chassis_type'] == 'not_defined' or self['chassis_type'] == '': stats.specify_the_broken_one('chassis_type')
        
        if self['model'] == 'not_defined' or self['model'] == '': stats.specify_the_broken_one('model')
        
        if self['body_condition'] == 'not_defined' or self['body_condition'] == '': stats.specify_the_broken_one('body_condition')
            
        if self['fuel'] == 'not_defined' or self['fuel'] == '': stats.specify_the_broken_one('fuel')

        # Broken Items Stats
        stats.calculate_the_broken_stats()