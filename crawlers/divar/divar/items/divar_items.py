from divar.items.items import BaseItem, HomeBaseItem, CarBaseItem, RecruitmentBaseItem
from divar.utilities.Normalize import remove_extra_character_and_normalize
from divar.utilities.Normalize import convert_alphabetic_number_to_integer, clean_number
from divar.utilities.uses import hash_token, get_time_stamp, extract_model_brand
from scrapy.utils.log import logger
from unidecode import unidecode

class DivarBaseItem(BaseItem):
    def extract(self, dict_data):
        self['time'] = get_time_stamp()
        self['title'] = dict_data['data']['share']['title']
        self['description'] = dict_data['widgets']['description']
        self['token'] = hash_token(dict_data['token'], 1)
        self['source_id'] = 1
        self['url'] = dict_data['data']['url']
        image_list = dict_data['widgets']['web_images']
        self['thumbnail'] = (image_list[0][0]['src'].replace(
            'webp', 'jpg')) if len(image_list) > 0 else 'not_defined'
        self['latitude'] = float(
            dict_data['widgets']['location'].get('latitude', -1))
        self['longitude'] = float(
            dict_data['widgets']['location'].get('longitude', -1))
        self['neighbourhood'] = dict_data['widgets']['header']['place']


class CarItem(CarBaseItem, DivarBaseItem):

    def fetch_data(self, i):
        if 'برند' in i['title']:
            if 'بنزین' in i['title']:
                self['fuel'] = 'بنزین'
            elif 'دوگانه' in i['title']:
                self['fuel'] = 'دوگانه سوز'
            elif 'گازو' in i['title']:
                self['fuel'] = 'گازوئیل'
            elif 'هیبرید' in i['title']:
                self['fuel'] = 'هیبریدی'
            elif 'cng' in i['title'].lower():
                self['fuel'] = 'دوگانه سوز'
            else:
                self['fuel'] = 'بنزین'
            if 'سایر' not in i['value']:
                extract_model_brand(self, i['value'])
                self.brand_model_checker()
        elif 'کارکرد' in i['title']:
            try:
                self['consumption'] = clean_number(i['value'])
            except:
                self['consumption'] = -1
        elif 'سال' in i['title']:
            try:
                self['production'] = clean_number(i['value'])
            except:
                self['production'] = -1
        elif 'رنگ' in i['title']:
            self['color'] = i['value']
        elif 'قیمت' in i['title']:
            self['price'] = i['value']
        elif i['title'] == 'نوع آگهی':
            pass
        elif i['title'] == 'مایلم معاوضه کنم':
            self['swap'] = True if i['value'] == 'هستم' else False
        elif 'گیربکس' in i['title']:
            self['gear_box'] = i['value']
        elif 'وضعیت بدنه' in i['title']:
            self['body_condition'] = i['value']

        elif i['title'] == 'نحوه فروش':
            if 'نقدی' in i['value']:
                self['cash_installment'] = 'نقدی'
            elif 'قسطی' in i['value']:
                self['cash_installment'] = 'قسطی'
            if 'معاوضه' in i['value']:
                self['swap'] = True

    def extract(self, data):
        DivarBaseItem.extract(self, data)
        list_data = data['widgets']['list_data']
        for i in list_data:
            if 'items' in i:
                for item in i['items']:
                    self.fetch_data(item)
            else:
                self.fetch_data(i)

        subcategory = data['data']['category']['title']
        if subcategory == 'سنگین':
            self['sub_category'] = 'سنگین و نیمه سنگین'
            self['category'] = 'خودرو'
        elif subcategory == 'خودرو':
            self['sub_category'] = 'وسایل نقلیه'
            self['category'] = 'خودرو'
        elif 'سواری' in subcategory or 'وانت' in subcategory:
            self['sub_category'] = 'سواری'
            self['category'] = 'خودرو'
        elif subcategory =='سواری' or subcategory == 'اجاره‌ای' or subcategory == 'کلاسیک':
            self['category'] = 'خودرو'
            self['sub_category'] = subcategory
        elif subcategory == 'قطعات یدکی و لوازم جانبی خودرو':
            self['category'] = 'قطعات یدکی و لوازم جانبی خودرو'
        elif subcategory == 'موتورسیکلت و لوازم جانبی':
            self['category'] = 'موتورسیکلت و لوازم جانبی'
        elif subcategory == 'قایق و لوازم جانبی':
            self['category'] = 'قایق و لوازم جانبی'
        elif subcategory == 'وسایل نقلیه':
            self['category'] = 'سایر وسایل نقلیه'
            
    def brand_model_checker(self):
        def null_checker(v):
            return str(v) != '-1' and v != 'not_defined' and v != 'notdefined' and v != 'not defined' and str(v) != '-1.0' and v != 'not-defined' \
                and v != 'NOTDEFINED' and v != 'NOT DEFINED' and len(str(v)) != 0 and v is not None

        error_dict = dict()
        if not null_checker(self['brand']):
            error_dict['brand'] = 'this item is null'

        if not null_checker(self['model']):
            error_dict['model'] = 'this item is null'

        if len(error_dict) != 0:
            error_dict['url'] = self['url']
            error_dict['title'] = self['title']
            logger.critical(str(error_dict))


class HomeItem(HomeBaseItem, DivarBaseItem):

    def fetch_info_data(self, i):
        if 'ساخت' in i['title']:
            try:
                self['production'] = clean_number(i['value'])
            except:
                self['production'] = -1
        elif 'اتاق' in i['title']:
            self['room'] = i['value']
        elif i['title'] == 'متراژ':
            try:
                self['area'] = clean_number(i['value'])
            except:
                self['area'] = -1
        elif i['title'] == 'متراژ زمین':
            try:
                self['area'] = clean_number(i['value'])
            except:
                self['area'] = -1
        elif 'قیمت' in i['title'] and ('متر' not in i['title']):
                self['price'] = i['value']
        elif ('ودیعه' in i['title'] or 'رهن' in i['title']) and ('اجارهٔ' not in  i['title']) and ('اجاره' not in  i['title']):
                self['deposit'] = i['value']
        elif ('اجارهٔ' in  i['title'] or 'اجاره' in  i['title']) and ('ودیعه' not in i['title']):
            try:
                self['rent'] = i['value']
            except:
                if ['value'] == 'مجانی':
                    self['rent'] = 0
                elif ['value'] == 'توافقی':
                    self['rent'] = -1
        elif i['title'] == 'نوع آگهی':
            adtype = i['value']
            if adtype == 'ارائه':
                pass
            elif adtype == 'فروشی':
                pass
        elif i['title'] == 'آگهی‌دهنده':
            self['advertiser'] = i['value']
        elif 'املاک' in i['title']:
            self['advertiser'] = 'مشاور املاک'
        elif i['title'] == 'سند اداری':
            self['administrative_document'] = False if i['value'] == 'نیست' else True
        elif i['title'] == 'مایلم معاوضه کنم':
            self['swap'] = True if i['value'] == 'هستم' else False
        elif 'ودیعه' in i['title'] and 'اجاره' in i['title']:
            try:
                self['swap_deposit_rent'] = 'غیر' not in i['value']
            except:
                pass

    def fetch_feature_data(self, feature):
        if 'آسانسور' in feature:
            self['elevator'] = 'ندارد' not in feature

        elif 'پارکینگ' in feature:
            self['parking'] = 'ندارد' not in feature

        elif 'انباری' in feature:
            self['storeroom'] = 'ندارد' not in feature

        elif 'بالکن' in feature:
            self['balcony'] = 'ندارد' not in feature

    def fetch_category(self, categories):
        for item in categories:
            if item['parent_slug'] == 'real-estate':
                self['category'] = item['title']
            if item['parent_slug'] != 'real-estate' and item['parent_slug'] is not None and item['parent_slug'] != 'root':
                self['sub_category'] = item['title']

    def extract(self, data):
        DivarBaseItem.extract(self, data)
        for i in data['widgets']['list_data']:
            if 'items' in i and i['format'] == 'group_info_row':
                for item in i['items']:
                    self.fetch_info_data(item)
            elif 'items' in i and i['format'] == 'group_feature_row':
                for item in i['items']:
                    self.fetch_feature_data(item['title'])
            else:
                self.fetch_info_data(i)

        self.fetch_category(data['widgets']['breadcrumb']['categories'])

        category = data['data']['category']['slug']
        if category == 'apartment-rent' or category == 'house-villa-rent':
            self['category'] = 'اجاره مسکونی'
        elif category == 'house-villa-sell' or category == 'apartment-sell':
            self['category'] = 'فروش مسکونی'
        elif category == 'industry-agriculture-business-sell':
            self['category'] = 'فروش اداری و تجاری'
        elif category == 'shop-sell':
            self['category'] = 'فروش اداری و تجاری'
        elif category == 'office-sell':
            self['category'] = 'فروش اداری و تجاری'
        elif category == 'industry-agriculture-business-rent':
            self['category'] = 'اجاره اداری و تجاری'
        elif category == 'shop-rent':
            self['category'] = 'اجاره اداری و تجاری'
        elif category == 'office-rent':
            self['category'] = 'اجاره اداری و تجاری'
        elif category == 'agency':
            self['category'] = 'خدمات املاک'
        elif category == 'partnership':
            self['category'] = 'خدمات املاک'
        elif category == 'financial-legal':
            self['category'] = 'خدمات املاک'
        elif category == 'presell':
            self['category'] = 'خدمات املاک'
        elif category == 'املاک':
            self['category'] = 'سایر املاک'
            self['sub_category'] = 'سایر املاک'


class RecruitmentItem(RecruitmentBaseItem, DivarBaseItem):

    def fetch_data(self, i):
        if 'همکاری' in i['title']:
            self['cooperation'] = i['value']
 
        elif 'دستمزد' in i['title']:
          try:
            if 'از' in i['value'] and 'تا' in i['value']:
                tmp = unidecode(i['value']
                                        ).replace('z', ''
                                        ).replace('twmn', ''
                                        ).replace(',', ''
                                        ).strip(
                                        ).split('t')
                
                self['salary'] = (int(tmp[0].strip()) + int(tmp[1].strip())) // 2
            
            elif 'حداقل' in i['value']:
                self['salary'] = int(unidecode(i['value']
                                                    ).replace('Hdql', ''
                                                    ).replace('twmn', ''
                                                    ).replace(',', ''
                                                    ).replace(' ', ''
                                                    ).strip())

            elif 'حداکثر' in i['value']:
                self['salary'] = int(
                                     unidecode(i['value']
                                     ).replace('Hdkhthr', ''
                                     ).replace('twmn', ''
                                     ).replace(',', ''
                                     ).replace(' ', ''
                                     ).strip())
            elif 'تومان' in i['value']:
                self['salary'] = int(
                                     unidecode(i['value']
                                     ).replace('twmn', ''
                                     ).replace(',', ''
                                     ).replace(' ', ''
                                     ).strip())
          except:
            pass
        elif 'بیمه' in i['title']:
            if 'ندارد' in i['value']:
                self['insurnace'] = False
            else:
                self['insurnace'] = True
            
        elif 'دورکاری' in i['title']:
            if i['value'] == 'دارد':
               self['teleworking'] = True
            else:
               self['teleworking'] = False

        elif 'نیاز به سابقه' in i['title']:
            if 'از' in i['value'] and 'تا' in i['value']:
                tmp = unidecode(i['value']
                                        ).replace('z', ''
                                        ).replace('sl', ''
                                        ).replace(',', ''
                                        ).strip(
                                        ).split('t')
                self['experience'] = (int(tmp[0].strip()) + int(tmp[1].strip())) // 2
            elif 'حداقل' in i['value']:
                self['experience'] = int(
                                        unidecode(i['value']
                                        ).replace('Hdql', ''
                                        ).replace('sl', ''
                                        ).replace(' ', ''))
            elif 'حداکثر' in i['value']:
                self['experience'] = int(
                                     unidecode(i['value']
                                     ).replace('Hdkhthr', ''
                                     ).replace('sl', ''
                                     ).replace(',', ''
                                     ).replace(' ', ''
                                     ).strip())
            elif 'کم‌تر' in i['value']:
                self['experience'] = int(
                                     unidecode(i['value']
                                     ).replace('khmtr', ''
                                     ).replace('sl', ''
                                     ).replace('z', ''
                                     ).replace(',', ''
                                     ).replace(' ', ''
                                     ).strip())
            elif 'بیش از' in i['value']:
                self['experience'] = int(
                                     unidecode(i['value']
                                     ).replace('bysh', ''
                                     ).replace('sl', ''
                                     ).replace('z', ''
                                     ).replace(',', ''
                                     ).replace(' ', ''
                                     ).strip())                       
            elif 'سال' in i['value']:
                self['experience'] = int(
                                     unidecode(i['value']
                                     ).replace('sl', ''
                                     ).replace(',', ''
                                     ).replace(' ', ''
                                     ).strip())
            elif 'ندارد' in i['value']:
                self['experience'] = 0
            
            else:
                self['experience'] = 0

    def extract(self, dict_data):
        DivarBaseItem.extract(self, dict_data)
        list_data = dict_data['widgets']['list_data']
        for i in list_data:
            if 'items' in i:
                for item in i['items']:
                    self.fetch_data(item)
            else:
                self.fetch_data(i)
                
        if self['cooperation'] == 'not_defined':
           self['cooperation'] = 'سایر'
        
        
        self['category'] = dict_data['data']['category']['title']
