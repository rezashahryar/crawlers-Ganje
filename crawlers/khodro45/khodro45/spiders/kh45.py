import scrapy
import json
from khodro45.items import Khodro45CarItem
from khodro45.statistics import Khodro45Stats

class Kh45Spider(scrapy.Spider):
    name = 'kh45'
    allowed_domains = ['khodro45.com']
    start_urls = ['https://khodro45.com/']
    stats = Khodro45Stats()

    def parse(self, response):
        try:
            res = json.loads(response.text)
            cars_details = res["results"] 

            for car in cars_details:
                car_url_data ={
                    'brand_slug' : car['car_properties']['brand']['url_slug'],
                    'model_slug' : car['car_properties']['model']['url_slug'],
                    'city_en' : car['city']['title_en'],
                    'slug' : car['slug'],
                }
                car_url = f"https://khodro45.com/used-car/{car_url_data['brand_slug']}-{car_url_data['model_slug']}/{car_url_data['city_en']}/cla-{car_url_data['slug']}/"
                url = f"https://khodro45.com/api/v1/car_listing/{car['slug']}/"
                yield scrapy.Request(url=url,callback=self.parse_details,meta ={'car_url' : car_url})

        except : None

        for page_index in range(1,6):
            link = f"https://khodro45.com/api/v2/car_listing/?page={page_index}&ordering=-created_time"
            yield scrapy.Request(url=link,callback=self.parse)
        

    def parse_details(self, response):
        item = Khodro45CarItem()
        item.extract(response,self.stats)
        self.stats.item_added()
        yield item