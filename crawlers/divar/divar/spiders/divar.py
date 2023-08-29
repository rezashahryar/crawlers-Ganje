import os
import scrapy
import json

from scrapy import signals
from datetime import datetime
from divar.items.divar_items import HomeItem, CarItem, RecruitmentItem
from divar.utilities.db_work import get_province
from divar.utilities.Normalize import normalize_text


class DivarSpider(scrapy.Spider):
    name = "divar"
    start_urls = [
        'https://api.divar.ir/v8/places/cities'
    ]
    allowed_domains = ['divar.ir']

    def __init__(self, category='', **kwargs):
        self.cat = category
        self.category = category
        prev_timestamp = None
        if self.category == 'home':
            self.category = 'real-estate'
        elif self.category == 'car':
            self.category = 'cars'
        elif self.category == 'recruiment':
            self.category = 'jobs'
        try:
            f = open('previous_time_stamp_' + self.category + '.txt')
            prev_timestamp = int(f.readline().strip())
            f.close()
        except:
            pass
        self.metropolis = [
            'تهران',
            'مشهد',
            'کرج',
            'شیراز',
            'اصفهان',
            'اهواز',
            'تبریز',
            'کرمانشاه',
            'قم',
            'رشت'
        ]
        try:
            f = open('divar_' + self.category + '.txt')
            self.prev_tokens = [token.strip() for token in f.readlines()] if len(f.readlines()) !=0 else []
            f.close()
        except:
            self.prev_tokens = []
        self.current_tokens = []
        self.current_timestamp = int(datetime.now().timestamp() * 10**6)
        self.previous_timestamp = prev_timestamp if prev_timestamp != None else self.current_timestamp - 1500000000 #25 minutes
        super().__init__(**kwargs)

    def parse(self, response):
        city_list = json.loads(response.body.decode('UTF-8'))["cities"]
        for city in city_list:
            self.logger.info("Getting %s city", city['name'])
            code = city['id']  # City code
            req = {"json_schema": {"category": {"value": self.category}}, "last-post-date": self.current_timestamp, "first_post_date": self.previous_timestamp}

            province_city = get_province(city['name'])
            city["name"] = province_city["c"]

            yield scrapy.Request(
                f'https://api.divar.ir/v8/web-search/{code}/{self.category}',
                callback=self.get_page,
                method='POST',
                body=json.dumps(req),
                headers=self.headers,
                cb_kwargs={
                    'city': city,
                    'province': province_city["p"],
                    'category': self.category,
                    'counter': 1
                }
            )

    def get_page(self, response, city, category, counter, province):
        self.logger.info("Getting page {} of {}".format(counter, city["name"]))
        json_response = json.loads(response.body.decode("UTF-8"))
        # Get page details
        for i in range(0, len(json_response['web_widgets']['post_list'])):
            token = json_response['web_widgets']['post_list'][i]['data']['token']
            if token not in self.prev_tokens:
                self.current_tokens.append(token)
                yield scrapy.Request(
                    os.path.join(
                        "https://api.divar.ir/v5/posts/",
                        token
                    ),
                    callback=self.get_page_items,
                    cb_kwargs={'city': city, 'province': province},
                    headers=self.headers
                )
        # Next page
        # if (city["name"] not in self.metropolis and counter <= 1) or (city["name"] in self.metropolis and counter <= 2):
        #     req = {"json_schema": {"category": {"value": category}}, "last-post-date": json_response['last_post_date']}
        #     yield response.follow(
        #         f'https://api.divar.ir/v8/web-search//{city["id"]}/{self.category}',
        #         callback=self.get_page,
        #         method='POST',
        #         body=json.dumps(req),
        #         cb_kwargs={
        #             'city': city,
        #             'category': category,
        #             'counter': counter + 1,
        #             'province': province
        #         },
        #         headers=self.headers
        #     )

    def get_page_items(self, response, city, province):
        self.logger.info("Getting page items")
        json_response = json.loads(response.body.decode("UTF-8"))
        if self.category == 'real-estate':
            item = HomeItem()
        elif self.category == 'cars':
            item = CarItem()
        elif self.category == 'jobs':
            item = RecruitmentItem()
        else:
            return
        item.extract(json_response)
        item['city'] = normalize_text(city["name"])
        item['province'] = province
        return item

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(DivarSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        f = open('previous_time_stamp_' + self.category + '.txt', 'w')
        f.write(str(self.current_timestamp))
        f.close()

        g = open('divar_' + self.category + '.txt', 'w')
        for token in self.current_tokens:
            g.write(str(token) + '\n')
        g.close()


    headers = {
        'Accept': 'application/json',
        'User-Agent': 'ganje bot (+https://ganje.ir)'
    }
