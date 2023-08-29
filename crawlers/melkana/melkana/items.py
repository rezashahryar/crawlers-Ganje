# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from melkana.utilities.Normalize import clean_number, remove_extra_character_and_normalize
from melkana.utilities.uses import get_production, get_time_stamp, hash_token, get_persian_year, extract_model_brand

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
    vector = scrapy.Field()

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
        self['vector'] = 'not_defined'


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

class MelkanaItem(BaseItem, HomeBaseItem):
    def check_features(self, features):
        if 'کولر' in features:
            self['cooler'] = True
        if 'پارکینگ' in features:
            self['parking'] = True
        if 'آسانسور' in features:
            self['elevator'] = True
        if 'انباری' in features:
            self['storeroom'] = True
        if 'بالکن' in features:
            self['balcony'] = True
        if 'پکیج' in features:
            self['package'] = True

    def extract(self, dict_data):
        details = dict_data['details']
        self['token'] = hash_token(details['code'], 6)
        self['url'] = f"https://www.melkana.com/estate/detail/{details['code']}"
        self['source_id'] = 6
        self['time'] = get_time_stamp()
        self['area'] = int(details['foundation'] or -1)
        self['title'] = self['category'] + " " + (f"{self['area']} متر" if self['area'] != -1 else "")
        self['province'] = 'تهران'
        self['city'] = 'تهران'
        self['production'] = -1 if details['estate_age'] is None else get_production(details['estate_age'])
        self['room'] = int(details['rooms'] or -1)
        if details['deal_type'] == 'فروش':
            self['price'] = clean_number(details['price'])
        else:
            self['deposit'] = clean_number(details['price'])
        self['rent'] = clean_number(details['price_rent'])
        self['description'] = details['description'] or details['features'] or 'not_defined'
        self['thumbnail'] = details['image_360'] or 'not_defined'
        self['latitude'] = dict_data['myLatLng']['lat']
        self['longitude'] = dict_data['myLatLng']['lng']
        self['estate_floor'] = 0 if details['estate_floor'] == 'همکف' else details['estate_floor']
        self['estate_direction'] = details['estate_direction']
        self['kitchen'] = details['kitchen']
        self['floor_covering'] = details['floor_covering']
        self.check_features(details['features'])