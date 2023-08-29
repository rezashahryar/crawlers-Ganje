import datetime
from persiantools.jdatetime import JalaliDate


def hash_token(token, source_id):
    import hashlib
    token = f"{token}{source_id}"
    return int(str(int(hashlib.sha1(str(token).encode()).hexdigest(), 16))[:18])


def get_time_stamp():
    return int(datetime.datetime.now().timestamp())


def get_persian_year():
    return int(JalaliDate.today().year)


def get_production(age):
    if age is None or age == -1 or age == '-1':
        return -1
    else:
        return get_persian_year() - int(age)


def extract_model_brand(self, brand_model):
    i = dict()
    i['value'] = brand_model
    # pride 111
    if 'پراید' in i['value'] and '111' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '111'
        if 'ex' in i['value'].lower():
            self['tip'] = 'EX'
        elif 'se' in i['value'].lower():
            self['tip'] = 'SE'
        elif 'sl' in i['value'].lower():
            self['tip'] = 'SL'
        elif 'sx' in i['value'].lower():
            self['tip'] = 'SX'
    # pride 131
    elif 'پراید' in i['value'] and '131' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '131'
        if 'ex' in i['value'].lower():
            self['tip'] = 'EX'
        elif 'se' in i['value'].lower():
            self['tip'] = 'SE'
        elif 'sl' in i['value'].lower():
            self['tip'] = 'SL'
        elif 'sx' in i['value'].lower():
            self['tip'] = 'SX'
        elif 'le' in i['value'].lower():
            self['tip'] = 'LE'
        elif 'tl' in i['value'].lower():
            self['tip'] = 'TL'
    # pride 132
    elif 'پراید' in i['value'] and '132' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '132'
        if 'ex' in i['value'].lower():
            self['tip'] = 'EX'
        elif 'se' in i['value'].lower():
            self['tip'] = 'SE'
        elif 'sl' in i['value'].lower():
            self['tip'] = 'SL'
        elif 'sx' in i['value'].lower():
            self['tip'] = 'SX'
    # pride 141
    elif 'پراید' in i['value'] and '141' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '141'
        if 'ex' in i['value'].lower():
            self['tip'] = 'EX'
        elif 'se' in i['value'].lower():
            self['tip'] = 'SE'
        elif 'sx' in i['value'].lower():
            self['tip'] = 'SX'
    elif 'پراید' in i['value'] and 'صندوق‌' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'صندوق‌دار'
    elif 'پراید' in i['value'] and 'هاچ' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'هاچبک'
    elif ('وانت' in i['value'] or '151' in i['value']) and 'پراید' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'وانت'
    # pride others
    elif 'پراید' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = None

    # tiba with box
    elif 'تیبا' in i['value'] and 'صندوق‌' in i['value'].lower():
        self['brand'] = 'تیبا'
        self['model'] = 'صندوق دار'
        if 'پلاس' in i['value'].lower():
            self['tip'] = 'پلاس'
        elif 'ex' in i['value'].lower():
            self['tip'] = 'EX'
        elif 'lx' in i['value'].lower():
            self['tip'] = 'LX'
        elif 'sx' in i['value'].lower():
            self['tip'] = 'SX'
    # tiba without box
    elif ('تیبا' in i['value'] and 'هاچ' in i['value'].lower()) or ('تیبا' in i['value'] and '2' in i['value']):
        self['brand'] = 'تیبا'
        self['model'] = 'هاچ بک'
        if 'پلاس' in i['value'].lower():
            self['tip'] = 'پلاس'
        elif 'ex' in i['value'].lower():
            self['tip'] = 'EX'
        elif 'sx' in i['value'].lower():
            self['tip'] = 'SX'
    elif 'تیبا' in i['value']:
        self['brand'] = 'تیبا'
        self['model'] = 'صندوق دار'
        if 'پلاس' in i['value'].lower():
            self['tip'] = 'پلاس'
        elif 'ex' in i['value'].lower():
            self['tip'] = 'EX'
        elif 'lx' in i['value'].lower():
            self['tip'] = 'LX'
        elif 'sx' in i['value'].lower():
            self['tip'] = 'SX'
    
    # ario
    elif 'آریو' in i['value'] and 'اتوماتیک' in i['value'].lower():
        self['brand'] = 'آریو'
        self['model'] = 'اتوماتیک'
        if '1600cc' in i['value'].lower():
            self['tip'] = '1600cc'
    elif 'دنده‌ای' in i['value'] and '1500' in i['value'].lower():
        self['brand'] = 'آریو'
        self['model'] = 'دنده ای'
        if '1500cc' in i['value'].lower():
            self['tip'] = '1500cc'
    elif 'دنده‌ای' in i['value'] and '1600' in i['value'].lower():
        self['brand'] = 'آریو'
        self['model'] = 'دنده ای'
        if '1600cc' in i['value'].lower():
            self['tip'] = '1600cc'
    elif 'آریو' in i['value']:
        self['brand'] = 'آریو'
        self['model'] = None

    elif 'ساینا' in i['value'] and 'اتوماتیک' in i['value']:
        self['brand'] = 'ساینا'
        self['model'] = 'اتوماتیک'
    elif 'ساینا' in i['value'] and 'پلاس' in i['value']:
        self['brand'] = 'ساینا'
        self['model'] = 'دنده ای پلاس'
    elif 'ساینا' in i['value'] and 'ex' in i['value'].lower():
        self['brand'] = 'ساینا'
        self['model'] = 'EX'
    elif 'ساینا' in i['value'] and 'g' in i['value'].lower():
        self['brand'] = 'ساینا'
        self['model'] = 'G'
    elif 'ساینا' in i['value'] and 'sx' in i['value'].lower():
        self['brand'] = 'ساینا'
        self['model'] = 'SX'
    elif 'ساینا' in i['value'] and 's' in i['value'].lower():
        self['brand'] = 'ساینا'
        self['model'] = 'S'
    elif 'ساینا' in i['value']:
        self['brand'] = 'ساینا'
        self['model'] = None

    elif ('ام وی ام' in i['value'] or "ام‌وی‌ام" in i['value']) and '110s' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = '110S'
    elif ('ام وی ام' in i['value'] or "ام‌وی‌ام" in i['value']) and '110' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '110'
    elif ('ام وی ام' in i['value'] or "ام‌وی‌ام" in i['value']) and '315' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '315'
        if 'صندوق' in i['value']:
            self['tip'] = 'صندوق‌دار'
        elif 'هاچ' in i['value'] and 'پلاس' in i['value']:
            self['tip'] = 'هاچبک پلاس'
        elif 'هاچ' in i['value']:
            self['tip'] = 'هاچبک'
    elif ('ام وی ام' in i['value'] or "ام‌وی‌ام" in i['value']) and '530' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '530'
    elif ('ام وی ام' in i['value'] or "ام‌وی‌ام" in i['value']) and '550' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '550'
    elif ('ام وی ام' in i['value'] or "ام‌وی‌ام" in i['value']) and 'x33' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = 'X33'
        if 's' in i['value'].lower():
            self['tip'] = "S"
    elif ('ام وی ام' in i['value'] or "ام‌وی‌ام" in i['value']) and 'x22' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = 'X22'
        if 'pro' in i['value'].lower():
            self['tip'] = 'Pro'
    elif ('ام وی ام' in i['value'] or "ام‌وی‌ام" in i['value']) and 'x55' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = 'X55'
        if 'اکسلنت' in i['value']:
            self['tip'] = 'اکسلنت'
        elif 'pro' in i['value'].lower():
            self['tip'] = 'Pro'
    elif 'ام وی ام' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '‌None'

    
    #peugeut
    elif 'پژو' in i['value'] and '2008' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '2008'
    elif 'پژو' in i['value'] and '205' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '205'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD'
        if 'v1' in i['value'].lower():
            self['tip'] = 'v1'
        if 'v10' in i['value'].lower():
            self['tip'] = 'v10'
        elif 'v19' in i['value'].lower():
            self['tip'] = 'v19'
        elif 'v2' in i['value'].lower():
            self['tip'] = 'v2'
        elif 'v20' in i['value'].lower():
            self['tip'] = 'v20'
        elif 'v6' in i['value'].lower():
            self['tip'] = 'v6'
        elif 'v8' in i['value'].lower():
            self['tip'] = 'v8'
        elif 'v9' in i['value'].lower():
            self['tip'] = 'v9'
    elif 'پژو' in i['value'] and '206' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206'
        if 'تیپ ۱' in i['value'].lower() or "تیپ 1" in i['value'].lower():
            self['tip'] = 'تیپ ۱'
        elif 'تیپ ۲' in i['value'].lower() or "تیپ 2" in i['value'].lower():
            self['tip'] = 'تیپ ۲'
        elif 'تیپ ۳' in i['value'].lower() or "تیپ 3" in i['value'].lower():
            self['tip'] = 'تیپ ۳'
        elif 'تیپ ۴' in i['value'].lower() or "تیپ 4" in i['value'].lower():
            self['tip'] = 'تیپ ۴'
        elif 'تیپ ۵' in i['value'].lower() or "تیپ 5" in i['value'].lower():
            self['tip'] = 'تیپ ۵'
        elif 'تیپ ۶' in i['value'].lower() or "تیپ 6" in i['value'].lower():
            self['tip'] = 'تیپ ۶'
    elif 'پژو' in i['value'] and '207' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '207'
        if 'mc' in i['value'].lower():
            self['tip'] = 'MC'
        elif 'پانوراما' in i['value'].lower():
            self['tip'] = 'پانوراما'
        if 'sd' in i['value'].lower():
            self['tip'] = 'SD'
    elif 'پژو' in i['value'] and '301' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '301'
    elif 'پژو' in i['value'] and '404' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '404'
    elif 'پژو' in i['value'] and '405' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '405'
        if 'استیشن' in i['value'].lower():
            self['tip'] = 'استیشن'
        elif 'glx' in i['value'].lower():
            self['tip'] = 'GLX'
        elif 'gli' in i['value'].lower():
            self['tip'] = 'GLI'
        elif 'gl' in i['value'].lower():
            self['tip'] = 'GL'
        elif 'slx' in i['value'].lower():
            self['tip'] = 'SLX'
    elif 'پژو' in i['value'] and '406' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '406'
    elif 'پژو' in i['value'] and '407' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '407'
    elif 'پژو' in i['value'] and '504' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '504'
    elif 'پژو' in i['value'] and '508' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '508'
    elif 'پژو' in i['value'] and 'پارس' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = 'پارس'
        if 'elx' in i['value'].lower():
            self['tip'] = 'ELX'
        elif 'lx' in i['value'].lower():
            self['tip'] = 'LX'
        elif 'xu7p' in i['value'].lower():
            self['tip'] = 'XU7P'
        elif 'لیموزین' in i['value'].lower():
            self['tip'] = 'لیموزین'
    elif 'پژو' in i['value'] and ('روآ' in i['value'] or 'roa' in i['value'].lower() or 'روا' in i['value']):
        self['brand'] = 'پژو'
        self['model'] = 'روآ'
    elif 'پژو' in i['value'] and ('rd' in i['value'].lower() or 'آردی' in i['value'] or 'اردی' in i['value']):
        self['brand'] = 'پژو'
        self['model'] = 'RD'
    elif 'پژو' in i['value'] and 'rdi' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = 'RDI'
    elif 'پژو' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = None

    elif 'پیکان' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'پیکان'
        self['model'] = 'وانت'
    elif 'پیکان' in i['value']:
        self['brand'] = 'پیکان'
        self['model'] = 'سواری'

    elif 'دنا' in i['value'] and 'پلاس' in i['value']:
        self['brand'] = 'دنا'
        self['model'] = 'پلاس'
    elif 'دنا' in i['value'] and 'معمولی' in i['value']:
        self['brand'] = 'دنا'
        self['model'] = 'معمولی'
    elif 'دنا' in i['value']:
        self['brand'] = 'دنا'
        self['model'] = None

    elif 'رانا' in i['value'] and 'پلاس' in i['value']:
        self['brand'] = 'رانا'
        self['model'] = 'پلاس'
        if 'پانوراما' in i['value'].lower():
            self['tip'] = 'پانوراما'
    elif 'رانا' in i['value'] and 'el' in i['value'].lower():
        self['brand'] = 'رانا'
        self['model'] = 'EL'
    elif 'رانا' in i['value'] and 'lx' in i['value'].lower():
        self['brand'] = 'رانا'
        self['model'] = 'LX'
    elif 'رانا' in i['value']:
        self['brand'] = 'رانا'
        self['model'] = None

    elif 'سمند' in i['value'] and 'سریر' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = 'سریر'
    elif 'سمند' in i['value'] and 'سورن' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = 'سورن'
        if 'elx' in i['value'].lower():
            self['tip'] = 'ELX'
        elif 'پلاس' in i['value']:
            self['tip'] = 'پلاس'
        else:
            self['tip'] = 'معمولی'
    elif 'سورن' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = 'سورن'
        if 'elx' in i['value'].lower():
            self['tip'] = 'ELX'
        elif 'پلاس' in i['value']:
            self['tip'] = 'پلاس'
    elif 'سمند' in i['value'] and 'el' in i['value'].lower():
        self['brand'] = 'سمند'
        self['model'] = 'EL'
    elif 'سمند' in i['value'] and 'lx' in i['value'].lower():
        self['brand'] = 'سمند'
        self['model'] = 'LX'
    elif 'سمند' in i['value'] and 'se' in i['value'].lower():
        self['brand'] = 'سمند'
        self['model'] = 'SE'
    elif 'سمند' in i['value'] and 'x7' in i['value'].lower():
        self['brand'] = 'سمند'
        self['model'] = 'X7'
    elif 'سمند' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = None

    elif 'آریسان' in i['value'] :
        self['brand'] = 'آریسان'
        self['model'] = 'وانت'

    elif 'هایما' in i['value'] and 's5' in i['value'].lower():
        self['brand'] = 'هایما'
        self['model'] = 'S5'
    elif 'هایما' in i['value'] and 's7' in i['value'].lower():
        self['brand'] = 'هایما'
        self['model'] = 'S7'
    elif 'هایما' in i['value']:
        self['brand'] = 'هایما'
        self['model'] = None

    elif 'جک' in i['value'] and 'j3' in i['value'].lower():
        self['brand'] = 'جک'
        self['model'] = 'J3'
        if 'سدان' in i['value'].lower():
            self['tip'] = 'سدان'
        elif 'هاچ' in i['value'].lower():
            self['tip'] = 'هاچبک'
    elif 'جک' in i['value'] and ('j4' in i['value'].lower() or 'جی 4' in i['value']):
        self['brand'] = 'جک'
        self['model'] = 'J4'
    elif 'جک' in i['value'] and ('j5' in i['value'].lower() or 'جی 5' in i['value']):
        self['brand'] = 'جک'
        self['model'] = 'J5'
    elif 'جک' in i['value'] and 's3' in i['value'].lower():
        self['brand'] = 'جک'
        self['model'] = 'S3'
    elif 'جک' in i['value'] and 's5' in i['value'].lower():
        self['brand'] = 'جک'
        self['model'] = 'S5'
    elif 'جک' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'جک'
        self['model'] = 'ون'
        if 'ریفاین' in i['value'].lower():
            self['tip'] = 'ریفاین'
        elif 'سانری' in i['value'].lower():
            self['tip'] = 'سانری'
    elif 'جک' in i['value']:
        self['brand'] = 'جک'
        self['model'] = None

    elif 'جیلی' in i['value'] and ('emgrand' in i['value'].lower() or 'امگرند' in i['value']):
        self['brand'] = 'جیلی'
        self['model'] = 'امگرند'
        if '7' in i['value'].lower():
            self['tip'] = '7'
        if '7 آر وی' in i['value'].lower() or 'rv7' in i['value'].lower():
            self['tip'] = 'RV7'
        if 'ایکس 7' in i['value'].lower() or 'x7' in i['value'].lower() or 'ایکس ۷' in i['value']:
            self['tip'] = 'ٓX7'
    elif 'جیلی' in i['value'] and 'gc6' in i['value'].lower():
        self['brand'] = 'جیلی'
        self['model'] = 'GC6'
    elif 'جیلی' in i['value']:
        self['brand'] = 'جیلی'
        self['model'] = None

    elif 'لیفان' in i['value'] and '520i' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = '520i'
    elif 'لیفان' in i['value'] and '520' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = '520'
    elif 'لیفان' in i['value'] and '620' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = '620'
    elif 'لیفان' in i['value'] and '820' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = '820'
    elif 'لیفان' in i['value'] and 'x50' in i['value'].lower():
        self['brand'] = 'لیفان'
        self['model'] = 'X50'
    elif 'لیفان' in i['value'] and 'x60' in i['value'].lower():
        self['brand'] = 'لیفان'
        self['model'] = 'X60'
    elif 'لیفان' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = None

    elif 'رنو' in i['value'] and 'اسکالا' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'اسکالا'
    elif 'تندر' in i['value'] and '90' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'تندر 90'
        if 'e0' in i['value'].lower():
            self['tip'] = 'E0'
        elif 'e1' in i['value'].lower():
            self['tip'] = 'E1'
        elif 'e2' in i['value'].lower():
            self['tip'] = 'E2'
        elif 'پلاس' in i['value']:
            self['tip'] = 'پلاس'
        elif 'استیشن' in i['value']:
            self['tip'] = 'استیشن'
    elif 'تندر' in i['value'] and 'پارس' in i['value'].lower():
        self['brand'] = 'رنو'
        self['model'] = 'پارس تندر'
    elif 'رنو' in i['value'] and 'پارس' in i['value'].lower():
        self['brand'] = 'رنو'
        self['model'] = 'پارس تندر'
    elif 'رنو' in i['value'] and 'پی' in i['value'].lower():
        self['brand'] = 'رنو'
        self['model'] = 'PK'
    elif 'رنو' in i['value'] and ('تلیسمان' in i['value'] or 'تالیسمان' in i['value']):
        self['brand'] = 'رنو'
        self['model'] = 'تلیسمان'
        if 'e2' in i['value'].lower():
            self['tip'] = 'E2'
        if 'e3' in i['value'].lower():
            self['tip'] = 'E3'
    elif 'رنو' in i['value'] and 'تندر' in i['value'].lower():
        self['brand'] = 'رنو'
        self['model'] = 'تندر 90'
        if 'e0' in i['value'].lower():
            self['tip'] = 'E0'
        elif 'e1' in i['value'].lower():
            self['tip'] = 'E1'
        elif 'e2' in i['value'].lower():
            self['tip'] = 'E2'
        elif 'پلاس' in i['value']:
            self['tip'] = 'پلاس'
        elif 'پارس' in i['value']:
            self['tip'] = 'پارس'
        elif 'استیشن' in i['value']:
            self['tip'] = 'استیشن'
    elif 'رنو' in i['value'] and 'داستر' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'داستر'
    elif 'رنو' in i['value'] and 'ساندرو' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'ساندرو'
        if 'استب وی' in i['value'].lower() or 'استپ‌وی' in i['value']:
            self['tip'] = 'استب وی'
    elif 'رنو' in i['value'] and 'سپند' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'سپند'
    elif 'رنو' in i['value'] and 'سفران' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'سفران'
    elif 'رنو' in i['value'] and 'سیمبل' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'سیمبل'
    elif 'رنو' in i['value'] and 'فلوئنس' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'فلوئنس'
    elif 'رنو' in i['value'] and 'کپچر' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'کپچر'
    elif 'رنو' in i['value'] and ('کولیوس' in i['value'] or'کوليوس' in i['value']):
        self['brand'] = 'رنو'
        self['model'] = 'کوليوس'
    elif 'رنو' in i['value'] and 'لاگونا' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'لاگونا'
    elif 'رنو' in i['value'] and 'لتیتود' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'لتیتود'
    elif 'رنو' in i['value'] and 'مگان' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'مگان'
    elif 'رنو' in i['value'] and 'مگان' in i['value'].lower():
        self['brand'] = 'رنو'
        self['model'] = 'مگان'
        if '1600' in i['value'].lower():
            self['tip'] = '1600cc'
        elif '2000' in i['value'].lower():
            self['tip'] = '2000cc'
    elif 'وانت' in i['value'] and 'رنو' in i['value'] and 'وانت' in i['value'].lower():
        self['brand'] = 'رنو'
        self['model'] = 'وانت'
    elif 'رنو' in i['value'] and '21' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = '21'
    elif 'رنو' in i['value'] and '5' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = '5'
    elif 'رنو' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = None

    elif 'برلیانس' in i['value'] and 'h220' in i['value'].lower():
        self['brand'] = 'برلیانس'
        self['model'] = 'H220'
    elif 'برلیانس' in i['value'] and 'h230' in i['value'].lower():
        self['brand'] = 'برلیانس'
        self['model'] = 'H230'
    elif 'برلیانس' in i['value'] and 'h320' in i['value'].lower():
        self['brand'] = 'برلیانس'
        self['model'] = 'H320'
    elif 'برلیانس' in i['value'] and 'h330' in i['value'].lower():
        self['brand'] = 'برلیانس'
        self['model'] = 'H330'
    elif 'برلیانس' in i['value'] and 'v5' in i['value'].lower():
        self['brand'] = 'برلیانس'
        self['model'] = 'V5'
    elif 'برلیانس' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'ون'
    elif 'برلیانس' in i['value'] and 'کراس' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'کراس'    
    elif 'برلیانس' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = None

    elif 'هیوندای' in i['value'] and 'آزرا' in i['value'] and 'گرنجور' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'آزرا گرنجور'
    elif 'هیوندای' in i['value'] and 'آوانته' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'آوانته'
    elif 'هیوندای' in i['value'] and 'اسکوپ' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'اسکوپ'
    elif 'هیوندای' in i['value'] and 'اکسل' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'اکسل'
    elif 'هیوندای' in i['value'] and 'اکسنت' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'اکسنت'
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
        elif 'ساده' in i['value'].lower():
            self['tip'] = 'ساده' 
        elif 'بلو' in i['value'].lower():
            self['tip'] = 'بلو' 
    elif 'هیوندای' in i['value'] and 'النترا' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'النترا'   
        if '1600' in i['value']:
            self['tip'] = "1600cc"
        elif '1800' in i['value']:
            self['tip'] = "1800cc"    
        elif '2000' in i['value']:
            self['tip'] = "2000cc"
    elif 'هیوندای' in i['value'] and 'تراجت' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'تراجت'
    elif 'هیوندای' in i['value'] and 'توسان' in i['value'].lower():
        self['brand'] = 'هیوندای'
        self['model'] = 'توسان'
        if 'ix' in i['value'].lower() and '35' in i['value']:
            self['tip'] = 'ix 35'
    elif 'هیوندای' in i['value'] and 'جنسیس' in i['value'].lower():
        self['brand'] = 'هیوندای'
        self['model'] = 'جنسیس'
        if 'سدان' in i['value'].lower():
            self['tip'] = 'سدان'
        if 'کوپه' in i['value'].lower():
            self['tip'] = 'کوپه'
    elif 'هیوندای' in i['value'] and 'سانتافه' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'سانتافه'
        if 'ix' in i['value'].lower() and '45' in i['value']:
            self['tip'] = 'ix 45'
    elif 'هیوندای' in i['value'] and 'سنتنیال' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'سنتنیال'
    elif 'هیوندای' in i['value'] and 'سوناتا' in i['value'].lower():
        self['brand'] = 'هیوندای'
        self['model'] = 'سوناتا'
        if 'lf' in i['value'].lower():
            self['tip'] = 'LF'
        if 'lf هیبرید' in i['value'].lower():
            self['tip'] = 'LF هیبرید'
        if 'nf' in i['value'].lower():
            self['tip'] = 'NF'
        if 'yf' in i['value'].lower():
            self['tip'] = 'YF'
    elif 'هیوندای' in i['value'] and 'وراکروز' in i['value'].lower():
        self['brand'] = 'هیوندای'
        self['model'] = 'وراکروز'
        if 'ix55' in i['value'].lower():
            self['tip'] = 'iX55'
    elif 'هیوندای' in i['value'] and 'ورنا' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'ورنا'
    elif 'هیوندای' in i['value'] and 'ولستر' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'ولستر'
    elif 'هیوندای' in i['value'] and 'fx' in i['value'].lower():
        self['brand'] = 'هیوندای'
        self['model'] = 'FX'
        if 'کوپه' in i['value'].lower():
            self['tip'] = 'کوپه'
    elif 'هیوندای' in i['value'] and 'i10' in i['value'].lower():
        self['brand'] = 'هیوندای'
        self['model'] = 'i10'
    elif 'هیوندای' in i['value'] and 'i20' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'i20'
    elif 'هیوندای' in i['value'] and 'i30' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'i30'
    elif 'هیوندای' in i['value'] and 'i40' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'i40'
        if 'استیشن' in i['value']:
            self['tip'] = 'استیشن'
    elif 'هیوندای' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'ون'
        if 'h1' in i['value'].lower():
            self['tip'] = 'H1'
        elif 'h350' in i['value'].lower():
            self['tip'] = 'H350'
    elif 'هیوندای' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = None

    elif 'کیا' in i['value'] and 'اپتیما' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'اپتیما'
        if '2400' in i['value'].lower():
            self['tip'] = '2400cc'
        elif '2700' in i['value'].lower():
            self['tip'] = '2700cc'
    elif 'کیا' in i['value'] and 'اپیروس' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'اپیروس'
    elif 'کیا' in i['value'] and 'اسپورتیج' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'اسپورتیج'
        if '2400' in i['value'].lower():
            self['tip'] = '2400cc'
        elif '2700' in i['value'].lower():
            self['tip'] = '2700cc'
    elif 'کیا' in i['value'] and 'پیکانتو' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'پیکانتو'
    elif 'کیا' in i['value'] and 'ریو' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'ریو'
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
        elif 'هاچ' in i['value'].lower():
            self['tip'] = 'هاچ بک'
        elif 'سدان' in i['value'].lower():
            self['tip'] = 'سدان'
    elif 'کیا' in i['value'] and 'سراتو' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'سراتو'
        if '1600' in i['value'].lower():
            self['tip'] = '1600cc'
        elif '2000' in i['value'].lower():
            self['tip'] = '2000cc'
    elif 'کیا' in i['value'] and 'سورنتو' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'سورنتو'
        if 'اول' in i['value'] or '1' in i['value'] or '۱' in i['value']:
            self['tip'] = 'نسل اول'
        elif 'دوم' in i['value'] or '2' in i['value'] or '۲' in i['value']:
            self['tip'] = 'نسل دوم'
        elif 'سوم' in i['value'] or '3' in i['value'] or '۳' in i['value']:
            self['tip'] = 'نسل سوم'
    elif 'کیا' in i['value'] and 'سول' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'سول'
    elif 'کیا' in i['value'] and 'کادنزا' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'کادنزا'
    elif 'کیا' in i['value'] and 'کارناوال' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'کارناوال'
    elif 'کیا' in i['value'] and 'کارنز' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'کارنز'
    elif 'کیا' in i['value'] and 'موهاوی' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'موهاوی'
        if '6' in i['value'] and 'سیلندر':
            self['tip'] = '6 سیلندر'
        elif '8' in i['value'] and 'سیلندر':
            self['tip'] = '8 سیلندر'
    elif 'کیا' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = None

    elif 'بسترن' in i['value'] and 'B30' in i['value']:
        self['brand'] = 'بسترن'
        self['model'] = 'B30'
    elif 'بسترن' in i['value'] and 'b50f' in i['value'].lower():
        self['brand'] = 'بسترن'
        self['model'] = 'B50F'
    elif 'بسترن' in i['value'] and 'b50' in i['value'].lower():
        self['brand'] = 'بسترن'
        self['model'] = 'B50'
    elif 'بسترن' in i['value']:
        self['brand'] = 'بسترن'
        self['model'] = None
# new
    elif 'آئودی' in i['value'] and 'Q5' in i['value']:
        self['brand'] = 'آئودی'
        self['model'] = 'Q5'
    elif 'آئودی' in i['value'] and 'TT' in i['value']:
        self['brand'] = 'آئودی'
        self['model'] = 'TT'
    elif 'آئودی' in i['value']:
        self['brand'] = 'آئودی'
        self['model'] = None

    elif 'آلفارومئو' in i['value'] and '4c' in i['value'].lower():
        self['brand'] = 'آلفارومئو '
        self['model'] = '4C'
    elif 'آلفارومئو' in i['value'] and 'جولیتا' in i['value']:
        self['brand'] = 'آلفارومئو'
        self['model'] = 'جولیتا'
    elif 'آلفارومئو' in i['value'] and 'میتو' in i['value']:
        self['brand'] = 'آلفارومئو'
        self['model'] = 'میتو'
    elif 'آلفارومئو' in i['value']:
        self['brand'] = 'آلفارومئو'
        self['model'] = None

    elif 'آمیکو' in i['value'] and 'آراز' in i['value']:
        self['brand'] = 'آمیکو وانت'
        self['model'] = 'آراز'
        if ('دو' in i['value'].lower() or '2' in i['value'] or '۲' in i['value']) and 'دیفرانسیل' in i['value']:
            self['tip'] = 'دو دیفرانسیل'
        elif ('تک' in i['value'].lower() or '1' in i['value'] or '۱' in i['value']) and 'دیفرانسیل' in i['value']:
            self['tip'] = 'تک دیفرانسیل'
    elif 'آمیکو' in i['value'] and 'آسنا' in i['value']:
        self['brand'] = 'آمیکو وانت'
        self['model'] = 'آسنا'
    elif 'آمیکو وانت' in i['value']:
        self['brand'] = 'آمیکو وانت'
        self['model'] = None

    elif 'اپل' in i['value'] and 'آسترا' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'آسترا'
        if 'استیشن' in i['value']:
            self['tip'] = 'استیشن'
        elif 'هاچ' in i['value']:
            self['tip'] = 'هاچبک'
    elif 'اپل' in i['value'] and 'امگا' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'امگا'
    elif 'اپل' in i['value'] and 'اینسیگنیا' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'اینسیگنیا'
    elif 'اپل' in i['value'] and 'کالیبرا' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'کالیبرا'
    elif 'اپل' in i['value'] and 'کورسا' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'کورسا'
    elif 'اپل' in i['value'] and 'موکا' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'موکا'
    elif 'اپل' in i['value'] and 'وکترا' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'وکترا'
    elif 'اپل' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = None

    elif ('اس‌دبلیو‌ام' in i['value'] or 'اس دبلیو ام' in i['value']) and 'g01 f' in i['value'].lower():
        self['brand'] = 'اس‌دبلیو‌ام'
        self['model'] = 'G01 F'
    elif ('اس‌دبلیو‌ام' in i['value'] or 'اس دبلیو ام' in i['value']) and 'g01' in i['value'].lower():
        self['brand'] = 'اس‌دبلیو‌ام'
        self['model'] = 'G01'
    elif 'اس‌دبلیو‌ام' in i['value']:
        self['brand'] = 'اس‌دبلیو‌ام'
        self['model'] = None

    elif 'اسمارت' in i['value'] and '2' in i['value'] and 'فور' in i['value']:
        self['brand'] = 'اسمارت'
        self['model'] = 'فور 2'
    elif 'اسمارت' in i['value'] and '4' in i['value'] and 'فور' in i['value']:
        self['brand'] = 'اسمارت'
        self['model'] = 'فور 4'
    elif 'اسمارت' in i['value']:
        self['brand'] = 'اسمارت'
        self['model'] = None

    elif 'الدزمبیل' in i['value'] and 'ریجنسی' in i['value']:
        self['brand'] = 'الدزمبیل'
        self['model'] = 'ریجنسی'
    elif 'الدزمبیل' in i['value'] and 'کاتالاس' in i['value']:
        self['brand'] = 'الدزمبیل'
        self['model'] = 'کاتالاس'
    elif 'الدزمبیل' in i['value']:
        self['brand'] = 'الدزمبیل'
        self['model'] = None


    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']) and '350' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '350'
    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']) and '360' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '360'
    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']) and '550' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '550'
    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']) and '3' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '3'
    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']) and '6' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '6'
    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']) and 'gs' in i['value'].lower():
        self['brand'] = 'ام‌جی'
        self['model'] = 'GS'
    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']) and 'gt' in i['value'].lower():
        self['brand'] = 'ام‌جی'
        self['model'] = 'GT'
    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']) and 'rx5' in i['value'].lower():
        self['brand'] = 'ام‌جی'
        self['model'] = 'RX5'
    elif ('ام‌جی' in i['value'] or 'ام جی' in i['value']):
        self['brand'] = 'ام‌جی'
        self['model'] = None

    elif 'ایسوزو' in i['value'] and 'دو کابین' in i['value']:
        self['brand'] = 'ایسوزو'
        self['model'] = 'دو کابین'
    elif 'ایسوزو' in i['value']:
        self['brand'] = 'ایسوزو'
        self['model'] = None

    elif 'اینرودز' in i['value'] and 'c35' in i['value'].lower():
        self['brand'] = 'اینرودز'
        self['model'] = 'C35'
    elif 'اینرودز' in i['value']:
        self['brand'] = 'اینرودز'
        self['model'] = None

    elif 'ایویکو' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'ایویکو'
        self['model'] = 'ون'
    elif 'ایویکو' in i['value']:
        self['brand'] = 'ایویکو'
        self['model'] = None

    elif 'بایک' in i['value'] and 'سابرینا' in i['value']:
        self['brand'] = 'بایک'
        self['model'] = 'سابرینا'
    elif 'بایک' in i['value'] and 'سنوا' in i['value']:
        self['brand'] = 'بایک'
        self['model'] = 'سنوا'
    elif 'بایک' in i['value'] and 'x25' in i['value'].lower():
        self['brand'] = 'بایک'
        self['model'] = 'X25'
    elif 'بایک' in i['value']:
        self['brand'] = 'بایک'
        self['model'] = None

    elif 'بورگوارد' in i['value'] and 'bx5' in i['value'].lower():
        self['brand'] = 'بورگوارد'
        self['model'] = 'BX5'
    elif 'بورگوارد' in i['value'] and 'bx7' in i['value'].lower():
        self['brand'] = 'بورگوارد'
        self['model'] = 'BX7'
    elif 'بورگوارد' in i['value']:
        self['brand'] = 'بورگوارد'
        self['model'] = None

    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and '2002' in i['value']:
        self['brand'] = 'بی ام و'
        self['model'] = '2002'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 1' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 1'
        if 'هاچ' in i['value'].lower():
            self['tip'] = 'هاچبک'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 2' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 2'
        if 'اکتیوتور' in i['value']:
            self['tip'] = 'اکتیوتور'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 2' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 2'
        if 'کروک' in i['value'].lower():
            self['tip'] = 'کروک'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 2' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 2'
        if 'کوپه' in i['value'].lower():
            self['tip'] = 'کوپه'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 3' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 3'
        if 'gt' in i['value'].lower():
            self['tip'] = 'gt'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 4' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 4'
        if 'گرن' in i['value'].lower():
            self['tip'] = 'گرن'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 5' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 5'
        if 'gt' in i['value'].lower():
            self['tip'] = 'gt'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 6' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 6'
        if 'گرن' in i['value'].lower():
            self['tip'] = 'گرن'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'سری 7' in i['value']:
        self['brand'] = 'بی ام و'
        self['model'] = 'سری 7'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'کلاسیک' in i['value']:
        self['brand'] = 'بی ام و'
        self['model'] = 'کلاسیک'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'i8' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'i8'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'x1' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'X1'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'x3' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'X3'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'x4' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'X4'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'x5' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'X5'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'x6' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'X6'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'z3' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'Z3'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']) and 'z4' in i['value'].lower():
        self['brand'] = 'بی ام و'
        self['model'] = 'Z4'
    elif ('بی‌ام‌و' in i['value'] or 'بی ام و' in i['value'] or 'ب ام و' in i['value']):
        self['brand'] = 'بی ام و'
        self['model'] = None

    elif 'بیسو' in i['value'] and 't3' in i['value'].lower():
        self['brand'] = 'بیسو'
        self['model'] = 'T3'
    elif 'بیسو' in i['value'] and 't5' in i['value'].lower():
        self['brand'] = 'بیسو'
        self['model'] = 'T5'
    elif 'بیسو' in i['value']:
        self['brand'] = 'بیسو'
        self['model'] = None

    elif ('بی‌‌وای‌دی' in i['value'] or 'بی وای دی' in i['value']) and 'f3' in i['value'].lower():
        self['brand'] = 'بی وای دی'
        self['model'] = 'F3'
    elif ('بی‌‌وای‌دی' in i['value'] or 'بی وای دی' in i['value']) and 's6' in i['value'].lower():
        self['brand'] = 'بی وای دی'
        self['model'] = 'S6'
    elif ('بی‌‌وای‌دی' in i['value'] or 'بی وای دی' in i['value']) and 's7' in i['value'].lower():
        self['brand'] = 'بی وای دی'
        self['model'] = 'S7'
    elif ('بی‌‌وای‌دی' in i['value'] or 'بی وای دی' in i['value']):
        self['brand'] = 'بی وای دی'
        self['model'] = None

    elif 'بیوک' in i['value'] and 'b2' in i['value'].lower():
        self['brand'] = 'بیوک'
        self['model'] = 'B2'
    elif 'بیوک' in i['value'] and 'b3' in i['value'].lower():
        self['brand'] = 'بیوک'
        self['model'] = 'B3'
    elif 'بیوک' in i['value']:
        self['brand'] = 'بیوک'
        self['model'] = None

    elif 'پاژن' in i['value'] and ('2 در' in i['value'] or 'تک کابین' in i['value']):
        self['brand'] = 'پاژن'
        self['model'] = '2 در'
    elif 'پاژن' in i['value'] and ('4 در' in i['value'] or 'دوکابین' in i['value']):
        self['brand'] = 'پاژن'
        self['model'] = '4 در'
        if '2' in i['value'] and 'سیلندر' in i['value']:
            self['tip'] = '2 سیلندر'
        elif '2' in i['value'] and 'سیلندر' in i['value']:
            self['tip'] = '2 سیلندر'
    elif 'پاژن' in i['value'] and 'هرور' in i['value']:
        self['brand'] = 'پاژن'
        self['model'] = 'هرور'
    elif 'پاژن' in i['value']:
        self['brand'] = 'پاژن'
        self['model'] = None

    elif 'پروتون' in i['value'] and 'ایمپین' in i['value']:
        self['brand'] = 'پروتون'
        self['model'] = 'ایمپین'
    elif 'پروتون' in i['value'] and 'جن تو' in i['value']:
        self['brand'] = 'پروتون'
        self['model'] = 'جن تو'
    elif 'پروتون' in i['value'] and 'ویرا' in i['value']:
        self['brand'] = 'پروتون'
        self['model'] = 'ویرا'
    elif 'پروتون' in i['value']:
        self['brand'] = 'پروتون'
        self['model'] = None

    elif 'پورشه' in i['value'] and '911' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = '911'
        if 'کررا' in i['value'] and 's' in i['value'].lower():
            self['tip'] = 'کررا S'
        elif 'کررا' in i['value'] and '4' in i['value']:
            self['tip'] = 'کررا 4'
    elif 'پورشه' in i['value'] and 'باکستر' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'باکستر'
        if '718' in i['value'] and 's' in i['value'].lower():
            self['tip'] = '718 S'
        elif '718' in i['value']:
            self['tip'] = '718'
        if 'v6' in i['value'].lower() and 's' in i['value'].lower():
            self['tip'] = 'V6 S'
        elif 'v6' in i['value'].lower():
            self['tip'] = 'V6'
    elif 'پورشه' in i['value'] and 'پانامرا' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'پانامرا'
        if '4s' in i['value'].lower() and 'توربو' in i['value']:
            self['tip'] = '4S توربو'
        elif '4s' in i['value'].lower():
            self['tip'] = '4S'
        elif 'v6' in i['value'].lower():
            self['tip'] = 'V6'
    elif 'پورشه' in i['value'] and 'کاین' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'کاین'
        if 'gts' in i['value'].lower():
            self['tip'] = 'GTS'
        elif 's' in i['value'].lower() and 'توربو' in i['value']:
            self['tip'] = 'S توربو'
        elif 's' in i['value'].lower():
            self['tip'] = 'S'
        elif 'v6' in i['value'].lower():
            self['tip'] = 'V6'
    elif 'پورشه' in i['value'] and 'کیمن' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'کیمن'
        if 's' in i['value'].lower():
            self['tip'] = 'S'
    elif 'پورشه' in i['value'] and 'ماکان' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'ماکان'
    elif 'پورشه' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = None

    elif 'پونتیاک' in i['value'] and 'پاریزین' in i['value']:
        self['brand'] = 'پونتیاک'
        self['model'] = 'پاریزین'
    elif 'پونتیاک' in i['value'] and 'گرند پریکس' in i['value']:
        self['brand'] = 'پونتیاک'
        self['model'] = 'گرند پریکس'
    elif 'پونتیاک' in i['value']:
        self['brand'] = 'پونتیاک'
        self['model'] = None

    elif 'سوزوکی' in i['value'] and 'کیزاشی' in i['value']:
        self['brand'] = 'سوزوکی'
        self['model'] = 'کیزاشی'
    elif 'سوزوکی' in i['value'] and 'ویتارا' in i['value'].lower():
        self['brand'] = 'سوزوکی'
        self['model'] = 'گرند ویتارا'
        if '2000' in i['value'].lower():
            self['tip'] = '2000cc'
        elif '2400' in i['value'].lower():
            self['tip'] = '2400cc'
    elif 'سوزوکی' in i['value']:
        self['brand'] = 'سوزوکی'
        self['model'] = None

    elif 'تارا' in i['value'] and 'اتوماتیک' in i['value']:
        self['brand'] = 'تارا'
        self['model'] = 'اتوماتیک'
    elif 'تارا' in i['value'] and 'دنده ای' in i['value']:
        self['brand'] = 'تارا'
        self['model'] = 'دنده ای'
    elif 'تارا' in i['value']:
        self['brand'] = 'تارا'
        self['model'] = None

    elif 'تویوتا' in i['value'] and 'آریون' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'آریون'
    elif 'تویوتا' in i['value'] and 'اف جی کروز' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'اف جی کروز'
    elif 'تویوتا' in i['value'] and 'اکو' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'اکو'
    elif 'تویوتا' in i['value'] and 'پرادو' in i['value'].lower():
        self['brand'] = 'تویوتا'
        self['model'] = 'پرادو'
        if '2 در' in i['value'].lower():
            self['tip'] = '2 در'
        elif '4 در' in i['value'].lower():
            self['tip'] = '4 در'
    elif 'تویوتا' in i['value'] and 'پریوس' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'پریوس'
    elif 'تویوتا' in i['value'] and 'راوفور' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'راوفور'
    elif 'تویوتا' in i['value'] and 'سلیکا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'سلیکا'
    elif 'تویوتا' in i['value'] and 'سوپرا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'سوپرا'
    elif 'تویوتا' in i['value'] and 'سولارا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'سولارا'
    elif 'تویوتا' in i['value'] and 'فررانر' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'فررانر'
    elif 'تویوتا' in i['value'] and 'فورچونر' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'فورچونر'
    elif 'تویوتا' in i['value'] and 'کارینا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'کارینا'
    elif 'تویوتا' in i['value'] and 'کراون' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'کراون'
    elif 'تویوتا' in i['value'] and 'کرولا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'کرولا'
    elif 'تویوتا' in i['value'] and 'کرونا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'کرونا'
    elif 'تویوتا' in i['value'] and 'کریسیدا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'کریسیدا'
    elif 'تویوتا' in i['value'] and 'کمری' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'کمری'
    elif 'تویوتا' in i['value'] and 'وانت لندکروز' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'وانت لندکروز'
    elif 'تویوتا' in i['value'] and 'لندکروز' in i['value'].lower():
        self['brand'] = 'تویوتا'
        self['model'] = 'لندکروز'
        if '2 در' in i['value'].lower():
            self['tip'] = '2 در'
        elif '4 در' in i['value'].lower():
            self['tip'] = '4 در'
    elif 'تویوتا' in i['value'] and 'هایلوکس' in i['value'].lower():
        self['brand'] = 'تویوتا'
        self['model'] = 'هایلوکس '
        if 'تک کابین' in i['value'].lower():
            self['tip'] = 'تک کابین'
        elif 'دو کابین' in i['value'].lower():
            self['tip'] = 'دو کابین'
        elif 'دو کابین بلند' in i['value'].lower():
            self['tip'] = 'دو کابین بلند'
    elif 'تویوتا' in i['value'] and 'یاریس' in i['value'].lower():
        self['brand'] = 'تویوتا'
        self['model'] = 'یاریس'
        if 'صندوق دار' in i['value'].lower():
            self['tip'] = 'صندوق دار'
        elif 'هاچ' in i['value'].lower():
            self['tip'] = 'هاچبک'
    elif 'تویوتا' in i['value'] and ('r' in i['value'].lower() and 'h' in i['value'].lower() and 'c' in i['value'].lower()):
        self['brand'] = 'تویوتا'
        self['model'] = 'CHR'
    elif 'تویوتا' in i['value'] and 'gt' in i['value'].lower() and '86' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'GT 86'
    elif 'تویوتا' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'ون'
    elif 'تویوتا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = None

    elif 'جگوار' in i['value'] and 'xj' in i['value'].lower():
        self['brand'] = 'جگوار'
        self['model'] = 'XJ'
    elif 'جگوار' in i['value']:
        self['brand'] = 'جگوار'
        self['model'] = None

    elif 'جوی لانگ' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'جوی لانگ'
        self['model'] = 'ون'
    elif 'جوی لانگ' in i['value']:
        self['brand'] = 'جوی لانگ'
        self['model'] = None

    elif ('جی‌ام‌سی' in i['value'] or 'جی ام سی' in i['value']) and 's350' in i['value'].lower():
        self['brand'] = 'جی‌ام‌سی'
        self['model'] = 'S350'
    elif ('جی‌ام‌سی' in i['value'] or 'جی ام سی' in i['value']):
        self['brand'] = 'جی‌ام‌سی'
        self['model'] = None
    
    elif ('جی‌ای‌سی گونو' in i['value'] or 'جی ای سی گونو' in i['value'] or 'گک' in i['value']) and 'gx5' in i['value'].lower():
        self['brand'] = 'جی ای سی گونو'
        self['model'] = 'GX5'
    elif ('جی‌ای‌سی گونو' in i['value'] or 'جی ای سی گونو' in i['value'] or 'گک' in i['value']) and 'g5' in i['value'].lower():
        self['brand'] = 'جی ای سی گونو'
        self['model'] = 'G5'
    elif ('جی‌ای‌سی گونو' in i['value'] or 'جی ای سی گونو' in i['value'] or 'گک' in i['value']) and 'ga3s' in i['value'].lower():
        self['brand'] = 'جی ای سی گونو'
        self['model'] = 'GA3S'
    elif ('جی‌ای‌سی گونو' in i['value'] or 'جی ای سی گونو' in i['value'] or 'گک' in i['value']) and 'gs5' in i['value'].lower():
        self['brand'] = 'جی ای سی گونو'
        self['model'] = 'GS5'
    elif ('جی‌ای‌سی گونو' in i['value'] or 'جی ای سی گونو' in i['value'] or 'گک' in i['value']) and 'وانت' in i['value']:
        self['brand'] = 'جی ای سی گونو'
        self['model'] = 'وانت'
    elif ('جی‌ای‌سی گونو' in i['value'] or 'جی ای سی گونو' in i['value'] or 'گک' in i['value']):
        self['brand'] = 'جی ای سی گونو'
        self['model'] = None

    elif 'جیپ' in i['value'] and 'آهو' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'آهو'
    elif 'جیپ' in i['value'] and 'چروکی' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'چروکی'
    elif 'جیپ' in i['value'] and 'رنگلر' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'رنگلر'
    elif 'جیپ' in i['value'] and 'رنه گید' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'رنه گید'
    elif 'جیپ' in i['value'] and 'شهباز' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'شهباز'
    elif 'جیپ' in i['value'] and 'صحرا' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'صحرا'
    elif 'جیپ' in i['value'] and 'میوت' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'میوت'
    elif 'جیپ' in i['value'] and 'واگونیر' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'واگونیر'
    elif 'جیپ' in i['value'] and 'km' in i['value'].lower():
        self['brand'] = 'جیپ'
        self['model'] = 'KM'
    elif 'جیپ' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'وانت'
    elif 'جیپ' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = None

    elif 'چانگان' in i['value'] and 'cs' in i['value'].lower() and '35' in i['value']:
        self['brand'] = 'چانگان'
        self['model'] = 'CS35'
    elif 'چانگان' in i['value'] and 'eado' in i['value'].lower():
        self['brand'] = 'چانگان'
        self['model'] = 'EADO'
    elif 'چانگان' in i['value']:
        self['brand'] = 'چانگان'
        self['model'] = None

    elif 'چری' in i['value'] and 'آریزو' in i['value'].lower():
        self['brand'] = 'چری'
        self['model'] = 'آریزو'
        if '5' in i['value'] and 'ie' in i['value'].lower():
            self['tip'] = '5ie'
        elif '5' in i['value'] and 'te' in i['value'].lower():
            self['tip'] = '5te'
        elif '5' in i['value'].lower():
            self['tip'] = '5'
        elif '6' in i['value'].lower():
            self['tip'] = '6'
    elif 'چری' in i['value'] and 'تیگو' in i['value'].lower():
        self['brand'] = 'چری'
        self['model'] = 'تیگو'
        if '5' in i['value'].lower():
            self['tip'] = '5'
        elif '7' in i['value'].lower():
            self['tip'] = '7'
    elif 'چری' in i['value'] and 'ویانا' in i['value']:
        self['brand'] = 'چری'
        self['model'] = 'ویانا'
        if 'a15' in i['value'].lower():
            self['tip'] = 'A15'
    elif 'چری' in i['value']:
        self['brand'] = 'چری'
        self['model'] = None

    elif 'داتسون' in i['value'] and 'سواری' in i['value']:
        self['brand'] = 'داتسون'
        self['model'] = 'سواری'
    elif 'داتسون' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'داتسون'
        self['model'] = 'وانت'
    elif 'داتسون' in i['value']:
        self['brand'] = 'داتسون'
        self['model'] = None

    elif 'دانگ فنگ' in i['value'] and 'h30' in i['value'].lower() and 'کراس' in i['value']:
        self['brand'] = 'دانگ فنگ'
        self['model'] = 'H30 کراس'
    elif 'دانگ فنگ' in i['value'] and 's30' in i['value'].lower():
        self['brand'] = 'دانگ فنگ'
        self['model'] = 'S30'
    elif 'دانگ فنگ' in i['value']:
        self['brand'] = 'دانگ فنگ'
        self['model'] = None

    elif 'دامای' in i['value'] and 'x7' in i['value'].lower():
        self['brand'] = 'دامای'
        self['model'] = 'X7'
    elif 'دامای' in i['value']:
        self['brand'] = 'دامای'
        self['model'] = None

    elif 'دایون' in i['value'] and 'y5' in i['value'].lower():
        self['brand'] = 'دایون'
        self['model'] = 'Y5'
    elif 'دایون' in i['value']:
        self['brand'] = 'دایون'
        self['model'] = None

    elif 'دایهاتسو' in i['value']:
        self['brand'] = 'دایهاتسو'
        self['model'] = None

    elif 'دلیکا' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'دلیکا'
        self['model'] = 'ون'
    elif 'دلیکا' in i['value']:
        self['brand'] = 'دلیکا'
        self['model'] = None

    elif 'دوج' in i['value'] and 'کرنت' in i['value']:
        self['brand'] = 'دوج'
        self['model'] = 'کرنت'
    elif 'دوج' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'دوج'
        self['model'] = 'ون'
    elif 'دوج' in i['value']:
        self['brand'] = 'دوج'
        self['model'] = None

    elif 'دوو' in i['value'] and 'اسپرو' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = 'اسپرو'
    elif 'دوو' in i['value'] and 'ریسر' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = 'ریسر'
        if 'gte' in i['value'].lower():
            self['tip'] = 'GTE'
        elif 'gti' in i['value'].lower():
            self['tip'] = 'GTI'
        elif 'هاچ' in i['value']:
            self['tip'] = 'هاچبک'
    elif 'دوو' in i['value'] and ('سی یلو' in i['value'] or 'سیلو' in i['value']):
        self['brand'] = 'دوو'
        self['model'] = 'سی یلو'
        if 'هاچ' in i['value']:
            self['tip'] = 'هاچبک'
    elif 'دوو' in i['value'] and 'ماتیز' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = 'ماتیز'
    elif 'دوو' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = None

    elif ('دی‌اس' in i['value'] or 'دی اس' in i['value']) and 'کراس بک' in i['value'].lower():
        self['brand'] = 'دی اس'
        self['model'] = 'کراس بک'
        if '4' in i['value'].lower():
            self['tip'] = '4'
        elif '7' in i['value'] and 'اپرا' in i['value']:
            self['tip'] = '7 اپرا'
        elif '7' in i['value'] and 'ریولی' in i['value']:
            self['tip'] = '7 ریولی'
        elif '7' in i['value']:
            self['tip'] = '7'
    elif ('دی‌اس' in i['value'] or 'دی اس' in i['value']) and '3' in i['value']:
        self['brand'] = 'دی اس'
        self['model'] = '3'
    elif ('دی‌اس' in i['value'] or 'دی اس' in i['value']) and '5ls' in i['value'].lower():
        self['brand'] = 'دی اس'
        self['model'] = '5LS'
    elif ('دی‌اس' in i['value'] or 'دی اس' in i['value']) and '5' in i['value']:
        self['brand'] = 'دی اس'
        self['model'] = '5'
    elif ('دی‌اس' in i['value'] or 'دی اس' in i['value']) and '6' in i['value']:
        self['brand'] = 'دی اس'
        self['model'] = '6'
    elif ('دی‌اس' in i['value'] or 'دی اس' in i['value']):
        self['brand'] = 'دی اس'
        self['model'] = None

    elif 'دیگنیتی' in i['value'] and 'پرایم' in i['value']:
        self['brand'] = 'دیگنیتی'
        self['model'] = 'پرایم'
    elif 'دیگنیتی' in i['value'] and 'پرستیژ' in i['value']:
        self['brand'] = 'دیگنیتی'
        self['model'] = 'پرستیژ'
    elif 'دیگنیتی' in i['value']:
        self['brand'] = 'دیگنیتی'
        self['model'] = None

    elif 'دییر' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'دییر'
        self['model'] = 'وانت'
    elif 'دییر' in i['value']:
        self['brand'] = 'دییر'
        self['model'] = None

    elif 'راین' in i['value'] and 'v5' in i['value'].lower():
        self['brand'] = 'راین'
        self['model'] = 'V5'
    elif 'راین' in i['value']:
        self['brand'] = 'راین'
        self['model'] = None

    elif 'رولزرویس' in i['value']:
        self['brand'] = 'رولزرویس'
        self['model'] = None

    elif 'ریگان' in i['value'] and 'کوپا' in i['value']:
        self['brand'] = 'ریگان'
        self['model'] = 'کوپا'
        if 'اکسکلوسیو' in i['value']:
            self['tip'] = 'اکسکلوسیو'
        elif 'رویال' in i['value']:
            self['tip'] = 'رویال'
        elif 'فلگ شیپ' in i['value']:
            self['tip'] = 'فلگ شیپ'
    elif 'ریگان' in i['value']:
        self['brand'] = 'ریگان'
        self['model'] = None
    
    elif 'زامیاد' in i['value'] and 'کارون' in i['value'].lower():
        self['brand'] = 'زامیاد'
        self['model'] = 'کارون'
    elif 'زامیاد' in i['value'] and 'پادرا' in i['value'].lower():
        self['brand'] = 'زامیاد'
        self['model'] = 'پادرا'
        if 'پلاس' in i['value'].lower():
            self['tip'] = 'پلاس'
    elif 'زامیاد' in i['value'] and 'درکا' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = 'درکا'
    elif 'زامیاد' in i['value'] and 'شوکا' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = 'شوکا'
    elif 'زامیاد' in i['value'] and 'z 24' in i['value'].lower():
        self['brand'] = 'زامیاد'
        self['model'] = 'Z 24'
    elif 'ریچ' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = 'ریچ'
        if 'تک' in i['value']:
            self['tip'] = 'تک کابین'
    elif 'زامیاد' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = None

    elif 'زوتی' in i['value'] and 'z300' in i['value'].lower():
        self['brand'] = 'زوتی'
        self['model'] = 'Z300'
    elif 'زوتی' in i['value']:
        self['brand'] = 'زوتی'
        self['model'] = None

    elif 'سانگ یانگ' in i['value'] and 'اکتیون' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'اکتیون'
    elif 'سانگ یانگ' in i['value'] and 'تیوولی' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'تیوولی'
        if 'ارمور' in i['value'].lower() or 'آرمور' in i['value']:
            self['tip'] = 'ارمور'
        elif 'اسپرت' in i['value'].lower():
            self['tip'] = 'اسپرت'
        elif 'الیت' in i['value'].lower():
            self['tip'] = 'الیت'
        elif 'سولار' in i['value'].lower():
            self['tip'] = 'سولار'
        elif 'فیس 2018' in i['value'].lower():
            self['tip'] = 'فیس 2018'
        elif 'فایتر' in i['value'] and 'توربو' in i['value']:
            self['tip'] = 'فایتر توربو'
        elif 'فایتر' in i['value']:
            self['tip'] = 'فایتر'
        elif 'اسپشیال' in i['value'] and 'توربو' in i['value']:
            self['tip'] = 'اسپشیال توربو'
        elif 'اسپشیال' in i['value']:
            self['tip'] = 'اسپشیال'
    elif 'سانگ یانگ' in i['value'] and 'چیرمن' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'چیرمن'
    elif 'سانگ یانگ' in i['value'] and 'رکستون' in i['value'].lower():
        self['brand'] = 'سانگ یانگ'
        self['model'] = ' رکستون'
        if 'g4' in i['value'].lower():
            self['tip'] = 'G4'
    elif 'سانگ یانگ' in i['value'] and 'رودیوس' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'رودیوس'
    elif 'سانگ یانگ' in i['value'] and 'کایرون' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'کایرون'
    elif 'سانگ یانگ' in i['value'] and 'کوراندو' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'کوراندو'
        if '2300' in i['value']:
            self['tip'] = '2300cc'
        elif '3200' in i['value']:
            self['tip'] = '3200cc'
    elif 'سانگ یانگ' in i['value'] and 'موسو' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'موسو'
        if '2300' in i['value']:
            self['tip'] = '2300cc'
        elif '3200' in i['value']:
            self['tip'] = '3200cc'
    elif 'سانگ یانگ' in i['value'] and 'نیو اکتیون' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'نیو اکتیون'
        if 'کامفورت' in i['value']:
            self['tip'] = 'کامفورت'
        elif 'لاکچری' in i['value']:
            self['tip'] = 'لاکچری'
        elif 'پرستیژ' in i['value']:
            self['tip'] = 'پرستیژ'
    elif 'سانگ یانگ' in i['value'] and 'نیو کوراندو' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'نیو کوراندو'
        if 'پرمیوم' in i['value'] and 'پلاس' in i['value']:
            self['tip'] = 'پرمیوم پلاس'
        elif 'پرمیوم' in i['value']:
            self['tip'] = 'پرمیوم'
    elif 'سانگ یانگ' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = None

    elif 'سئات' in i['value'] and 'لئون' in i['value']:
        self['brand'] = 'سئات'
        self['model'] = 'لئون'
    elif 'سئات' in i['value']:
        self['brand'] = 'سئات'
        self['model'] = None

    elif 'سوئیست' in i['value'] and 'dx 3' in i['value'].lower():
        self['brand'] = 'سوئیست'
        self['model'] = 'DX 3'
    elif 'سوئیست' in i['value']:
        self['brand'] = 'سوئیست'
        self['model'] = None

    elif 'سوبارو' in i['value'] and 'فارستر' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'فارستر'
    elif 'سوبارو' in i['value'] and 'لگاسی' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'لگاسی'
    elif 'سوبارو' in i['value'] and 'وی ویو' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'وی ویو'
    elif 'سوبارو' in i['value'] and 'x7' in i['value'].lower():
        self['brand'] = 'سوبارو'
        self['model'] = 'X7'
    elif 'سوبارو' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'وانت'
    elif 'سوبارو' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = None

    elif 'سیتروئن' in i['value'] and 'زانتیا' in i['value'].lower():
        self['brand'] = 'سیتروئن'
        self['model'] = 'زانتیا'
        if '1800' in i['value'] or '1.8' in i['value']:
            self['tip'] = '1800cc'
        elif '2000' in i['value'] or '2.0' in i['value']:
            self['tip'] = '2000cc'
        elif '2' in i['value']:
            self['tip'] = '2000cc'
    elif 'سیتروئن' in i['value'] and 'ژیان' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = 'ژیان'
    elif 'سیتروئن' in i['value'] and 'c3' in i['value'].lower():
        self['brand'] = 'سیتروئن'
        self['model'] = 'C3'
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
    elif 'سیتروئن' in i['value'] and 'c5' in i['value'].lower():
        self['brand'] = 'سیتروئن'
        self['model'] = 'C5'
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
    elif 'سیتروئن' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = None

    elif 'سیناد' in i['value']:
        self['brand'] = 'سیناد'
        self['model'] = None

    elif 'شاهین' in i['value'] and 'g' in i['value'].lower():
        self['brand'] = 'شاهین'
        self['model'] = 'G'
    elif 'شاهین' in i['value']:
        self['brand'] = 'شاهین'
        self['model'] = None

    elif 'شورولت' in i['value'] and 'ایمپالا' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'ایمپالا'
    elif 'شورولت' in i['value'] and 'بلر' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'بلر'
    elif 'شورولت' in i['value'] and 'بلیزر' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'بلیزر'
    elif 'شورولت' in i['value'] and 'رویال' in i['value'].lower():
        self['brand'] = 'شورولت'
        self['model'] = 'رویال '
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
    elif 'شورولت' in i['value'] and 'سابربن' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'سابربن'
    elif 'شورولت' in i['value'] and 'فلیت' in i['value'].lower():
        self['brand'] = 'شورولت'
        self['model'] = 'فلیت '
        if 'مستر' in i['value']:
            self['tip'] = 'مستر'
    elif 'شورولت' in i['value'] and 'کاپریس' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'کاپریس'
    elif 'شورولت' in i['value'] and 'کامارو' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'کامارو'
    elif 'شورولت' in i['value'] and 'مونت کارلو' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'مونت کارلو'
    elif 'شورولت' in i['value'] and 'نوا' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'نوا'
    elif 'شورولت' in i['value'] and 'نوا' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'نوا '
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
    elif 'شورولت' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'وانت'
    elif 'شورولت' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'ون'
    elif 'شورولت' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = None

    elif 'فردا' in i['value'] and '511' in i['value']:
        self['brand'] = 'فردا'
        self['model'] = '511'
    elif 'فردا' in i['value'] and 'sx5' in i['value'].lower():
        self['brand'] = 'فردا'
        self['model'] = 'Sx5'
    elif 'فردا' in i['value'] and 'sx6' in i['value'].lower():
        self['brand'] = 'فردا'
        self['model'] = 'Sx6'
    elif 'فردا' in i['value'] and 't5' in i['value'].lower():
        self['brand'] = 'فردا'
        self['model'] = 'T5'
    elif 'فردا' in i['value']:
        self['brand'] = 'فردا'
        self['model'] = None

    elif 'فوتون' in i['value'] and 'ساوانا' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = 'ساوانا'
    elif 'فوتون' in i['value'] and 'تونلند' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = 'تونلند'
    elif 'فوتون' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = 'وانت'
    elif 'فوتون' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = 'ون'
    elif 'فوتون' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = None

    elif 'فورد' in i['value'] and 'تاروس' in i['value']:
        self['brand'] = 'فورد'
        self['model'] = 'تاروس'
    elif 'فورد' in i['value'] and 'موستانگ' in i['value']:
        self['brand'] = 'فورد'
        self['model'] = 'موستانگ'
    elif 'فورد' in i['value'] and 'F150' in i['value']:
        self['brand'] = 'فورد'
        self['model'] = 'F150'
    elif 'فورد' in i['value']:
        self['brand'] = 'فورد'
        self['model'] = None

    elif 'فولکس' in i['value'] and 'بیتل' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'بیتل'
    elif 'فولکس' in i['value'] and 'پاسات' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'پاسات'
    elif 'فولکس' in i['value'] and 'تیگوان' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'تیگوان'
    elif 'فولکس' in i['value'] and 'کدی' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'کدی'
    elif 'فولکس' in i['value'] and 'گل' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'گل'
    elif 'فولکس' in i['value'] and 'گلف' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'گلف'
    elif 'فولکس' in i['value'] and 'ترنسپورتر' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'ترنسپورتر'
    elif 'فولکس' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'وانت'
    elif 'فولکس' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'ون'
    elif 'فولکس' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = None

    elif 'فونیکس' in i['value'] and 'آریزو 6 پرو' in i['value']:
        self['brand'] = 'فونیکس'
        self['model'] = 'آریزو 6 پرو'
    elif 'فونیکس' in i['value'] and 'تیگو 7 پرو' in i['value']:
        self['brand'] = 'فونیکس'
        self['model'] = 'تیگو 7 پرو'
    elif 'فونیکس' in i['value'] and 'تیگو 8 پرو' in i['value']:
        self['brand'] = 'فونیکس'
        self['model'] = 'تیگو 8 پرو'
    elif 'فونیکس' in i['value']:
        self['brand'] = 'فونیکس'
        self['model'] = None

    elif 'فیات' in i['value'] and '500' in i['value']:
        self['brand'] = 'فیات'
        self['model'] = '500'
    elif 'فیات' in i['value'] and 'سی ینا' in i['value']:
        self['brand'] = 'فیات'
        self['model'] = 'سی ینا'
    elif 'فیات' in i['value']:
        self['brand'] = 'فیات'
        self['model'] = None
        
    elif 'ریسپکت' in i['value'] and 'پرایم' in i['value']:
        self['brand'] = 'ریسپکت'
        self['model'] = 'پرایم'
    elif 'ریسپکت' in i['value'] and 'پرایم' in i['value']:
        self['brand'] = 'ریسپکت'
        self['model'] = None

    elif 'فیدلیتی' in i['value'] and 'پرایم' in i['value']:
        self['brand'] = 'فیدلیتی'
        self['model'] = 'پرایم'
    elif 'فیدلیتی' in i['value']:
        self['brand'] = 'فیدلیتی'
        self['model'] = None

    elif 'کاپرا' in i['value'] and '2' in i['value']:
        self['brand'] = 'کاپرا'
        self['model'] = '2'
    elif 'کاپرا' in i['value'] and 'تک کابین' in i['value']:
        self['brand'] = 'کاپرا'
        self['model'] = 'تک کابین'
    elif 'کاپرا' in i['value'] and 'دو کابین' in i['value']:
        self['brand'] = 'کاپرا'
        self['model'] = 'دو کابین'
    elif 'کاپرا' in i['value']:
        self['brand'] = 'کاپرا'
        self['model'] = None

    elif 'کرایسلر' in i['value']:
        self['brand'] = 'کرایسلر'
        self['model'] = None

    elif 'کوییک' in i['value'] and 'اتوماتیک' in i['value']:
        self['brand'] = 'کوییک'
        self['model'] = 'اتوماتیک'
    elif 'کوییک' in i['value'] and ('دنده‌' in i['value'] or 'دنده' in i['value']): #this two دنده not similar!
        self['brand'] = 'کوییک'
        self['model'] = 'دنده‌ای'
        if 's' in i['value'].lower():
            self['tip'] = 'S'
    elif 'کوییک' in i['value']:
        self['brand'] = 'کوییک'
        self['model'] = None

    elif ('کی‌ام‌سی' in i['value'] or 'کی ام سی' in i['value']) and 'k7' in i['value'].lower():
        self['brand'] = 'کی‌ام‌سی'
        self['model'] = 'K7'
    elif ('کی‌ام‌سی' in i['value'] or 'کی ام سی' in i['value']) and 'j7' in i['value'].lower():
        self['brand'] = 'کی‌ام‌سی'
        self['model'] = 'J7'
    elif ('کی‌ام‌سی' in i['value'] or 'کی ام سی' in i['value']) and 't8' in i['value'].lower():
        self['brand'] = 'کی‌ام‌سی'
        self['model'] = 'T8'
    elif 'کی‌ام‌سی' in i['value']:
        self['brand'] = 'کی‌ام‌سی'
        self['model'] = None

    elif 'گریت وال' in i['value'] and 'وینگل' in i['value'].lower():
        self['brand'] = 'گریت وال'
        self['model'] = 'وینگل'
        if '3' in i['value']:
            self['tip'] = '3'
        elif 'تک کابین 5 ' in i['value'].lower():
            self['tip'] = 'تک کابین 5 '
        elif 'دو کابین 5' in i['value'].lower():
            self['tip'] = 'دو کابین 5'
    elif 'گریت وال' in i['value'] and 'هاوال' in i['value'].lower():
        self['brand'] = 'گریت وال'
        self['model'] = 'هاوال'
        if 'h2' in i['value'].lower():
            self['tip'] = 'H2'
        elif 'h6' in i['value'].lower():
            self['tip'] = 'H6'
        elif 'm4' in i['value'].lower():
            self['tip'] = 'M4'
    elif 'گریت وال' in i['value'] and 'c30' in i['value'].lower():
        self['brand'] = 'گریت وال'
        self['model'] = 'C30'
    elif 'گریت وال' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'گریت وال'
        self['model'] = 'ون'
    elif 'گریت وال' in i['value']:
        self['brand'] = 'گریت وال'
        self['model'] = None

    elif 'لادا' in i['value'] and 'نیوا' in i['value']:
        self['brand'] = 'لادا'
        self['model'] = 'نیوا'
    elif 'لادا' in i['value']:
        self['brand'] = 'لادا'
        self['model'] = None

    elif 'لاماری' in i['value'] and 'ایما' in i['value']:
        self['brand'] = 'لاماری'
        self['model'] = 'ایما'
    elif 'لاماری' in i['value']:
        self['brand'] = 'لاماری'
        self['model'] = None

    elif 'لامبورگینی' in i['value']:
        self['brand'] = 'لامبورگینی'
        self['model'] = None
        
    elif 'لینکلن' in i['value'] and 'کنتینانتال' in i['value']:
        self['brand'] = 'لینکلن'
        self['model'] = 'کنتینانتال'    
    elif 'لینکلن' in i['value']:
        self['brand'] = 'لینکلن'
        self['model'] = None
    
    elif 'اینفینیتی' in i['value'] and 'qx80' in i['value'].lower():
        self['brand'] = 'اینفینیتی'
        self['model'] = 'QX80'
    elif 'اینفینیتی' in i['value']:
        self['brand'] = 'اینفینیتی'
        self['model'] = None

    elif 'لکسوس' in i['value'] and 'ct' in i['value'].lower():
        self['brand'] = 'لکسوس'
        self['model'] = 'CT'
    elif 'لکسوس' in i['value'] and 'es' in i['value'].lower():
        self['brand'] = 'لکسوس'
        self['model'] = 'ES'
    elif 'لکسوس' in i['value'] and 'gs' in i['value'].lower():
        self['brand'] = 'لکسوس'
        self['model'] = 'GS'
    elif 'لکسوس' in i['value'] and 'is' in i['value'].lower():
        self['brand'] = 'لکسوس'
        self['model'] = 'IS'
    elif 'لکسوس' in i['value'] and 'ls' in i['value'].lower():
        self['brand'] = 'لکسوس'
        self['model'] = 'LS'
    elif 'لکسوس' in i['value'] and 'lx' in i['value'].lower():
        self['brand'] = 'لکسوس'
        self['model'] = 'LX'
    elif 'لکسوس' in i['value'] and 'nx' in i['value'].lower():
        self['brand'] = 'لکسوس'
        self['model'] = 'NX'
        if '200' in i['value'] and 't' in i['value'].lower():
            self['tip'] = '200t'
        elif '300' in i['value'] and 'h' in i['value'].lower():
            self['tip'] = '300 H'
    elif 'لکسوس' in i['value'] and 'RX' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'RX'
    elif 'لکسوس' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = None

    elif 'لندروز' in i['value'] and 'دیسکاوری' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'دیسکاوری'
    elif 'لندروز' in i['value'] and 'دیفندر' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'دیفندر'
    elif 'لندروز' in i['value'] and 'رنجرور' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'رنجرور'
    elif 'لندروز' in i['value'] and 'رنجرور' in i['value'].lower():
        self['brand'] = 'لندروز'
        self['model'] = 'رنجرور'
        if 'ایووک' in i['value'].lower():
            self['tip'] = 'ایووک'
    elif 'لندروز' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'مونتاژ'
    elif 'لندروز' in i['value'] and 'فریلندر' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'فریلندر'
    elif 'لندروز' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = None

    elif 'لندمارک' in i['value'] and 'V7' in i['value']:
        self['brand'] = 'لندمارک'
        self['model'] = 'V7'
    elif 'لندمارک' in i['value']:
        self['brand'] = 'لندمارک'
        self['model'] = None

    elif 'لوتوس' in i['value'] and 'الیزه' in i['value']:
        self['brand'] = 'لوتوس'
        self['model'] = 'الیزه'
    elif 'لوتوس' in i['value']:
        self['brand'] = 'لوتوس'
        self['model'] = None

    elif 'لوکسیژن' in i['value'] and 'U6' in i['value']:
        self['brand'] = 'لوکسیژن'
        self['model'] = 'U6'
    elif 'لوکسیژن' in i['value']:
        self['brand'] = 'لوکسیژن'
        self['model'] = None

    elif 'مازراتی' in i['value'] and 'کواتروپورته' in i['value']:
        self['brand'] = 'مازراتی'
        self['model'] = 'کواتروپورته'
    elif 'مازراتی' in i['value'] and 'گرن' in i['value'].lower():
        self['brand'] = 'مازراتی'
        self['model'] = 'گرن'
        if 'توریسمو' in i['value'].lower():
            self['tip'] = 'توریسمو'
    elif 'مازراتی' in i['value'] and 'گرن' in i['value'].lower():
        self['brand'] = 'مازراتی'
        self['model'] = 'گرن'
        if 'کبریو' in i['value'].lower():
            self['tip'] = 'کبریو'
    elif 'مازراتی' in i['value'] and 'گیبلی' in i['value']:
        self['brand'] = 'مازراتی'
        self['model'] = 'گیبلی'
    elif 'مازراتی' in i['value']:
        self['brand'] = 'مازراتی'
        self['model'] = None
    
    elif 'مزدا' in i['value'] and 'کارا' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = 'کارا'
        if 'تک' in i['value']:
            self['tip'] = 'تک کابین'
        elif 'دو' in i['value']:
            self['tip'] = 'دوکابین'
    elif 'مزدا' in i['value'] and '323' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '323'
    elif 'مزدا' in i['value'] and '3n' in i['value'].lower():
        self['brand'] = 'مزدا'
        self['model'] = '3N'
        if 'صندوق دار مونتاژ' in i['value'].lower():
            self['tip'] = 'صندوق دار مونتاژ'
        if 'هاچبک مونتاژ' in i['value'].lower():
            self['tip'] = 'هاچبک مونتاژ'
    elif 'مزدا' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = 'وانت'
    elif 'مزدا' in i['value'] and '2' in i['value'].lower():
        self['brand'] = 'مزدا'
        self['model'] = '2'
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
    elif 'مزدا' in i['value'] and '3' in i['value'].lower():
        self['brand'] = 'مزدا'
        self['model'] = '3'
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
    elif 'مزدا' in i['value'] and '6' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '6'
    elif 'مزدا' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = None

    elif 'کارا' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = 'کارا'
        if 'تک' in i['value']:
            self['tip'] = 'تک کابین'
        elif 'دو' in i['value']:
            self['tip'] = 'دوکابین'

    elif 'مکث موتور' in i['value'] and 'کلوت' in i['value']:
        self['brand'] = 'مکث موتور'
        self['model'] = 'کلوت'
    elif 'مکث موتور' in i['value']:
        self['brand'] = 'مکث موتور'
        self['model'] = None

    elif 'مکسوس' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'مکسوس'
        self['model'] = 'ون'
    elif 'مکسوس' in i['value']:
        self['brand'] = 'مکسوس'
        self['model'] = None

    elif 'میتسوبیشی' in i['value'] and 'اوتلندر' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'اوتلندر'
    elif 'میتسوبیشی' in i['value'] and 'اوتلندر' in i['value'] and 'PHEV' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'اوتلندر'
        if 'phev' in i['value'].lower():
            self['tip'] = 'phev'
    elif 'میتسوبیشی' in i['value'] and 'پاجرو' in i['value'].lower():
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'پاجرو '
        if '2 در' in i['value'].lower():
            self['tip'] = '2 در'
    elif 'میتسوبیشی' in i['value'] and 'پاجرو' in i['value'].lower():
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'پاجرو '
        if '4 در' in i['value'].lower():
            self['tip'] = '4 در'
    elif 'میتسوبیشی' in i['value'] and 'پاجرو' in i['value'].lower():
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'پاجرو '
        if 'مونتاژ' in i['value'].lower():
            self['tip'] = 'مونتاژ'
    elif 'میتسوبیشی' in i['value'] and 'گالانت' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'گالانت'
    elif 'میتسوبیشی' in i['value'] and 'لنسر' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'لنسر'
    elif 'میتسوبیشی' in i['value'] and 'میراژ' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'میراژ'
    elif 'میتسوبیشی' in i['value'] and 'ASX' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'ASX'
    elif 'میتسوبیشی' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'وانت'
    elif 'میتسوبیشی' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'ون'
    elif 'میتسوبیشی' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = None

    elif 'مینی' in i['value'] and 'کانتری من' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = 'کانتری من'
    elif 'مینی' in i['value'] and 'کلاب من' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = 'کلاب من'
    elif 'مینی' in i['value'] and 'کلاسیک' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = 'کلاسیک'
    elif 'مینی' in i['value'] and 's' in i['value'].lower():
        self['brand'] = 'مینی'
        self['model'] = 'S'
        if 'کوپر' in i['value']:
            self['tip'] = 'کوپر'
    elif 'مینی' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = None

    elif 'نیسان' in i['value'] and 'آلتیما' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'آلتیما'
    elif 'نیسان' in i['value'] and 'ایکس تریل' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'ایکس تریل'
    elif 'نیسان' in i['value'] and 'پاترول' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'پاترول'
        if '4 در' in i['value']:
            self['tip'] = '4 در'
        elif '2 در' in i['value']:
            self['tip'] = '2 در'
    elif 'نیسان' in i['value'] and 'پت فایندر' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'پت فایندر'
    elif 'نیسان' in i['value'] and 'تی ینا' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'تی ینا'
    elif 'نیسان' in i['value'] and 'تیدا' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'تیدا'
    elif 'نیسان' in i['value'] and 'جوک' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'جوک'
    elif 'نیسان' in i['value'] and 'رونیز' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'رونیز'
    elif 'نیسان' in i['value'] and 'سانی' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'سانی'
    elif 'نیسان' in i['value'] and 'سرانزا' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'سرانزا'
    elif 'نیسان' in i['value'] and 'قشقایی' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'قشقایی'
    elif 'نیسان' in i['value'] and 'ماکسیما' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'ماکسیما'
    elif 'نیسان' in i['value'] and 'مورانو' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'مورانو'
    elif 'نیسان' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'وانت'
    elif 'نیسان' in i['value'] and 'پیکاپ' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'وانت'
    elif 'نیسان' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = None

    elif 'ولوو' in i['value'] and 'C30' in i['value']:
        self['brand'] = 'ولوو'
        self['model'] = 'C30'
    elif 'ولوو' in i['value'] and 'C70' in i['value']:
        self['brand'] = 'ولوو'
        self['model'] = 'C70'
    elif 'ولوو' in i['value'] and 'V40' in i['value']:
        self['brand'] = 'ولوو'
        self['model'] = 'V40'
    elif 'ولوو' in i['value'] and 'XC60' in i['value']:
        self['brand'] = 'ولوو'
        self['model'] = 'XC60'
    elif 'ولوو' in i['value'] and 'XC90' in i['value']:
        self['brand'] = 'ولوو'
        self['model'] = 'XC90'
    elif 'ولوو' in i['value']:
        self['brand'] = 'ولوو'
        self['model'] = None

    elif 'ون ایران خودرو' in i['value'] and 'غزال' in i['value']:
        self['brand'] = 'ون ایران خودرو'
        self['model'] = 'غزال'
    elif 'ون ایران خودرو' in i['value'] and 'وانا' in i['value']:
        self['brand'] = 'ون ایران خودرو'
        self['model'] = 'وانا'
    elif 'ون ایران خودرو' in i['value']:
        self['brand'] = 'ون ایران خودرو'
        self['model'] = None

    elif 'ون سایپا' in i['value'] and 'کاروان' in i['value']:
        self['brand'] = 'ون سایپا'
        self['model'] = 'کاروان'
    elif 'ون سایپا' in i['value']:
        self['brand'] = 'ون سایپا'
        self['model'] = None

    elif 'ون فاو' in i['value'] and 'سیبا' in i['value']:
        self['brand'] = 'ون فاو'
        self['model'] = 'سیبا'
    elif 'ون فاو' in i['value']:
        self['brand'] = 'ون فاو'
        self['model'] = None

    elif 'ون نارون' in i['value'] and 'تاکسی' in i['value']:
        self['brand'] = 'ون نارون'
        self['model'] = 'تاکسی'
    elif 'ون نارون' in i['value'] and 'شخصی' in i['value']:
        self['brand'] = 'ون نارون'
        self['model'] = 'شخصی'
    elif 'ون نارون' in i['value']:
        self['brand'] = 'ون نارون'
        self['model'] = None

    elif 'هافی لوبو' in i['value'] and 'لوبو' in i['value']:
        self['brand'] = 'هافی لوبو'
        self['model'] = 'لوبو'
    elif 'هافی لوبو' in i['value']:
        self['brand'] = 'هافی لوبو'
        self['model'] = None

    elif 'هامر' in i['value'] and 'H2' in i['value']:
        self['brand'] = 'هامر'
        self['model'] = 'H2'
    elif 'هامر' in i['value']:
        self['brand'] = 'هامر'
        self['model'] = None

    elif 'هاوال' in i['value'] and 'h2' in i['value'].lower():
        self['brand'] = 'هاوال'
        self['model'] = 'H2'
    elif 'هاوال' in i['value'] and 'h6' in i['value'].lower():
        self['brand'] = 'هاوال'
        self['model'] = 'H6'
    elif 'هاوال' in i['value'] and 'h9' in i['value'].lower():
        self['brand'] = 'هاوال'
        self['model'] = 'H9'
    elif 'هاوال' in i['value'] and 'm4' in i['value'].lower():
        self['brand'] = 'هاوال'
        self['model'] = 'M4'
    elif 'هاوال' in i['value']:
        self['brand'] = 'هاوال'
        self['model'] = None

    elif 'هن تنگ' in i['value'] and 'X5 مونتاژ' in i['value']:
        self['brand'] = 'هن تنگ'
        self['model'] = 'X5 مونتاژ'
    elif 'هن تنگ' in i['value'] and 'X7 مونتاژ' in i['value']:
        self['brand'] = 'هن تنگ'
        self['model'] = 'X7 مونتاژ'
    elif 'هن تنگ' in i['value']:
        self['brand'] = 'هن تنگ'
        self['model'] = None

    elif 'هوندا' in i['value'] and 'آکورد' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = 'آکورد'
    elif 'هوندا' in i['value'] and 'سیویک' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = 'سیویک'
    elif 'هوندا' in i['value'] and 'لجند' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = 'لجند'
    elif 'هوندا' in i['value'] and ('cr-v' in i['value'].lower() or 'c-rv' in i['value'].lower()):
        self['brand'] = 'هوندا'
        self['model'] = 'CRV'
    elif 'هوندا' in i['value'] and ('cr-x' in i['value'].lower() or 'c-rx' in i['value'].lower()):
        self['brand'] = 'هوندا'
        self['model'] = 'CRX'
    elif 'هوندا' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = None

    elif 'هیلمن' in i['value']:
        self['brand'] = 'هیلمن'
        self['model'] = None

    elif 'هیوسو' in i['value'] and 'T205' in i['value']:
        self['brand'] = 'هیوسو'
        self['model'] = 'T205'
    elif 'هیوسو' in i['value']:
        self['brand'] = 'هیوسو'
        self['model'] = None

    elif 'یوآز' in i['value'] and 'پاتریوت' in i['value']:
        self['brand'] = 'یوآز'
        self['model'] = 'پاتریوت'
    elif 'یوآز' in i['value'] and 'پیکاپ' in i['value']:
        self['brand'] = 'یوآز'
        self['model'] = 'پیکاپ'
    elif 'یوآز' in i['value']:
        self['brand'] = 'یوآز'
        self['model'] = None

    elif 'بنز' in i['value'] and 'cla' in i['value'].lower() and 'کلاس' in i['value']: 
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CLA'
    elif 'بنز' in i['value'] and 'clk' in i['value'].lower() and 'کلاس' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CLK'
    elif 'بنز' in i['value'] and 'cls' in i['value'].lower() and 'کلاس' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CLS'
    elif 'بنز' in i['value'] and 'cl' in i['value'].lower() and 'کلاس' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CL'
    elif 'بنز' in i['value'] and 'gla' in i['value'].lower():
        self['brand'] = 'بنز'
        self['model'] = 'GLA'
    elif 'بنز' in i['value'] and 'glk' in i['value'].lower():
        self['brand'] = 'بنز'
        self['model'] = 'GLK'
    elif 'بنز' in i['value'] and 'ml' in i['value'].lower():
        self['brand'] = 'بنز'
        self['model'] = 'ML'
    elif 'بنز' in i['value'] and 'slc' in i['value'].lower():
        self['brand'] = 'بنز'
        self['model'] = 'SLC'
    elif 'بنز' in i['value'] and 'slk' in i['value'].lower():
        self['brand'] = 'بنز'
        self['model'] = 'SLK'
    elif 'بنز' in i['value'] and 'sl' in i['value'].lower():
        self['brand'] = 'بنز'
        self['model'] = 'SL'
    elif 'بنز' in i['value'] and 'کلاسیک' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاسیک'
    elif 'بنز' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'ون'
    elif 'بنز' in i['value'] and 'a' in i['value'].lower() and 'کلاس' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس A'
    elif 'بنز' in i['value'] and 'b' in i['value'].lower() and 'کلاس' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس B'
    elif 'بنز' in i['value'] and 'c' in i['value'].lower() and 'کلاس' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس C'
    elif 'بنز' in i['value'] and 's' in i['value'].lower():
        self['brand'] = 'بنز'
        self['model'] = 'S'
    elif 'بنز' in i['value'] and 'e' in i['value'].lower() and 'کلاس' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس E'
    elif 'بنز' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = None

    else:
        self['brand'] = "not_defined"
        self['model'] = "not_defined"
