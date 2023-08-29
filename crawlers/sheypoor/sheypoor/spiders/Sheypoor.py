# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy import Spider
from sheypoor.items.SheypoorItems import SheypoorItemCar, SheypoorCarItemHeavy

class SheypoorSpider(Spider):
    name = "sheypoor_car"
    allowed_domains = ["sheypoor.com"]
    start_urls = ["https://www.sheypoor.com/"]
    category_urls = [
        "https://www.sheypoor.com/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86/%D9%88%D8%B3%D8%A7%DB%8C%D9%84-%D9%86%D9%82%D9%84%DB%8C%D9%87", # cars url
        "https://www.sheypoor.com/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9", #estate url
        "https://www.sheypoor.com/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85"  # recruitments url
    ]  
    _pages = 1
    sheypoor_page = 1
    request_time = -1
    last_id = None
    first_id = "-1"
    item_count = 0
    start_time = str(int(round((datetime.datetime.utcnow() - datetime.datetime(1970,1,1,0,0,0)).total_seconds(), 4))) + '.0000'
    
    headers = {
        'User-Agent': 'ganje bot (+https://ganje.ir)'
    }

    custom_settings = dict(
        DOWNLOADER_MIDDLEWARES = {
#            'cansoCrawler.middlewares.ProxyMiddleware': 350,
            'sheypoor.middlewares.sheypoorSpiderMiddleware': 543,
#            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
#            'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
            'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 900,
        },
#        FAKEUSERAGENT_PROVIDERS = [
#              'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # this is the first provider we'll try
#              'scrapy_fake_useragent.providers.FakerProvider',  # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
#       ],
    )


    def __init__(self, category='car', **kwargs):
        if category == "car":
            self.category = "car"
            self.start_urls = [self.category_urls[0]]
        elif category == "estate":
            self.category = "home"
            self.start_urls = [self.category_urls[1]]
        elif category == "recruitment":
            self.category = "recruitment"
            self.start_urls = [self.category_urls[2]]
        else:
            self.start_urls = ["None"]

    def start_requests(self):
        # self.item_count = get_item_count(self.category, 2)
        yield scrapy.Request(url=self.get_url(), callback=self.parse, headers=self.headers)

    # parse_start_url
    def parse(self, response, page=1):
        ads = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "content", " " ))]')
        self.logger.info(f"length of data:{len(ads)} for page:{page} and time is:{self.request_time}")

        for ad in ads:
            if page > self._pages:
                return None
            try:
                link = ad.css('h2 a::attr(href)').extract()[0]
                yield scrapy.Request(url=link, 
                                 callback=self.parse_car_details)
            except IndexError:
                # similar ads -small in the bottom of pages
                continue

        if page < self._pages:
            yield response.follow(url=self.get_url(), callback=self.parse, cb_kwargs={"page": page + 1},
                                  headers=self.headers)

    def parse_car_details(self, response):
        cat_tree = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "after", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]//a').extract()[0]
        self.logger.info("\nIncoming: " + cat_tree + "\n")
        #if "لوازم و قطعات" in cat_tree:
            #item = SheypoorItemAccessories()
        if "خودرو" in cat_tree:
            item = SheypoorItemCar()
        elif "سنگین" in cat_tree:
            item = SheypoorCarItemHeavy()
        #elif "کشاورزی" in cat_tree:
            #item = SheypoorCarItemAgricultural()
        #elif "موتور" in cat_tree:
            #item = SheypoorCarItemMotorcycle()
        else: 
            self.logger.error("Unknow Car category")
            return
        
        item.extract(response)
        return item

    def get_url(self):
        request_time = self.get_request_time()
        category_id = {
            "home": "ایران/املاک",
            "car": "ایران/وسایل-نقلیه",
            "recruitment": "43618"
        }
        if self.sheypoor_page == 1:
            return f"https://www.sheypoor.com/{category_id.get(self.category,'-1-')}"
        else:
            return f"https://www.sheypoor.com/{category_id.get(self.category,'-1-')}?p={self.sheypoor_page}&f={self.start_time}"

    def get_request_time(self):
        if self.request_time == -1 or self.sheypoor_page >= 25:
            self.sheypoor_page = 0
            self.request_time = str(self.start_time)[:15]
        self.sheypoor_page += 1
        return self.request_time
        
