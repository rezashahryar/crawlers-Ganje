import scrapy
import json
from trovit.items import TrovitItem
import re

class TrovitSpider(scrapy.Spider):
    name = 'trovit'
    allowed_domains = ['trovit.com.tr']
    start_urls = ['https://daire.trovit.com.tr']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        f = open('geo_province_turkey.json')
        self.province_geo = json.load(f)
        f.close()
        d = open('geo_province_fa_turkey.json')
        self.province_fa = json.load(d)
        d.close()
        e = open('tr_cities.json')
        self.cities = json.load(e)
        e.close()


    def parse(self, response):
        provinces = response.xpath('//li[@data-test="location"]/a')
        
        for province in provinces:
            name = province.xpath('.//text()').get()
            link = province.xpath('.//@href').get()
            selected_sub = response.xpath('//ul[@class="lh-selector lh-property-deal-type"]/li/span/text()').get()
            yield scrapy.Request(url=link , callback=self.parse_province,meta = {
                "province_name" : name ,
                "selected_sub" : selected_sub if selected_sub else "Ev",
                "selected_category": response.xpath('//ul[@class="lh-selector lh-deal-type"]/li/span/text()').get()
            })
            

        next_sub_category = response.xpath('//ul[@class="lh-selector lh-property-deal-type"]/li/following-sibling::li')
        if next_sub_category :
            category_a = next_sub_category.xpath('.//a')
            category_link = category_a.xpath('.//@href').get()
            if category_link :
               yield scrapy.Request(url=category_link, callback=self.parse)

        # # Sale OR Rent
        next_category = response.xpath('//ul[@class="lh-selector lh-deal-type"]/li/following-sibling::li')
        if next_category :
            categroy_a = next_category.xpath('.//a')
            category_link = categroy_a.xpath('.//@href').get()
            if category_link:
               yield scrapy.Request(url=category_link, callback=self.parse)

    def parse_province(self,response):
        the_alias = response.xpath("//strong[@class='qa-bc-current']/text()").get().lower()
        the_type = 1 # 1 For Home
        
        province_name = response.request.meta["province_name"]
        selected_sub = response.request.meta["selected_sub"]
        selected_category = response.request.meta["selected_category"]
        
        if selected_category == 'Satılık':
            if selected_sub == "Ev" : the_type = 1
            elif selected_sub == "Arazi" : the_type = 10
        elif selected_category == 'Kiralık':
            if selected_sub == "Ev" : the_type = 2

        link = f'https://daire.trovit.com.tr/cod.search_homes/type.{the_type}/what_d.{the_alias}/sug.0/isUserSearch.1/order_by.source_date/date_from.7/geo_id.{self.province_geo[province_name]}/'
        yield scrapy.Request(url = link,callback = self.parse_detail,meta = {
            "province_name" : province_name ,
            "selected_sub" : selected_sub, 
            "selected_category": selected_category})

    def parse_detail(self,response):
        items = response.xpath('//div[@class="snippet-wrapper js-item-wrapper"]')
        province_name = response.request.meta["province_name"]
        selected_sub = response.request.meta["selected_sub"]
        selected_category = response.request.meta["selected_category"]
        is_rent = response.xpath("//h1[contains(text(),'Kiralık')]/text()").get()
        
        cat_sub_detail = {
            "Kiralık" : 'اجاره مسکونی',
            'Satılık' : 'فروش مسکونی',
            'Arazi' : 'زمین',
            'Ev' : 'آپارتمان'
        }

        print(len(items))

        for item in items:
            res = TrovitItem()
            res.extract(item)
            res['province'] = self.province_fa[res['province']]
            if is_rent: 
                res['rent'] = res['price']
                res['price'] = -1
            res['subcategory'] = cat_sub_detail[selected_sub]
            res['category'] = cat_sub_detail[selected_category]
    
            if res['city'] in self.cities.keys():
               res['city'] = self.cities[res['city']]
               res['title'] = self._generate_title(res['category'],res['subcategory'],res['room'],res['area'],res['city'])
               yield res

    def _generate_title(self,category, sub_category,room,area,city):
        """generate standard title for torvit properties titles"""
        category = category.replace('مسکونی','').replace('تجاری','').strip()

        if room == 'not_defined':
            room = ''
        elif room and room != 'not_defined':
            room = int(re.search(r'\d+', room).group())
            room = str(room) + ' خواب '
        
        if area == 'not_defined':
            area = ''
        elif area and area != 'not_defined':
            # area = float(re.search(r'\d+', area).group())
            area =  re.findall(r"[-+]?\d*\.\d+|\d+", area)[0]
            area = str(area) + ' متری '

        return f"{category} {sub_category} {room}{area}در {city}"
                
        # next_page = response.xpath('//a[@data-test="p-next"]/@href').get()

        # if next_page :
        #     yield scrapy.Request(url=next_page,callback = self.parse_province , meta = {
        #         "province_name" : province_name , 
        #         "selected_sub" : selected_sub, 
        #         "selected_category": selected_category})