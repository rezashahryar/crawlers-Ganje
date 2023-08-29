from sheypoor.items.items import BaseItem, HomeBaseItem, CarBaseItem, RecruitmentBaseItem
from sheypoor.utilities.uses import hash_token, get_time_stamp, get_production
from sheypoor.utilities.Normalize import clean_number
from sheypoor.utilities.db_work import get_city_slug


class SheypoorBaseItem(BaseItem):

    def extract(self, data):
        self['url'] = f"https://www.sheypoor.com/{data.css('#item-details > p.description::attr(data-reveal-description)').extract_first()}"
        self['token'] = hash_token(data.css('#item-details > p.description::attr(data-reveal-description)').extract_first(), 2)
        self['source_id'] = 2
        self['time'] = get_time_stamp()
        try:
            self['title'] = data.css('h1::text').extract_first().strip()
        except:
            pass
        self['province'] = data.css('#breadcrumb > ul > li:nth-child(2) > a::text').extract_first().strip().replace('استان', '').replace('‌ ', '').strip()
        self['city'] = data.css('#breadcrumb > ul > li:nth-child(3) > a::text').extract_first().strip().replace('‌',' ').strip()
        self['city_slug'] = get_city_slug(self['province'], self['city'])[2]
        self['neighbourhood'] = 'not_defined'
        self['description'] = ''.join([item for item in data.css('#item-details > p.description::text').extract()])
        self['thumbnail'] = data.css('div[class="swiper-slide swiper-zoom-container"] img::attr(src)').extract_first()
        try:
            self['price'] = data.css("#item-details > p.text-left > span.clearfix.pull-left.text-right"
                                     " > span > strong::text").extract_first().replace(',', '')
        except:
            pass


class HomeItem(HomeBaseItem, SheypoorBaseItem):

    def get_production(self, data):
        if data == 'نوساز':
            return get_production(0)
        elif data == '۲۰ سال به بالا':
            return get_production(23)
        elif '-' in data:
            return {
                        "نوساز": get_production(0),
                        "۲-۵ سال": get_production(3),
                        "2-5 سال": get_production(3),
                        "۵-۱۰ سال": get_production(7),
                        "5-10 سال": get_production(7),
                        "۱۰-۱۵ سال": get_production(12),
                        "10-15 سال": get_production(12),
                        "۱۵-۲۰ سال": get_production(17),
                        "15-20 سال": get_production(17),
                        "۲۰ سال به بالا": get_production(23),
                    }.get(data, -1)
        elif 'سال' in data:
            return get_production(int(data.replace('سال', '').strip()))
        
        return None

    def parse_category(self, category, sub_category, title=None):
        if 'رهن و اجاره' in category and 'خانه و آپارتمان' in category:
            self['category'] = 'اجاره مسکونی'
            if 'آپارتمان' in sub_category:
                self['sub_category'] = 'آپارتمان'
            elif 'خانه' in sub_category:
                self['sub_category'] = 'خانه و ویلا'
            elif 'ویلا' in sub_category:
                self['sub_category'] = 'خانه و ویلا'

        elif 'خرید و فروش' in category and 'خانه و آپارتمان' in category:
            self['category'] = 'فروش مسکونی'
            if 'آپارتمان' in sub_category:
                self['sub_category'] = 'آپارتمان'
            elif 'خانه و کلنگی' in sub_category:
                self['sub_category'] = 'زمین و کلنگی'
            elif 'ویلا' in sub_category:
                self['sub_category'] = 'خانه و ویلا'

        elif 'رهن و اجاره' in category and 'اداری و تجاری' in category:
            self['category'] = 'اجاره اداری و تجاری'
            if 'اداری' in sub_category:
                self['sub_category'] = 'دفتر کار اتاق اداری و مطب'
            elif 'مغازه' in sub_category or 'تجاری' in sub_category:
                self['sub_category'] = 'مغازه و غرفه'
            elif 'صنعتی' in sub_category:
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'
            elif 'دامداری' in sub_category or 'کشاورزی' in sub_category:
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'

        elif 'خرید و فروش' in category and 'اداری و تجاری' in category:
            self['category'] = 'فروش اداری و تجاری'
            if 'اداری' in sub_category:
                self['sub_category'] = 'دفتر کار اتاق اداری و مطب'
            elif 'مغازه' in sub_category or 'تجاری' in sub_category:
                self['sub_category'] = 'مغازه و غرفه'
            elif 'صنعتی' in sub_category:
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'
            elif 'دامداری' in sub_category or 'کشاورزی' in sub_category:
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'
                
        elif 'کوتاه مدت' in category:
            self['category'] = 'اجاره کوتاه مدت'
            if 'سوئیت' in title or 'آپارتمان' in title or 'سوييت' in title or 'سویئت' or 'اپارتمان' in title:
                self['sub_category'] = 'آپارتمان و سوئیت'
            elif 'ویلا' in title or 'خانه' in title or 'باغ' in title:
                self['sub_category'] = 'ویلا و باغ'

        elif 'زمین و باغ' in category:
            self['category'] = 'زمین کلنگی و باغ'
            if 'مسکونی' in sub_category:
                self['category'] = 'فروش مسکونی'
                self['sub_category'] = 'زمین و کلنگی'
            elif 'صنعتی' in sub_category:
                self['category'] = 'فروش اداری و تجاری'
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'
            elif 'اداری و تجاری' in sub_category:
                self['category'] = 'فروش اداری و تجاری'
                self['sub_category'] = 'دفتر کار اتاق اداری و مطب'
            elif 'کشاورزی' in sub_category:
                self['category'] = 'فروش اداری و تجاری'
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'

    def parse_category_non_sub(self, category, title=None):
        if 'کوتاه مدت' in category:
            self['category'] = 'اجاره کوتاه مدت'
            if 'سوئیت' in title or 'آپارتمان' in title or 'سوييت' in title or 'سویئت' or 'اپارتمان' in title:
                self['sub_category'] = 'آپارتمان و سوئیت'
            elif 'ویلا' in title or 'خانه' in title or 'باغ' in title:
                self['sub_category'] = 'ویلا و باغ'
        elif 'خرید' in category:
                if 'ویلا' in category:
                    self['category'] = 'فروش مسکونی'
                    self['sub_category'] = 'خانه و ویلا'
                elif 'خانه' in category:
                    self['category'] = 'فروش مسکونی'
                    self['sub_category'] = 'آپارتمان'
                elif 'اداری' in category or 'تجاری' in category:
                    self['category'] = 'فروش اداری و تجاری'
                    self['sub_category'] = 'دفتر کار اتاق اداری و مطب'
        elif 'اجاره' in category:
            if 'خانه' in category:
                self['category'] = 'اجاره مسکونی'
                self['sub_category'] = 'آپارتمان'
            elif 'اداری' in category or 'تجاری' in category:
                self['category'] = 'اجاره اداری و تجاری'
                self['sub_category'] = 'دفتر کار اتاق اداری و مطب'
        elif 'زمین و باغ' in category:
            self['category'] = 'زمین کلنگی و باغ'
            if 'مسکونی' in title:
                self['category'] = 'فروش مسکونی'
                self['sub_category'] = 'زمین و کلنگی'
            elif 'صنعتی' in title:
                self['category'] = 'فروش اداری و تجاری'
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'
            elif 'اداری و تجاری' in title:
                self['category'] = 'فروش اداری و تجاری'
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'
            elif 'کشاورزی' in title:
                self['category'] = 'فروش اداری و تجاری'
                self['sub_category'] = 'صنعتی کشاورزی و تجاری'

    def extract(self, data):
        SheypoorBaseItem.extract(self, data)
        flag_home_type = False
        adtype = data.css('#breadcrumbs > ul > li:nth-child(5) > a::text').extract_first()

        try:
            self['advertiser'] = 'شخصی' if 'کاربر شیپور' in data.xpath('//*[@id="item-seller-details"]').extract()[0] else 'مشاور املاک'
        except:
            self['advertiser'] = None
        self['description'] = ''.join([item for item in data.css('#item-details > p.description::text').extract()])
        for i in data.css('#item-details > table.key-val'):
            for j in i.css('table > tr'):
                tmp = j.css('th::text').extract_first()
                if tmp == 'نوع ملک':
                    flag_home_type = True
                    try:
                        categorytmp = j.css('td::text').extract_first().strip()
                        self.parse_category(adtype, categorytmp)
                    except:
                        self['sub_category'] = 'خانه و ویلا'
                        if 'خرید' in adtype or 'فروش' in adtype:
                            self['category'] = 'فروش مسکونی'
                        elif 'رهن' in adtype or 'اجاره' in adtype:
                            self['category'] = 'اجاره مسکونی'
                elif tmp == 'نوع کاربری':
                    flag_home_type = True
                    try:
                        categorytmp = j.css('td::text').extract_first().strip()
                        self['sub_category'] = categorytmp
                        self.parse_category(adtype, categorytmp)
                    except:
                        self.parse_category(adtype, 'مسکونی')
                        # self['sub_category'] = 'مسکونی'
                elif tmp == 'سن بنا':
                    producttmp = j.css('td::text').extract_first().strip()
                    try:
                        self['production'] = self.get_production(producttmp)
                    except:
                        pass

                elif tmp == 'پارکینگ':
                    try:
                        self['parking'] = True
                    except:
                        self['parking'] = None
                elif tmp == 'انباری':
                    try:
                        self['storeroom'] = True
                    except:
                        self['storeroom'] = None
                elif tmp == 'آسانسور':
                    try:
                        self['elevator'] = True
                    except:
                        self['elevator'] = None
                elif tmp == 'تعداد اتاق':
                    try:
                        nRoom = j.css('td::text').extract_first().strip()
                        if nRoom == 'بدون اتاق':
                            self['room'] = 0
                        elif nRoom == '۵ به بالا':
                            self['room'] = 5
                        else:
                            self['room'] = int(nRoom)
                    except:
                        self['room'] = None
                elif tmp == 'متراژ':
                    try:
                        self['area'] = int(j.css('td::text').extract_first().strip())
                    except:
                        self['area'] = None
                elif tmp == 'رهن':
                    try:
                        self['deposit'] = int(
                            j.css('td::text').extract_first().replace(' تومان', '').strip().replace(',', ''))
                    except:
                        self['deposit'] = None
                elif tmp == 'اجاره':
                    try:
                        self['rent'] = int(
                            j.css('td::text').extract_first().replace(' تومان', '').strip().replace(',', ''))
                    except:
                        self['rent'] = None
                elif tmp == 'قابلیت تبدیل مبلغ رهن و اجاره':
                    self['swap_deposit_rent'] = True
        if not flag_home_type:
            adtype = data.css('#breadcrumbs > ul > li:nth-child(5) > a::text').extract_first()
            self.parse_category_non_sub(adtype, self['title'])
        self['thumbnail'] = data.css('div[class="swiper-slide swiper-zoom-container"] img::attr(src)').extract_first()


class CarItem(CarBaseItem, SheypoorBaseItem):

    def clean_category(self):
        if 'خودرو' == self['category']:
            self['sub_category'] = 'سواری'

        elif 'موتور سیکلت' == self['category']:
            self['category'] = 'موتورسیکلت و لوازم جانبی'
            self['brand'] = 'not_defined'
            self['model'] = 'not_defined'

        elif 'خودرو کلاسیک' == self['category']:
            self['category'] = 'خودرو'
            self['sub_category'] = 'کلاسیک'
            self['brand'] = 'not_defined'
            self['model'] = 'not_defined'

        elif 'سنگین' in self['category']:
            self['category'] = 'خودرو'
            self['sub_category'] = 'سنگین و نیمه سنگین'
            self['brand'] = 'not_defined'
            self['model'] = 'not_defined'

        elif 'کشاورزی و عمرانی' == self['category']:
            self['category'] = 'خودرو'
            self['sub_category'] = 'سنگین و نیمه سنگین'
            self['brand'] = 'not_defined'
            self['model'] = 'not_defined'

        elif 'لوازم و قطعات وسایل نقلیه' == self['category']:
            self['category'] = 'قطعات یدکی و لوازم جانبی خودرو'
            self['brand'] = 'not_defined'
            self['model'] = 'not_defined'

        elif 'اجاره خودرو' == self['category']:
            self['category'] = 'خودرو'
            self['sub_category'] = 'اجاره‌ای'
            self['brand'] = 'not_defined'
            self['model'] = 'not_defined'

        else:
            self['category'] = 'سایر وسایل نقلیه'
            self['brand'] = 'not_defined'
            self['model'] = 'not_defined'

    def extract_attributes(self, attribute_list):
        for attribute in attribute_list:
            if attribute.get('attributeLocalyticsKey') == 'model':
                self['model'] = attribute.get('attributeValue')

            if attribute.get('attributeLocalyticsKey') == 'bodyType':
                self['chassis_type'] = attribute.get('attributeValue')

            if attribute.get('attributeLocalyticsKey') == 'productionYear':
                self['production'] = clean_number(attribute.get('attributeValue'))

            if attribute.get('attributeLocalyticsKey') == 'km':
                self['consumption'] = clean_number(attribute.get('attributeValue'))

            if attribute.get('attributeLocalyticsKey') == 'carColor':
                self['color'] = attribute.get('attributeValue')

            if attribute.get('attributeLocalyticsKey') == 'gearbox':
                self['gear_box'] = attribute.get('attributeValue')

            if attribute.get('attributeLocalyticsKey') == 'carBodyCondition':
                self['body_condition'] = attribute.get('attributeValue')

            if attribute.get('attributeLocalyticsKey') == 'payment_type':
                self['cash_installment'] = attribute.get('attributeValue')

            if attribute.get('attributeLocalyticsKey') == 'fuel':
                self['fuel'] = attribute.get('attributeValue')

    def extract(self, dict_data):
        SheypoorBaseItem.extract(self, dict_data)
        self['brand'] = dict_data['category'].get('c3', 'not_defined') or 'not_defined'
        self.extract_attributes(dict_data['attributes'])
        self['category'] = dict_data['category'].get('c2', 'not_defined') or 'not_defined'
        self.clean_category()


class RecruitmentItem(RecruitmentBaseItem, SheypoorBaseItem):
    def extract(self, dict_data):
        SheypoorBaseItem.extract(self, dict_data)
