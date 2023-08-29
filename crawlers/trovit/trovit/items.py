# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from trovit.utilities.Normalize import clean_number, remove_extra_character_and_normalize
from trovit.utilities.uses import get_production, get_time_stamp, hash_token, get_persian_year, extract_model_brand
# from googletrans import Translator


class TrovitItem(scrapy.Item):
    token = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    subcategory = scrapy.Field()
    price = scrapy.Field()
    rent = scrapy.Field()
    deposit = scrapy.Field()
    url = scrapy.Field()
    thumbnail = scrapy.Field()
    description = scrapy.Field()
    country = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    time = scrapy.Field()
    source_id = scrapy.Field()
    room = scrapy.Field()
    bathroom = scrapy.Field()
    area = scrapy.Field()
    moneyunit = scrapy.Field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['token'] = 'not_defined'
        self['title'] = 'not_defined'
        self['price'] = 'not_defined'
        self['rent'] = 'not_defined'
        self['deposit'] = 'not_defined'
        self['url'] = 'not_defined'
        self['thumbnail'] = 'not_defined'
        self['description'] = 'not_defined'
        self['country'] = 'not_defined'
        self['province'] = 'not_defined'
        self['city'] = 'not_defined'
        self['category'] = 'not_defined'
        self['subcategory'] = 'not_defined'
        self['time'] = 'not_defined'
        self['source_id'] = 'not_defined'
        self['room'] = 'not_defined'
        self['bathroom'] = 'not_defined'
        self['area'] = 'not_defined'
        self['moneyunit'] = 'not_defined'

    def extract(self, response):
        """
        a method to extract data from response
        this method can be free style implement
        that means you can change arguments for your needs
        """
        self['source_id'] = 10
        self['moneyunit'] = "لیر"
        self['country'] = "ترکیه"
        self['time'] = get_time_stamp()

        item_details = response.xpath('.//descendant::a[@class="rd-link"]')

        self['title'] = item_details.xpath('.//descendant::div[@class="item-title"]/span/text()').get()
        self['description'] = item_details.xpath('.//descendant::div[@class="item-description"]/p/text()').get()
        self['price'] = item_details.xpath('.//descendant::span[@class="actual-price"]/text()').get()
        self['url'] = item_details.xpath('.//@href').get()
        self['token'] = hash_token(self['url'].split('/')[3].split('.')[1], 10)
        thumbnail = response.xpath('.//descendant::img/@src').get()
        self['thumbnail'] = 'https:' + thumbnail if thumbnail is not None else None
        room_count = item_details.xpath('.//descendant::div[@class="item-property item-rooms"]/span/text()').get()
        bathroom_count = item_details.xpath('.//descendant::div[@class="item-property item-baths"]/span/text()').get()
        size_area = item_details.xpath('.//descendant::div[@class="item-property item-size"]/span/text()').get()
        
        # City
        city = response.xpath('.//descendant::span[re:test(@class,"address.*")]/text()').get()
        city = list(map(lambda x: x.strip(), city.split(',')))
        self['province'] = city[-1].replace('bölgesinde', '').strip()
        # city = city[0]
        if len(city) >= 3:
            if not city[-3].isdigit():
                city = city[-3]
            else:
                city = city[-2]
        
        elif len(city) <= 2:
            if not city[-2].isdigit():
                city = city[-2]
            else:
                city = city[-1]

        self['city'] = city.lower()
        
        if room_count:
            self["room"] = room_count
        if bathroom_count :
            self["bathroom"] = bathroom_count
        if size_area :
            self["area"] = size_area