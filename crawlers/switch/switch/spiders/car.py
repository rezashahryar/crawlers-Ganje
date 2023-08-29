import json
import scrapy

from switch.items import SwitchItem
from switch.statistics import SwitchStats

class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.switch.ir']
    start_urls = ['https://www.switch.ir']
    stats = SwitchStats()

    def parse(self, response):
        for page_index in range(0,5):
            from_data = {
                "sort": 1,
                "filter": {
                    "dynamicsBrandId": None,
                    "minProduceYear": None,
                    "dynamicsModelId": None,
                    "maxProduceYear": None
                },
                "pageNumber": page_index,
                "pageSize": 12
            }
            yield scrapy.Request(url='https://www.switch.ir/api/Expo', callback=self.parse_cars , method="POST" , body=json.dumps(from_data) , headers={'Content-Type': 'application/json'})

    def parse_cars(self,response):
        cars = json.loads(response.body)
        for car in cars:
            car_details = {
                "id" : car["_id"],
                "image" : car['image'],
                "brand" : car['brand'],
                "model" : car['model'],
                "year" : car['year'],
                "price" : car['price'],
                "consumption" : car['workedKM']
            }
            car_url = f"https://www.switch.ir/advertisementDetails/{car['_id']}"
            yield scrapy.Request(url=car_url,callback=self.parse_car,meta={"details":car_details})
            
    def parse_car(self,response):
        details = response.request.meta['details']
        item = SwitchItem()
        item.extract(response,details,self.stats)
        self.stats.item_added()
        yield item
        