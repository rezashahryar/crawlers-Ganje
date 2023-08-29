import json
import scrapy

from kilid.items import KilidItem
# from kilid.statistics import KilidStats
from kilid.utilities.db_work import get_province

class HomeSpider(scrapy.Spider):
    name = 'kilid'
    allowed_domains = ['kilid.com']
    start_urls = ['https://kilid.com/']
    # stats = KilidStats()
    tokens = []

    def parse(self, response):
        cities_code = [{'code': 272905, 'city': 'tehran'}, 
                       {'code': 273014, 'city': 'karaj'}, 
                       {'code': 272903, 'city': 'isfahan'}, 
                       {'code': 272896, 'city': 'shiraz'},
                       {'code': 272895, 'city': 'mashhad'}]
        types = ['buy-residential' , 'buy-commercial' , 'rent-residential' , 'rent-commercial']
        for type in types:
            land_typeId = 3001
            list_typeId = 1
            is_rent = False
            if type.__contains__('rent') :
                is_rent = True
                list_typeId = 2
            if type.__contains__('commercial'):
                land_typeId = 3005
            for city_code in cities_code:
                for page_index in range(0,3):
                    url = f'https://kilid.com/{type}/{city_code["city"]}?landUseTypeIds={land_typeId}&listingTypeId={list_typeId}&location={city_code["code"]}&page={page_index}&sort=DATE_DESC'
                    yield scrapy.Request(url=url, callback=self.parse_homes, headers=self.headers, meta = {"is_rent" : is_rent}) 

    def parse_homes(self,response):
        homes = response.xpath('//div[@class="main"]')
        is_rent = response.request.meta['is_rent']
        for home in homes :
            try:
                href = home.xpath('.//parent::a/@href').get()
                token = href.split('/')[3]
                url = f'https://server.kilid.com/api/listing/{token}/single/v2.0'
                yield scrapy.Request(url = url , callback=self.parse_home ,headers=self.headers_json, meta = {"is_rent" : is_rent})
            except : None

    def parse_home(self, response):
        home = json.loads(response.body)
        is_rent = response.request.meta['is_rent']
        item = KilidItem()
        item['deal_type'] = 'rent' if is_rent else 'buy'
        item.extract(response=home)
        province_city = get_province(home['location']['city']['name'])
        item['province'] = province_city["p"]
        item["city"] = province_city["c"]
        # self.stats.item_added()
        yield item

    headers_json = {
        'Accept': 'application/json',
        'User-Agent': 'ganje bot (+https://ganje.ir)'
    }

    headers = {
        'User-Agent': 'ganje bot (+https://ganje.ir)'
    }