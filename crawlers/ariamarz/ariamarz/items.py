# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from curses.ascii import isdigit
import scrapy

from ariamarz.utilities.uses import hash_token

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

class AriamarzItem(BaseItem,HomeBaseItem):
    def extract(self,response,is_buy,stats):
        token = response.xpath('.//div/@id').get()
        if token :
            token = token.replace('property_','')

        # source_id , token
        self['source_id'] = 17
        if token : self['token'] = hash_token(token , 17)

        # title
        if is_buy : self['title'] = "فروش آپارتمان" 
        else : self['title'] = "اجاره آپارتمان"

        # details
        details = response.xpath('.//descendant::div[@class="col-7"]/ul')

        if is_buy :
            price = details.xpath('.//li[1]/strong/text()').get()
            if price : 
                if price.__contains__('تومان') : price = price.replace('تومان','').strip()

        else :
            rent = details.xpath('.//li[1]/strong/text()').get()
            deposit = details.xpath('.//li[2]/strong/text()').get()

            if rent :
                if rent.__contains__('تومان') : rent = rent.replace('تومان اجاره','').strip()
            
            if deposit :
                if deposit.__contains__('تومان') : deposit = deposit.replace('تومان رهن','').strip()

        desc = details.xpath('.//li[@class="medium-sm-text"]/text()').extract()
        desc = list(map(lambda x : x.strip(), desc))

        # info 
        info = response.xpath('.//descendant::div[@class="col-5"]/ul')

        room = info.xpath('.//li/span[contains(text(),"خواب")]/text()').get()
        if room : room = room.replace("خواب","").strip()

        area = info.xpath('.//li/span[contains(text(),"زیربنا")]/text()').get()
        if area : 
            self['title'] += f" {area.strip()}"
            area = area.replace("متر زیربنا","").strip()

        production = info.xpath('.//li/span[contains(text(),"سال ساخت")]/text()').get()
        if production : production = production.replace("سال ساخت","").strip()

        # thumbnail
        thumbnail = response.xpath('.//button/following-sibling::a/img/@src').get()
    
        # Validation
        if thumbnail :
            if not thumbnail.__contains__("https") : thumbnail = 'not_defined'

        # Storing Data
        if is_buy :
            if price :
                if str(price)[0].isdigit() : self['price'] = price
                else : self['price'] = -1

        else :
            if rent :
                if str(rent)[0].isdigit() : self['rent'] = rent
                else : self['rent'] = -1

            if deposit :
                if str(deposit)[0].isdigit() : self['deposit'] = deposit
                else : self['deposit'] = -1

        if desc :
            if desc : self['description'] = desc

        if room :
          if str(room).isdigit() : self['room'] = room

        if area :
           if str(area).isdigit() : self['area'] = area

        if production :
           if str(production).isdigit() : self['production'] = production

        if thumbnail : self['thumbnail'] = thumbnail

        if token : self['url'] = f'https://www.ariamarz.com/property-profile/{token}'

        # Calculate Statistics Of Broken Fields
        if self['title'] == 'not_defined' or self['title'] == '': stats.specify_the_broken_one('title')
        
        if self['city'] == 'not_defined' or self['city'] == '': stats.specify_the_broken_one('city')
        
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