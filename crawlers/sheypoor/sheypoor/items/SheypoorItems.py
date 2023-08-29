import scrapy
from sheypoor.items.items import BaseItem
from sheypoor.utilities.uses import hash_token,get_time_stamp, extract_model_brand
from sheypoor.utilities.Normalize import clean_number
import re
import logging

# map website attributes to database field names
attribute_map_table = {
            # Normal Cars
            "نوع شاسی" : "chassis_type",
            "گیربکس" : "gear_box",
            "سال تولید" : "production", 
            "نقدی/اقساطی" : "cash_installment",
            "مدل خودرو" : "model",
            "وضعیت بدنه" : "body_condition",
            "رنگ" : "color",
            "نوع سوخت" : "fuel",
            'کیلومتر' : "consumption",
            "لینک وب‌سایت	" : "dealer",

            # Motorcycles
            "حجم موتور" : "engine_cap",
            "نوع فروش" : "cash_installment",
            "تیپ" : "motorcycle_type",          

            # Accessories
            "نوع لوازم و قطعات" : "accessory_type"

            # Trucks and Heavy Vehicles
            # No specific attribs found in the website - so far

            # Classic Cars
            # No specific attribs found in the website - so far

            # Agricultral and Civil vehicles
            # No specific attribs found in the website - so far
}

# SheypoorItemBase
class SheypoorItemBase(BaseItem):
    dealer = scrapy.Field() #-----
    def extract(self, data):
        self['dealer'] = 'not_defined'
        self['url'] = f"https://www.sheypoor.com/{data.css('#item-details > p.description::attr(data-reveal-description)').extract_first()}"
        self['token'] = hash_token(data.css('#item-details > p.description::attr(data-reveal-description)').extract_first(), 2)
        self['source_id'] = 2
        self['time'] = get_time_stamp()
        self['province'] = data.css('#breadcrumbs > ul > li:nth-child(2) > a::text').extract_first().strip().replace('استان', '').replace('‌ ', '')
        self['city'] = data.css('#breadcrumbs > ul > li:nth-child(3) > a::text').extract_first().strip().replace('‌',' ')
        self['description'] = ''.join([item for item in data.css('#item-details > p.description::text').extract()])
        self['thumbnail'] = data.xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/img").css("::attr(data-srcset)").extract_first()
        if self['thumbnail'] is None :
            try:
                self['thumbnail'] = data.css('div.swiper-slide.swiper-zoom-container.swiper-slide-active > img::attr(src)').extract_first()
                if self['thumbnail'] is None:
                    self['thumbnail'] = data.css("#item-images > div.wrapper > div > div > div").css("img")[0].css("::attr(src)").extract_first()
            except:
                self['thumbnail'] = 'not_defined'
        self['neighbourhood'] = 'not_defined'

        try:
            self['title'] = data.css('#item-details > div > h1::text').extract_first().strip()
        except:
            pass
        try:
            self['price'] = data.css("#item-details > p.text-left > span.clearfix.pull-left.text-right > span > strong::text").extract_first().replace(',', '')
        except:
            pass


class SheypoorItemVehicle(scrapy.Item):
    tell = scrapy.Field()
    swap = scrapy.Field()
    model = scrapy.Field()              # car, truck, classic
    brand = scrapy.Field()              # car, truck, classic
    chassis_type = scrapy.Field()       # car, classic
    gear_box = scrapy.Field()           # car, truck, classic
    cash_installment = scrapy.Field()   # car, truck, classic
    body_condition = scrapy.Field()     # car, truck, classic
    color = scrapy.Field()              # car, truck, classic
    fuel = scrapy.Field()               # car, truck, classic
    consumption = scrapy.Field()        # car, truck, classic
    company = scrapy.Field()
    production = scrapy.Field()
    tip = scrapy.Field()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['brand'] = 'not_defined'
        self['consumption'] = -1
        self['company'] = 'not_defined'
        self['tell'] = 'not_defined'
        self['swap'] = 'not_defined'
        self['model'] = 'not_defined'
        self['color'] = 'not_defined'
        self['cash_installment'] = 'not_defined'
        self['body_condition'] = 'not_defined'
        self['chassis_type'] = 'not_defined'
        self['fuel'] = 'not_defined'
        self['gear_box'] = 'not_defined'
        self['production'] = 'not_defined'
        self['tip'] = 'not_defined'
        

class SheypoorItemCar(SheypoorItemVehicle, SheypoorItemBase):  
    def extract(self, data):
        super().extract(data)
        self['category'] = 'خودرو'
        self['sub_category'] = 'سواری'

        self['brand'] = data.css('#breadcrumbs > ul > li:nth-child(6) > a::text').extract_first()

        # extract available information inside the page and map them to item fields
        details_table = data.css('section[id="item-details"]').css('th::text').extract()
        for idx,val in enumerate(details_table):
            try:
                self[attribute_map_table[val]] = data.css('section[id="item-details"]').xpath('.//td//text()').extract()[idx]
            except:
                continue

        extract_model_brand(self, self['brand'] + ' ' + self['model'])
        
        """if self['consumption'] is not None:
            logging.info("================================================================================")
            logging.info(self['consumption'])
            logging.info("================================================================================")
            self['consumption'] = ''.join(re.findall(r'\d+', self['consumption']))"""


class SheypoorItemClassic(SheypoorItemVehicle):
    def extract(self, data):
        super().extract(data)
        self['category'] = 'خودرو'
        self['sub_category'] = 'کلاسیک'


class SheypoorItemMotorcycle(SheypoorItemVehicle, SheypoorItemBase):
    engine_cap = scrapy.Field()         # motorcycle
    motorcycle_type = scrapy.Field()    # motorcycle
    def extract(self, data):
        super().extract(data)
        self['engine_cap'] = 'not_defined'
        self['motorcycle_type'] = 'not_defined'

        self['category'] = 'موتورسیکلت و لوازم جانبی'
        self['sub_category'] = 'not_defined'
        
        # extract available information inside the page and map them to item fields
        details_table = data.css('section[id="item-details"]').css('th::text').extract()
        for idx,val in enumerate(details_table):
            try:
                self[attribute_map_table[val]] = data.css('section[id="item-details"]').xpath('.//td//text()').extract()[idx]
            except:
                continue



class SheypoorCarItemHeavy(SheypoorItemVehicle, SheypoorItemBase):
    def extract(self, data):
        super().extract(data)
        self['category'] = 'خودرو'
        self['sub_category'] = 'سنگین و نیمه سنگین'
        try:
            self['brand'] = data.xpath("#breadcrumbs > ul > li:nth-child(6) > a::text").css('a::text').extract_first()
        except:
            self['brand'] = 'not_defined'
        self['model'] = 'not_defined'
        

class SheypoorItemCarAccessories(SheypoorItemVehicle, SheypoorItemBase):
    accessory_type = scrapy.Field()     # accessories
    def extract(self, data):
        super().extract(data)
        self['category'] = 'قطعات یدکی و لوازم جانبی خودرو'
        self['sub_category'] = 'not_defined'
        self['accessory_type'] = 'not_defined'
        
        # extract available information inside the page and map them to item fields
        details_table = data.css('section[id="item-details"]').css('th::text').extract()
        for idx,val in enumerate(details_table):
            self[attribute_map_table[val]] = data.css('section[id="item-details"]').xpath('.//td//text()').extract()[idx]
            


class SheypoorItemAgricultural(SheypoorItemVehicle, SheypoorItemBase):
    def extract(self, data):
        super().extract(data)
        self['category'] = 'خودرو'
        self['sub_category'] = 'سنگین و نیمه سنگین'
            


class SheypoorItemRentCar(SheypoorItemVehicle, SheypoorItemBase):
    def extract(self, data):
        super().extract(data)
        self['category'] = 'خودرو'
        self['sub_category'] = 'اجاره‌ای'

