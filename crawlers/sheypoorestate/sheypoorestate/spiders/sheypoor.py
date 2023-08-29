import scrapy
import json
import csv


class SheypoorSpider(scrapy.Spider):
    name = 'sheypoor'
    allowed_domains = ['sheypoor.com', 'api.sheypoor.com', 'www.sheypoor.com']
    headers = {
        'User-Agent': 'ganje bot (+https://ganje.ir)'
    }


    # start_urls = ['http://sheypoor.com/']

    def start_requests(self):
        urls = ["https://www.sheypoor.com/shops/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9?p={}".format(i) for i in range(1, 16)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        links = response.xpath('.//descendant::div[re:test(@class,"gkjnQ")]/h2/a/@href').extract()
        links = ['https://www.sheypoor.com/api/v10.0.0/shops/slug/{}/about'.format(link.split('/')[-1]) for link in links]
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_back, headers=self.headers)

    def parse_back(self, response):
        data = json.loads(response.text)
        f = open('sheypoor_estate.csv', 'a')
        f.write(data['meta']['seo']['title'] + ',' + data['data']['attributes']['primaryPhone'] + ',' + data['data']['attributes']['workingTime'] + ',' + data['data']['attributes']["description"] + '\n')
        f.close()
        yield {
            "نام مشاور املاک": data['meta']['seo']['title'],
            "شماره تلفن": data['data']['attributes']['primaryPhone'],
            "ساعت کار": data['data']['attributes']['workingTime'],
            "توضیحات": data['data']['attributes']["description"]
        }

        
