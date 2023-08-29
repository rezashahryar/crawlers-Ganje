# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from kilid.utilities.Normalize import clean_number, remove_extra_character_and_normalize

from kilid.utilities.uses import get_production, get_time_stamp, hash_token, get_persian_year, extract_model_brand


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

class KilidItem(BaseItem, HomeBaseItem):    
    """ Kilid Extracotr Item """
    deal_type = scrapy.Field()

    def get_thumbnail(self, data):
        if data is None:
            return "not_defined"
        elif len(data) > 0:
            return data[0]['pictureUrlSmall']
        else:
            return "not_defined"

    def check_features(self, data):
        if data is None:
            return
        for _dict in data:
            if _dict['nameLat'] == 'balcony':
                self['balcony'] = True
            elif _dict['nameLat'] == 'storage':
                self['storeroom'] = True
            elif _dict['nameLat'] == 'elevator':
                self['elevator'] = True

    def set_category(self, use_type, estate_type):
        if 'مسکونی' in use_type:
            self['category'] = f'{"فروش" if self["deal_type"] == "buy" else "اجاره"} مسکونی'
            if 'آپارتمان' in estate_type:
                self['sub_category'] = 'آپارتمان'
            elif 'ویلا' in estate_type or 'پنت هاوس' in estate_type or 'برج' in estate_type:
                self['sub_category'] = 'خانه و ویلا'
            elif 'کلنگی' in estate_type or 'زمین' in estate_type:
                self['sub_category'] = 'زمین و کلنگی'
        if 'اداری' in use_type or 'تجاری' in use_type or 'صنعتی' in use_type:
            self['category'] = f'{"فروش" if self["deal_type"] == "buy" else "اجاره"} اداری و تجاری'
            if 'مغازه' in estate_type:
                self['sub_category'] = 'مغازه و غرفه'
            elif  'مستغلات' in estate_type or  'باغ' in estate_type or 'کارخانه' in estate_type or 'کارگاه' in estate_type \
                or 'انبار' in estate_type or 'سوله' in estate_type or 'کشاورزی' in estate_type:
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'
            elif 'اداری' in estate_type or 'مطب' in estate_type or 'کار' in estate_type:
                self['sub_category'] = 'دفتر کار اتاق اداری و مطب'

    def extract(self, response):
        self['url'] = self['url'] = f"https://kilid.com/{self['deal_type']}/detail/{response['id']}"
        self['source_id'] = 4
        self['time'] = get_time_stamp()
        self['token'] = hash_token(response['id'], 4)
        self['title'] = response['title']        
        self['city'] = response['location']['city']['name'] or "not_defined"
        self['neighbourhood'] = response['location']['sector']['name'] or "not_defined"
        self['production'] = get_production(response['age'])
        self['room'] = int(response['noBeds'] or -1)
        self['area'] = int(response['floorArea'] or -1)
        self['price'] = int(response['price'] or -1)
        self['deposit'] = int(response['deposit'] or -1)
        self['rent'] = int(response['rent'] or -1)
        self['description'] = response['description'] or "not_defined"
        self['thumbnail'] = self.get_thumbnail(response['pictures'])
        self['latitude'] = float(response['location']['latitude'] or -1)
        self['longitude'] = float(response['location']['longitude'] or -1)
        self['parking'] = response['noParkings'] is not None

        self.check_features(response['features'])
        self.set_category(response['landuseType'], response['propertyType'])

        # Calculate Statistics Of Broken Fields
        # if self['title'] == 'not_defined' or self['title'] == '': stats.specify_the_broken_one('title')
        
        # if self['city'] == 'not_defined' or self['city'] == '': stats.specify_the_broken_one('city')
        
        # if self['thumbnail'] == 'not_defined' or self['thumbnail'] == '': stats.specify_the_broken_one('thumbnail')
        
        # if self['url'] == 'not_defined' or self['url'] == '': stats.specify_the_broken_one('url')
            
        # if self['production'] == -1 : stats.specify_the_broken_one('production')

        # if self['token'] == -1 : stats.specify_the_broken_one('token')    
        
        # if self['room'] == -1 : stats.specify_the_broken_one('room')    
            
        # if self['area'] == -1 : stats.specify_the_broken_one('area')    

        # if self['price'] == -1: stats.specify_the_broken_one('price')  
        
        # if self['deposit'] == -1: stats.specify_the_broken_one('deposit')

        # if self['rent'] == -1: stats.specify_the_broken_one('rent')
        
        # Broken Items Stats
        # stats.calculate_the_broken_stats()