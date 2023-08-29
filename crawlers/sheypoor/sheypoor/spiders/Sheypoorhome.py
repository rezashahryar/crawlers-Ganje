# -*- coding: utf-8 -*-
import scrapy
import datetime
import json

from sheypoor.items.sheypoor_items import HomeItem, CarItem
from scrapy import signals

from sheypoor.utilities.db_work import get_stop_id, store_stop_id, get_item_count


class SheypoorSpider(scrapy.Spider):
    # handle_httpstatus_list = [400, 200, 300]
    custom_settings = dict(
        DOWNLOADER_MIDDLEWARES={
            #            'cansoCrawler.middlewares.ProxyMiddleware': 350,
            'sheypoor.middlewares.sheypoorSpiderMiddleware': 543,
            #            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
            #           'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
            'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 900,
        },
        #        FAKEUSERAGENT_PROVIDERS = [
        #              'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # this is the first provider we'll try
        #              'scrapy_fake_useragent.providers.FakerProvider',  # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
        #       ],
        DOWNLOAD_DELAY=7,
        RANDOMIZE_DOWNLOAD_DELAY=True,
        CONCURRENT_REQUESTS=1,
        CONCURRENT_REQUESTS_PER_DOMAIN=1,
        #       CONCURRENT_REQUESTS_PER_IP = 1,
    )

    name = 'sheypoor_home'
    allowed_domains = ['sheypoor.com']
    category = ''
    _pages = 1
    sheypoor_page = 1
    request_time = -1
    last_id = None
    first_id = "-1"
    item_count = 0
    start_time = str(
        int(round((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0)).total_seconds(), 4))) + '.0000'

    def __init__(self, category='none', **kwargs):
        self.cat = category
        self.category = category
        self.seed = round((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0)).total_seconds(), 4)
        super().__init__(**kwargs)

    def start_requests(self):
        # self.item_count = get_item_count(self.category, 2)
        yield scrapy.Request(url=self.get_url(), callback=self.parse, headers=self.headers)

    def parse(self, response, page=1):
        ads = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "content", " " ))]')
        self.logger.info(f"length of data:{len(ads)} for page:{page} and time is:{self.request_time}")

        for ad in ads:
            if page > self._pages:
                return None
            try:
                link = ad.css('h2 a::attr(href)').extract()[0]
                yield scrapy.Request(url=link,
                                     callback=self.parse_ad)
            except IndexError:
                # similar ads -small in the bottom of pages
                continue

        if page < self._pages:
            yield response.follow(url=self.get_url(), callback=self.parse, cb_kwargs={"page": page + 1},
                                  headers=self.headers)

    def parse_ad(self, response):
        if self.category == 'home':
            item = HomeItem()
            item.extract(response)
            return item
        if self.category == 'car':
            item = CarItem()
            item.extract(response)
            return item

        # return None

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(SheypoorSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        # store_stop_id('sheypoor', self.category, self.first_id)
        # new_count = get_item_count(self.category, 2)
        # if new_count is not None and self.item_count is not None:
        #     self.logger.info(
        #         f"count of stored items:{new_count - self.item_count} for category:{self.category}")
        pass

    def get_url(self):
        request_time = self.get_request_time()
        category_id = {
            "home": "ایران/املاک",
            "car": "ایران/وسایل-نقلیه",
            "recruitment": "43618"
        }
        if self.sheypoor_page == 1:
            return f"https://www.sheypoor.com/{category_id.get(self.category, '-1-')}"
        else:
            return f"https://www.sheypoor.com/{category_id.get(self.category, '-1-')}?p={self.sheypoor_page}&f={self.start_time}"

    def get_request_time(self):
        if self.request_time == -1 or self.sheypoor_page >= 25:
            self.sheypoor_page = 0
            self.request_time = str(self.start_time)[:15]
        self.sheypoor_page += 1
        return self.request_time

    def get_last_id(self):
        if self.last_id is not None:
            return self.last_id
        url = get_stop_id('sheypoor', self.category)
        if url is None:
            self.last_id = -1
        else:
            self.last_id = url.split('/')[-1]
        return self.last_id

    category_list = [
        "املاک",
        "وسایل نقلیه"
        "ورزش فرهنگ فراغت",
        "لوازم الکترونیکی",
        "استخدام",
        "صنعتی، اداری و تجاری",
        "خدمات و کسب و کار",
        "موبایل، تبلت و لوازم",
        "لوازم خانگی",
        "لوازم شخصی",
    ]

    headers = {
        'User-Agent': 'ganje bot (+https://ganje.ir)'
    }
