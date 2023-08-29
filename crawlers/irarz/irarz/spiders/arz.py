import scrapy


class ArzSpider(scrapy.Spider):
    name = 'arz'
    allowed_domains = ['irarz.com']
    start_urls = ['https://irarz.com']

    def parse(self, response):
        table = response.xpath('(//div[@class="table-responsive"])[4]/table/tbody/tr')
        pound_price = response.xpath('(//div[@class="card"])[4]//div[@class="text-center"]//span[@id="price_gbp"]/text()').get()
        yield {
            "title" : "پوند انگلیس",
            "price" : pound_price.replace(',','')
        }
        for arz in table:
            arz_title = arz.xpath('.//td[1]/text()').get()
            arz_price = arz.xpath('.//td[1]/following-sibling::td/span/text()').get()

            yield {
                "title" : arz_title,
                "price" : arz_price.replace(',','')
            }