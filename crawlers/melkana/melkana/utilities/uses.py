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
    #pride 111
    if 'پراید' in i['value'] and '111' in i['value'] and 'ex' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '111 EX'
    elif 'پراید' in i['value'] and '111' in i['value'] and 'se' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '111 SE'
    elif 'پراید' in i['value'] and '111' in i['value'] and 'sl' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '111 EX'
    elif 'پراید' in i['value'] and '111' in i['value'] and 'sx' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '111 SX'   
    elif 'پراید' in i['value'] and '111' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = '111 ساده'
    #pride 131
    elif 'پراید' in i['value'] and '131' in i['value'] and 'ex' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '131 EX'
    elif 'پراید' in i['value'] and '131' in i['value'] and 'se' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '131 SE'
    elif 'پراید' in i['value'] and '131' in i['value'] and 'sl' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '131 SL'
    elif 'پراید' in i['value'] and '131' in i['value'] and 'sx' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '131 SX' 
    elif 'پراید' in i['value'] and '131' in i['value'] and 'le' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '131 LE'
    elif 'پراید' in i['value'] and '131' in i['value'] and 'tl' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '131 TL'
    elif 'پراید' in i['value'] and '131' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = '131 ساده'   
    #pride 132
    elif 'پراید' in i['value'] and '132' in i['value'] and 'ex' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '132 EX'
    elif 'پراید' in i['value'] and '132' in i['value'] and 'se' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '132 SE'
    elif 'پراید' in i['value'] and '132' in i['value'] and 'sl' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '132 SL'
    elif 'پراید' in i['value'] and '132' in i['value'] and 'sx' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '132 SX'   
    elif 'پراید' in i['value'] and '132' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = '132 ساده'
    #pride 141
    elif 'پراید' in i['value'] and '141' in i['value'] and 'ex' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '141 EX'
    elif 'پراید' in i['value'] and '141' in i['value'] and 'se' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '141 SE'
    elif 'پراید' in i['value'] and '141' in i['value'] and 'sx' in i['value'].lower():
        self['brand'] = 'پراید'
        self['model'] = '141 SX'  
    elif 'پراید' in i['value'] and '141' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = '141 ساده'
    elif 'پراید' in i['value'] and 'صندوق‌دار' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'صندوق‌دار'
    elif 'پراید' in i['value'] and 'هاچبک' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'هاچبک'
    elif ('وانت' in i['value'] or '151' in i['value']) and 'پراید' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'وانت'
    #pride others
    elif 'پراید' in i['value'] and 'اتوماتیک' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'سایر مدل‌ها'
    elif 'پراید' in i['value'] and 'سفری' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'سایر مدل‌ها'
    elif 'پراید' in i['value']:
        self['brand'] = 'پراید'
        self['model'] = 'سایر مدل‌ها'

    #tiba with box
    elif 'تیبا' in i['value'] and 'صندوق‌دار' in i['value'] and 'پلاس' in i['value']:
        self['brand'] = 'تیبا'
        self['model'] = 'صندوق دار پلاس'
    elif 'تیبا' in i['value'] and 'صندوق‌دار' in i['value'] and 'ex' in i['value'].lower():
        self['brand'] = 'تیبا'
        self['model'] = 'صندوق دار EX'
    elif 'تیبا' in i['value'] and 'صندوق‌دار' in i['value'] and 'lx' in i['value'].lower():
        self['brand'] = 'تیبا'
        self['model'] = 'صندوق دار LX'
    elif 'تیبا' in i['value'] and 'صندوق‌دار' in i['value'] and 'sx' in i['value'].lower():
        self['brand'] = 'تیبا'
        self['model'] = 'صندوق دار SX'
    elif 'تیبا' in i['value'] and 'صندوق‌دار' in i['value'] or 'تیبا' in i['value'] and '1' in i['value']:
        self['brand'] = 'تیبا'
        self['model'] = 'صندوق دار ساده'

    #tiba without box
    elif 'تیبا' in i['value'] and 'هاچبک' in i['value'] and 'پلاس' in i['value']:
        self['brand'] = 'تیبا'
        self['model'] = 'هاچ بک پلاس'
    elif 'تیبا' in i['value'] and 'هاچبک' in i['value'] and 'ex' in i['value'].lower():
        self['brand'] = 'تیبا'
        self['model'] = 'هاچ بک EX'
    elif 'تیبا' in i['value'] and 'هاچبک' in i['value'] and 'sx' in i['value'].lower():
        self['brand'] = 'تیبا'
        self['model'] = 'هاچ بک SX'
    elif 'تیبا' in i['value'] and 'هاچبک' in i['value'] or 'تیبا' in i['value'] and '2' in i['value']:
        self['brand'] = 'تیبا'
        self['model'] = 'هاچ بک ساده'
    elif 'تیبا' in i['value']:
        self['brand'] = 'تیبا'
        self['model'] = '‌سایر مدل‌ها'

    #ario
    elif 'آریو' in i['value'] and 'اتوماتیک' in i['value'] and '1600cc' in i['value']:
        self['brand'] = 'آریو'
        self['model'] = 'اتوماتیک'
    elif 'دنده‌ای' in i['value'] and '1500cc' in i['value']:
        self['brand'] = 'آریو'
        self['model'] = 'دنده ای'
    elif 'دنده‌ای' in i['value'] and '1600cc' in i['value']:
        self['brand'] = 'آریو'
        self['model'] = 'دنده ای'
    elif 'آریو' in i['value']:
        self['brand'] = 'آریو'
        self['model'] = 'سایر مدل‌ها'

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
        self['model'] = 'سایر مدل‌ها'

    elif 'ام وی ام' in i['value'] and '110' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '110'
    elif 'ام وی ام' in i['value'] and '110s' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = '110S'
    elif 'ام وی ام' in i['value'] and '315' in i['value'] and 'صندوق‌دار' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '315 صندوق‌دار'
    elif 'ام وی ام' in i['value'] and '315' in i['value'] and 'هاچبک' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '315 هاچبک'
    elif 'ام وی ام' in i['value'] and '315' in i['value'] and 'هاچبک پلاس' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '315 هاپبک پلاس'
    elif 'ام وی ام' in i['value'] and '530' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '530'
    elif 'ام وی ام' in i['value'] and '550' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '550'
    elif 'ام وی ام' in i['value'] and 'x33' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = 'X33'
    elif 'ام وی ام' in i['value'] and 'x22' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = 'X22'
    elif 'ام وی ام' in i['value'] and 'x22 pro' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = 'X22 Pro'
    elif 'ام وی ام' in i['value'] and 'x33' in i['value'] and 's' in i['value'].lower():
        self['brand'] = 'ام وی ام'
        self['model'] = 'X33 S'
    elif 'ام‌وی‌ام' in i['value'] and 'x55' in i['value'].lower() and 'اکسلنت' in i['value'].lower():
        self['brand'] = 'ام‌وی‌ام'
        self['model'] = 'X55 اکسلنت'
    elif 'ام وی ام' in i['value'] and 'X55 Pro' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = 'X55 Pro'
    elif 'ام وی ام' in i['value']:
        self['brand'] = 'ام وی ام'
        self['model'] = '‌سایر مدل‌ها'

    elif 'پژو' in i['value'] and '2008' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '2008'
    elif 'پژو' in i['value'] and '205' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '205'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'تیپ ۱' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 تیپ ۱'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'تیپ ۲' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 تیپ ۲'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'تیپ ۳' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 تیپ ۳'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'تیپ ۴' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 تیپ ۴'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'تیپ ۵' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 تیپ ۵'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'تیپ ۶' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 تیپ ۶'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower() and 'v1' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD V1'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower() and 'v10' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD V10'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower() and 'v19' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD V19'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower() and 'v2' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD V2'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower() and 'v20' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD V20'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower() and 'v6' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD V6'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower() and 'v8' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD V8'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower() and 'v9' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD V9'
    elif 'پژو' in i['value'] and '206' in i['value'].lower() and 'sd' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '206 SD ساده'
    elif 'پژو' in i['value'] and '207' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '207'
    elif 'پژو' in i['value'] and '207' in i['value'].lower() and  'mc' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '207 MC'
    elif 'پژو' in i['value'] and '207' in i['value'].lower() and 'پانوراما' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '207 پانوراما'
    elif 'پژو' in i['value'] and '207' in i['value'].lower() and 'دنده‌ای' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '207 ساده'
    elif 'پژو' in i['value'] and '207' in i['value'].lower() and 'sd' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '207 SD'
    elif 'پژو' in i['value'] and '301' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '301'
    elif 'پژو' in i['value'] and '404' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '404'
    elif 'پژو' in i['value'] and '405' in i['value'].lower() and 'استیشن' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '405 استیشن'
    elif 'پژو' in i['value'] and '405' in i['value'].lower() and 'glx' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '405 GLX'
    elif 'پژو' in i['value'] and '405' in i['value'].lower() and 'gl' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '405 GL'
    elif 'پژو' in i['value'] and '405' in i['value'].lower() and 'gli' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '405 GLi'
    elif 'پژو' in i['value'] and '405' in i['value'].lower() and 'slx' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = '405 SLX'
    elif 'پژو' in i['value'] and '405':
        self['brand'] = 'پژو'
        self['model'] = '405 GLX'
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
    elif 'پژو' in i['value'] and 'پارس' in i['value'].lower() and 'lx' in i['value'].lower() and 'tu5' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = 'پارس LX TU5'
    elif 'پژو' in i['value'] and 'پارس' in i['value'].lower() and 'xu7p' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = 'پارس XU7P'
    elif 'پژو' in i['value'] and 'پارس' in i['value'].lower() and 'elx' in i['value'].lower():
        self['brand'] = 'پژو'
        self['model'] = 'پارس ELX'
    elif 'پژو' in i['value'] and 'پارس' in i['value'] and 'لیموزین' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = 'پارس لیموزین'
    elif 'پژو' in i['value'] and 'پارس' in i['value']:
        self['brand'] = 'پژو'
        self['model'] =  'پارس ساده'
    elif 'پژو' in i['value'] and 'روآ' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = 'روآ'
    elif 'پژو' in i['value'] and 'روآ' in i['value'] and 'سال' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = 'روآ'
    elif 'پژو' in i['value'] and 'RD' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = 'RD'
    elif 'پژو' in i['value'] and 'RDI' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = 'RDI'
    elif 'پژو' in i['value']:
        self['brand'] = 'پژو'
        self['model'] = '‌سایر مدل‌ها'

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
        self['model'] = '‌سایر مدل‌ها'

    elif 'رانا' in i['value'] and 'پلاس' in i['value'] and 'پانوراما' in i['value']:
        self['brand'] = 'رانا'
        self['model'] = 'پلاس پانوراما'
    elif 'رانا' in i['value'] and 'پلاس' in i['value'].lower():
        self['brand'] = 'رانا'
        self['model'] = 'پلاس'
    elif 'رانا' in i['value'] and 'el' in i['value'].lower():
        self['brand'] = 'رانا'
        self['model'] = 'EL'
    elif 'رانا' in i['value'] and 'lx' in i['value'].lower():
        self['brand'] = 'رانا'
        self['model'] = 'LX'
    elif 'رانا' in i['value']:
        self['brand'] = 'رانا'
        self['model'] = 'سایر مدل ها'

    elif 'سمند' in i['value'] and 'سریر' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = 'سریر'
    elif 'سمند' in i['value'] and 'سورن' in i['value'] and 'معمولی' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = 'سورن معمولی'
    elif 'سمند' in i['value'] and 'سورن' in i['value'] and 'elx' in i['value'].lower():
        self['brand'] = 'سمند'
        self['model'] = 'سورن ELX'
    elif 'سمند' in i['value'] and 'سورن پلاس' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = 'سورن پلاس'
    elif 'سمند' in i['value'] and 'el' in i['value'].lower():
        self['brand'] = 'سمند'
        self['model'] = 'EL'
    elif 'سمند' in i['value'] and 'lx' in i['value'].lower():
        self['brand'] = 'سمند'
        self['model'] = 'LX'
    elif 'سمند' in i['value'] and 'se' in i['value'].lower():
        self['brand'] = 'سمند'
        self['model'] = 'SE'
    elif 'سمند' in i['value'] and 'x7' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = 'X7'
    elif 'سمند' in i['value']:
        self['brand'] = 'سمند'
        self['model'] = '‌سایر مدل‌ها'

    elif 'وانت' in i['value'] and 'آریسان' in i['value'] and 'آریسان' in i['value']:
        self['brand'] = 'آریسان'
        self['model'] = 'وانت'
    elif 'وانت' in i['value'] and 'آریسان' in i['value']:
        self['brand'] = 'آریسان'
        self['model'] = 'وانت'

    elif 'هایما' in i['value'] and 's5' in i['value'].lower():
        self['brand'] = 'هایما'
        self['model'] = 'هایما S5'
    elif 'هایما' in i['value'] and 's7' in i['value'].lower():
        self['brand'] = 'هایما'
        self['model'] = 'هایما S7'
    elif 'هایما' in i['value']:
        self['brand'] = 'هایما'
        self['model'] = '‌سایر مدل‌ها'

    elif 'جک' in i['value'] and 'j3' in i['value'].lower() and 'سدان' in i['value']:
        self['brand'] = 'جک'
        self['model'] = 'J3 سدان'
    elif 'جک' in i['value'] and 'j3' in i['value'].lower() and 'هاچبک' in i['value']:
        self['brand'] = 'جک'
        self['model'] = 'J3 هاچبک'
    elif 'جک' in i['value'] and 'j4' in i['value'].lower():
        self['brand'] = 'جک'
        self['model'] = 'J4'
    elif 'جک' in i['value'] and 'j5' in i['value'].lower():
        self['brand'] = 'جک'
        self['model'] = 'J5'
    elif 'جک' in i['value'] and 's3' in i['value'].lower():
        self['brand'] = 'جک'
        self['model'] = 'S3'
    elif 'جک' in i['value'] and 's5' in i['value'].lower():
        self['brand'] = 'جک'
        self['model'] = 'S5'
    elif 'جک' in i['value'] and 'ون' in i['value'] and 'ریفاین' in i['value']:
        self['brand'] = 'جک'
        self['model'] = 'ون ریفاین'
    elif 'جک' in i['value'] and 'ون' in i['value'] and 'سانری' in i['value']:
        self['brand'] = 'جک'
        self['model'] = 'ون سانری'
    elif 'جک' in i['value']:
        self['brand'] = 'جک'
        self['model'] = '‌سایر مدل‌ها'

    elif 'جیلی' in i['value'] and 'Emgrand' in i['value'] and '7' in i['value']:
        self['brand'] = 'جیلی'
        self['model'] = 'امگرند 7'
    elif 'جیلی' in i['value'] and 'Emgrand' in i['value'] and '7_RV' in i['value']:
        self['brand'] = 'جیلی'
        self['model'] = 'امگرند آر وی 7'
    elif 'جیلی' in i['value'] and 'Emgrand' in i['value'] and 'X7' in i['value']:
        self['brand'] = 'جیلی'
        self['model'] = 'امگرند ایکس 7'
    elif 'جیلی' in i['value'] and 'GC6' in i['value']:
        self['brand'] = 'جیلی'
        self['model'] = 'GC6'
    elif 'جیلی' in i['value']:
        self['brand'] = 'جیلی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'لیفان' in i['value'] and '520' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = 'لیفان 520'
    elif 'لیفان' in i['value'] and '520i' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = 'لیفان 520i'
    elif 'لیفان' in i['value'] and '620' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = 'لیفان 620'
    elif 'لیفان' in i['value'] and '820' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = 'لیفان 820'
    elif 'لیفان' in i['value'] and 'X50' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = 'لیفان X50'
    elif 'لیفان' in i['value'] and 'X60' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = 'لیفان X60'
    elif 'لیفان' in i['value']:
        self['brand'] = 'لیفان'
        self['model'] = 'سایر مدل‌ها'

    elif 'رنو' in i['value'] and '21' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = '21'
    elif 'رنو' in i['value'] and '5' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = '5'
    elif 'رنو' in i['value'] and '5' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = '5 مونتاژ'
    elif 'رنو' in i['value'] and 'اسکالا' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'اسکالا'
    elif 'رنو' in i['value'] and 'پارس' in i['value'] and 'تندر' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'پارس تندر'
    elif 'رنو' in i['value'] and 'پی' in i['value'] and 'کی' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'پی کی'
    elif 'رنو' in i['value'] and 'تلیسمان' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'تلیسمان'
    elif 'رنو' in i['value'] and 'تندر' in i['value'] and '90' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'تندر 90'
    elif 'رنو' in i['value'] and 'تندر' in i['value'] and '90' in i['value'] and 'پلاس' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = '  تندر 90 پلاس'
    elif 'رنو' in i['value'] and 'داستر' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'داستر'
    elif 'رنو' in i['value'] and 'ساندرو' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'ساندرو'
    elif 'رنو' in i['value'] and 'ساندرو' in i['value'] and 'استپ‌وی' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'ساندرو استپ وی'
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
    elif 'رنو' in i['value'] and 'کوليوس' in i['value']:
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
    elif 'رنو' in i['value'] and 'مگان' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = 'مگان مونتاژ'
    elif 'وانت' in i['value'] and 'رنو' in i['value'] and 'وانت' in i['value'] and 'تندر' in i['value'] and '91' in i[
        'value']:
        self['brand'] = 'رنو'
        self['model'] = 'وانت رنو وانت تندر 90'
    elif 'رنو' in i['value']:
        self['brand'] = 'رنو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'برلیانس' in i['value'] and 'کراس' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'کراس'
    elif 'برلیانس' in i['value'] and 'H220' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'H220'
    elif 'برلیانس' in i['value'] and 'H230' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'H230'
    elif 'برلیانس' in i['value'] and 'H320' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'H320'
    elif 'برلیانس' in i['value'] and 'H330' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'H330'
    elif 'برلیانس' in i['value'] and 'V5' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'V5'
    elif 'برلیانس' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = 'ون'
    elif 'برلیانس' in i['value']:
        self['brand'] = 'برلیانس'
        self['model'] = '‌سایر مدل‌ها'

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
    elif 'هیوندای' in i['value'] and 'اکسنت' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'اکسنت مونتاژ'
    elif 'هیوندای' in i['value'] and 'النترا' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'النترا'
    elif 'هیوندای' in i['value'] and 'النترا' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'النترا مونتاژ'
    elif 'هیوندای' in i['value'] and 'تراجت' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'تراجت'
    elif 'هیوندای' in i['value'] and 'توسان' in i['value'] and 'ix' in i['value'] and '35' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'توسان ix 34'
    elif 'هیوندای' in i['value'] and 'جنسیس' in i['value'] and 'سدان' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'جنسیس سدان'
    elif 'هیوندای' in i['value'] and 'جنسیس' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'جنسیس کوپه'
    elif 'هیوندای' in i['value'] and 'سانتافه' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'سانتافه'
    elif 'هیوندای' in i['value'] and 'سنتنیال' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'سنتنیال'
    elif 'هیوندای' in i['value'] and 'سوناتا' in i['value'] and 'LF' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'سوناتا LF'
    elif 'هیوندای' in i['value'] and 'سوناتا' in i['value'] and 'LF' in i['value'] and 'هیبرید' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'سوناتا LF هیبرید'
    elif 'هیوندای' in i['value'] and 'سوناتا' in i['value'] and 'NF' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = '‌سایر مدل‌ها'
    elif 'هیوندای' in i['value'] and 'سوناتا' in i['value'] and 'YF' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = '‌سایر مدل‌ها'
    elif 'هیوندای' in i['value'] and 'سوناتا' in i['value'] and 'YF' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = '‌سایر مدل‌ها'
    elif 'هیوندای' in i['value'] and 'وراکروز' in i['value'] and 'ix55' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'وراکروز ix54‌'
    elif 'هیوندای' in i['value'] and 'ورنا' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'ورنا'
    elif 'هیوندای' in i['value'] and 'ولستر' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'ولستر'
    elif 'هیوندای' in i['value'] and 'FX' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'FX کوپه'
    elif 'هیوندای' in i['value'] and 'i10' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'i10 مونتاژ'
    elif 'هیوندای' in i['value'] and 'i20' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'i20'
    elif 'هیوندای' in i['value'] and 'i30' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'i30'
    elif 'هیوندای' in i['value'] and 'i40' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'i40'
    elif 'هیوندای' in i['value'] and 'i40' in i['value'] and 'استیشن' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = 'i40 استیشن'
    elif 'هیوندای' in i['value']:
        self['brand'] = 'هیوندای'
        self['model'] = '‌سایر مدل‌ها'

    elif 'کیا' in i['value'] and 'اپتیما' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'اپتیما'
    elif 'کیا' in i['value'] and 'اپیروس' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'اپیروس'
    elif 'کیا' in i['value'] and 'اسپورتیج' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'اسپورتیج'
    elif 'کیا' in i['value'] and 'پیکانتو' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'پیکانتو'
    elif 'کیا' in i['value'] and 'ریو' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'ریو'
    elif 'کیا' in i['value'] and 'ریو' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'ریو مونتاژ'
    elif 'کیا' in i['value'] and 'سراتو' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'سراتو'
    elif 'کیا' in i['value'] and 'سراتو' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'سراتو کوپه'
    elif 'کیا' in i['value'] and 'سراتو' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'سراتو مونتاژ'
    elif 'کیا' in i['value'] and 'سورنتو' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = 'سورنتو'
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
    elif 'کیا' in i['value']:
        self['brand'] = 'کیا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'بسترن' in i['value'] and 'B30' in i['value']:
        self['brand'] = 'بسترن'
        self['model'] = 'B30'
    elif 'بسترن' in i['value'] and 'B50' in i['value']:
        self['brand'] = 'بسترن'
        self['model'] = 'B50'
    elif 'بسترن' in i['value'] and 'B50F' in i['value']:
        self['brand'] = 'بسترن'
        self['model'] = 'B50F'
    elif 'بسترن' in i['value']:
        self['brand'] = 'بسترن'
        self['model'] = '‌سایر مدل‌ها'
# new
    elif 'آئودی' in i['value'] and 'Q5' in i['value']:
        self['brand'] = 'آئودی'
        self['model'] = 'Q5'
    elif 'آئودی' in i['value'] and 'TT' in i['value']:
        self['brand'] = 'آئودی'
        self['model'] = 'TT'
    elif 'آئودی' in i['value']:
        self['brand'] = 'آئودی'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'آلفارومئو' in i['value'] and '4C' in i['value']:
        self['brand'] = 'آلفارومئو '
        self['model'] = '4C'
    elif 'آلفارومئو' in i['value'] and 'جولیتا' in i['value']:
        self['brand'] = 'آلفارومئو'
        self['model'] = 'جولیتا'
    elif 'آلفارومئو' in i['value'] and 'میتو' in i['value']:
        self['brand'] = 'آلفارومئو'
        self['model'] = 'میتو'
    elif 'آلفارومئو' in i['value'] :
        self['brand'] = 'آلفارومئو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'آمیکو وانت' in i['value'] and 'آراز' in i['value']:
        self['brand'] = 'آمیکو وانت'
        self['model'] = 'آراز'
    elif 'آمیکو وانت' in i['value'] and 'آسنا' in i['value']:
        self['brand'] = 'آمیکو وانت'
        self['model'] = 'آسنا'
    elif 'آمیکو وانت' in i['value'] :
        self['brand'] = 'آمیکو وانت'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'اپل' in i['value'] and 'آسترا استیشن' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'آسترا استیشن'
    elif 'اپل' in i['value'] and 'آسترا سدان' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'آسترا سدان'
    elif 'اپل' in i['value'] and 'آسترا هاچبک' in i['value']:
        self['brand'] = 'اپل'
        self['model'] = 'آسترا هاچبک'
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
        self['model'] = '‌سایر مدل‌ها'

    elif 'اس‌دبلیو‌ام' in i['value'] and 'G01' in i['value']:
        self['brand'] = 'اس‌دبلیو‌ام'
        self['model'] = 'G01'
    elif 'اس‌دبلیو‌ام' in i['value'] and 'G01 F' in i['value']:
        self['brand'] = 'اس‌دبلیو‌ام'
        self['model'] = 'G01 F'
    elif 'اس‌دبلیو‌ام' in i['value']:
        self['brand'] = 'اس‌دبلیو‌ام'
        self['model'] = '‌سایر مدل‌ها'

    elif 'اسمارت' in i['value'] and 'فور 2' in i['value']:
        self['brand'] = 'اسمارت'
        self['model'] = 'فور 2'
    elif 'اسمارت' in i['value'] and 'فور 4' in i['value']:
        self['brand'] = 'اسمارت'
        self['model'] = 'فور 4'
    elif 'اسمارت' in i['value']:
        self['brand'] = 'اسمارت'
        self['model'] = '‌سایر مدل‌ها'

    elif 'الدزمبیل' in i['value'] and 'ریجنسی' in i['value']:
        self['brand'] = 'الدزمبیل'
        self['model'] = 'ریجنسی'
    elif 'الدزمبیل' in i['value'] and 'کاتالاس' in i['value']:
        self['brand'] = 'الدزمبیل'
        self['model'] = 'کاتالاس'
    elif 'الدزمبیل' in i['value']:
        self['brand'] = 'الدزمبیل'
        self['model'] = '‌سایر مدل‌ها'

    elif 'ام‌جی' in i['value'] and '3' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '3'
    elif 'ام‌جی' in i['value'] and '350' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '350'
    elif 'ام‌جی' in i['value'] and '360' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '360'
    elif 'ام‌جی' in i['value'] and '550' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '550'
    elif 'ام‌جی' in i['value'] and '6' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '6'
    elif 'ام‌جی' in i['value'] and 'GS' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = 'GS'
    elif 'ام‌جی' in i['value'] and 'GT' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = 'GT'
    elif 'ام‌جی' in i['value'] and 'RX5' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = 'RX5'
    elif 'ام‌جی' in i['value']:
        self['brand'] = 'ام‌جی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'ایسوزو' in i['value'] and 'دو کابین' in i['value']:
        self['brand'] = 'ایسوزو'
        self['model'] = 'دو کابین'
    elif 'ایسوزو' in i['value']:
        self['brand'] = 'ایسوزو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'اینرودز' in i['value'] and 'ون C35' in i['value']:
        self['brand'] = 'اینرودز'
        self['model'] = 'ون C35'
    elif 'اینرودز' in i['value']:
        self['brand'] = 'اینرودز'
        self['model'] = '‌سایر مدل‌ها'

    elif 'ایویکو' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'ایویکو'
        self['model'] = 'ون'
    elif 'ایویکو' in i['value']:
        self['brand'] = 'ایویکو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'بایک' in i['value'] and 'سابرینا' in i['value']:
        self['brand'] = 'بایک'
        self['model'] = 'سابرینا'
    elif 'بایک' in i['value'] and 'سابرینا مونتاژ' in i['value']:
        self['brand'] = 'بایک'
        self['model'] = 'سابرینا مونتاژ'
    elif 'بایک' in i['value'] and 'سنوا' in i['value']:
        self['brand'] = 'بایک'
        self['model'] = 'سنوا'
    elif 'بایک' in i['value'] and 'X25' in i['value']:
        self['brand'] = 'بایک'
        self['model'] = 'X25'
    elif 'بایک' in i['value']:
        self['brand'] = 'بایک'
        self['model'] = '‌سایر مدل‌ها' 

    elif 'بنز' in i['value'] and 'کلاس A' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس A'
    elif 'بنز' in i['value'] and 'کلاس B' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس B'
    elif 'بنز' in i['value'] and 'کلاس C' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس C'
    elif 'بنز' in i['value'] and 'کلاس C کوپه' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس C کوپه'
    elif 'بنز' in i['value'] and 'کلاس CL' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CL'
    elif 'بنز' in i['value'] and 'کلاس CLA' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CLA'
    elif 'بنز' in i['value'] and 'کلاس CLK' in i['value'] and 'کروک' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CLK کروک'
    elif 'بنز' in i['value'] and 'کلاس CLK' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CLK کوپه'
    elif 'بنز' in i['value'] and 'کلاس CLS' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس CLS'
    elif 'بنز' in i['value'] and 'کلاس E' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس E'
    elif 'بنز' in i['value'] and 'کلاس E' in i['value'] and 'کروک' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس E کروک'
    elif 'بنز' in i['value'] and 'کلاس E' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس E کوپه'
    elif 'بنز' in i['value'] and 'کلاس E' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاس E مونتاژ'
    elif 'بنز' in i['value'] and 'GLA' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'GLA'
    elif 'بنز' in i['value'] and 'GLK' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'GLK'
    elif 'بنز' in i['value'] and 'ML' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'ML'
    elif 'بنز' in i['value'] and 'S' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'S'
    elif 'بنز' in i['value'] and 'SL' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'SL'
    elif 'بنز' in i['value'] and 'SLC' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'SLC'
    elif 'بنز' in i['value'] and 'SLK' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'SLK'
    elif 'بنز' in i['value'] and 'کلاسیک' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'کلاسیک'
    elif 'بنز' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'بنز'
        self['model'] = 'ون'
    elif 'بنز' in i['value'] :
        self['brand'] = 'بنز'
        self['model'] = '‌سایر مدل‌ها'

    elif 'بورگوارد' in i['value'] and 'BX5' in i['value']:
        self['brand'] = 'بورگوارد'
        self['model'] = 'BX5'
    elif 'بورگوارد' in i['value'] and 'BX7' in i['value']:
        self['brand'] = 'بورگوارد'
        self['model'] = 'BX7'
    elif 'بورگوارد' in i['value'] :
        self['brand'] = 'بورگوارد'
        self['model'] = '‌سایر مدل‌ها'

    elif 'بی‌ام‌و' in i['value'] and '2002' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = '2002'
    elif 'بی‌ام‌و' in i['value'] and 'سری 1' in i['value'] and 'کروک' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 1 کروک'
    elif 'بی‌ام‌و' in i['value'] and 'سری 1' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 1 کوپه'
    elif 'بی‌ام‌و' in i['value'] and 'سری 1' in i['value'] and 'هاچبک' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 1 هاچبک'
    elif 'بی‌ام‌و' in i['value'] and 'سری 2' in i['value'] and 'اکتیوتور' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 2 اکتیوتور'
    elif 'بی‌ام‌و' in i['value'] and 'سری 2' in i['value'] and 'کروک' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 2 کروک'
    elif 'بی‌ام‌و' in i['value'] and 'سری 2' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 2 کوپه'
    elif 'بی‌ام‌و' in i['value'] and 'سری 3' in i['value'] and 'سدان' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 3 سدان'
    elif 'بی‌ام‌و' in i['value'] and 'سری 3' in i['value'] and 'کروک' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 3 کروک'
    elif 'بی‌ام‌و' in i['value'] and 'سری 3' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 3 کوپه'
    elif 'بی‌ام‌و' in i['value'] and 'سری 3' in i['value'] and 'GT' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 3 GT'
    elif 'بی‌ام‌و' in i['value'] and 'سری 4' in i['value'] and 'کروک' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 4 کروک'
    elif 'بی‌ام‌و' in i['value'] and 'سری 4' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 4 کوپه'
    elif 'بی‌ام‌و' in i['value'] and 'سری 4' in i['value'] and 'گرن کوپه' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 4 گرن کوپه'
    elif 'بی‌ام‌و' in i['value'] and 'سری 5' in i['value'] and 'سدان' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 5 سدان'
    elif 'بی‌ام‌و' in i['value'] and 'سری 5' in i['value'] and 'GT' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 5 GT'
    elif 'بی‌ام‌و' in i['value'] and 'سری 6' in i['value'] and 'کروک' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 6 کروک'
    elif 'بی‌ام‌و' in i['value'] and 'سری 6' in i['value'] and 'کوپه' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 6 کوپه'
    elif 'بی‌ام‌و' in i['value'] and 'سری 6' in i['value'] and 'گرن کوپه' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 6 گرن کوپه'
    elif 'بی‌ام‌و' in i['value'] and 'سری 7' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'سری 7'
    elif 'بی‌ام‌و' in i['value'] and 'کلاسیک' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'کلاسیک'
    elif 'بی‌ام‌و' in i['value'] and 'i8' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'i8'
    elif 'بی‌ام‌و' in i['value'] and 'X1' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'X1'
    elif 'بی‌ام‌و' in i['value'] and 'X3' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'X3'
    elif 'بی‌ام‌و' in i['value'] and 'X4' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'X4'
    elif 'بی‌ام‌و' in i['value'] and 'X5' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'X5'
    elif 'بی‌ام‌و' in i['value'] and 'X6' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'X6'
    elif 'بی‌ام‌و' in i['value'] and 'z3' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'z3'
    elif 'بی‌ام‌و' in i['value'] and 'Z4' in i['value']:
        self['brand'] = 'بی‌ام‌و'
        self['model'] = 'Z4'
    elif 'بی‌ام‌و' in i['value'] :
        self['brand'] = 'بی‌ام‌و'
        self['model'] = '‌سایر مدل‌ها'

    elif 'بیسو' in i['value'] and 'T3' in i['value']:
        self['brand'] = 'بیسو'
        self['model'] = 'T3'
    elif 'بیسو' in i['value'] and 'T5' in i['value']:
        self['brand'] = 'بیسو'
        self['model'] = 'T5'
    elif 'بیسو' in i['value'] :
        self['brand'] = 'بیسو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'بی‌‌وای‌دی' in i['value'] and 'F3' in i['value']:
        self['brand'] = 'بی‌‌وای‌دی'
        self['model'] = 'F3'
    elif 'بی‌‌وای‌دی' in i['value'] and 'S6' in i['value']:
        self['brand'] = 'بی‌‌وای‌دی'
        self['model'] = 'S6'
    elif 'بی‌‌وای‌دی' in i['value'] and 'S7' in i['value']:
        self['brand'] = 'بی‌‌وای‌دی'
        self['model'] = 'S7'
    elif 'بی‌‌وای‌دی' in i['value'] :
        self['brand'] = 'بی‌‌وای‌دی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'بیوک' in i['value'] and 'B2' in i['value']:
        self['brand'] = 'بیوک'
        self['model'] = 'B2'
    elif 'بیوک' in i['value'] and 'B3' in i['value']:
        self['brand'] = 'بیوک'
        self['model'] = 'B3'
    elif 'بیوک' in i['value'] and 'B3' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'بیوک'
        self['model'] = 'B3 مونتاژ'
    elif 'بیوک' in i['value']:
        self['brand'] = 'بیوک'
        self['model'] = '‌سایر مدل‌ها'

    elif 'پاژن' in i['value'] and '2 در' in i['value']:
        self['brand'] = 'پاژن'
        self['model'] = '2 در'
    elif 'پاژن' in i['value'] and '4 در' in i['value']:
        self['brand'] = 'پاژن'
        self['model'] = '4 در'
    elif 'پاژن' in i['value'] and 'هرور' in i['value']:
        self['brand'] = 'پاژن'
        self['model'] = 'هرور'
    elif 'پاژن' in i['value']:
        self['brand'] = 'پاژن'
        self['model'] = '‌سایر مدل‌ها'

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
        self['model'] = '‌سایر مدل‌ها'

    elif 'پورشه' in i['value'] and '911' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = '911'
    elif 'پورشه' in i['value'] and 'باکستر' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'باکستر'
    elif 'پورشه' in i['value'] and 'پانامرا' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'پانامرا'
    elif 'پورشه' in i['value'] and 'کاین' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'کاین'
    elif 'پورشه' in i['value'] and 'کیمن' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'کیمن'
    elif 'پورشه' in i['value'] and 'ماکان' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = 'ماکان'
    elif 'پورشه' in i['value']:
        self['brand'] = 'پورشه'
        self['model'] = '‌سایر مدل‌ها'

    elif 'پونتیاک' in i['value'] and 'پاریزین' in i['value']:
        self['brand'] = 'پونتیاک'
        self['model'] = 'پاریزین'
    elif 'پونتیاک' in i['value'] and 'گرند پریکس' in i['value']:
        self['brand'] = 'پونتیاک'
        self['model'] = 'گرند پریکس'
    elif 'پونتیاک' in i['value']:
        self['brand'] = 'پونتیاک'
        self['model'] = '‌سایر مدل‌ها'

    elif 'تارا' in i['value'] and 'اتوماتیک' in i['value']:
        self['brand'] = 'تارا'
        self['model'] = 'اتوماتیک'
    elif 'تارا' in i['value'] and 'دنده ای' in i['value']:
        self['brand'] = 'تارا'
        self['model'] = 'دنده ای'
    elif 'تارا' in i['value']:
        self['brand'] = 'تارا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'تویوتا' in i['value'] and 'آریون' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'آریون'
    elif 'تویوتا' in i['value'] and 'اف جی کروز' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'اف جی کروز'
    elif 'تویوتا' in i['value'] and 'اکو' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'اکو'
    elif 'تویوتا' in i['value'] and 'پرادو' in i['value'] and '2 در' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'پرادو 2 در'
    elif 'تویوتا' in i['value'] and 'پرادو' in i['value'] and '4 در' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'پرادو 4 در'
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
    elif 'تویوتا' in i['value'] and 'لندکروز' in i['value'] and '2 در' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'لندکروز 2 در'
    elif 'تویوتا' in i['value'] and 'لندکروز' in i['value'] and '4 در' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'لندکروز 4 در'
    elif 'تویوتا' in i['value'] and 'هایلوکس' in i['value'] and 'تک کابین' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'هایلوکس تک کابین'
    elif 'تویوتا' in i['value'] and 'هایلوکس' in i['value'] and 'دو کابین' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'دو کابین'
    elif 'تویوتا' in i['value'] and 'هایلوکس' in i['value'] and 'دو کابین بلند' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'دو کابین بلند'
    elif 'تویوتا' in i['value'] and 'یاریس' in i['value'] and 'صندوق دار' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'یاریس صندوق دار'
    elif 'تویوتا' in i['value'] and 'یاریس' in i['value'] and 'هاچبک' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'یاریس هاچبک'
    elif 'تویوتا' in i['value'] and 'CH-R' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'CH-R'
    elif 'تویوتا' in i['value'] and 'GT 86' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'GT 86'
    elif 'تویوتا' in i['value'] and 'وانت لندکروز' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'وانت لندکروز'
    elif 'تویوتا' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = 'ون'
    elif 'تویوتا' in i['value']:
        self['brand'] = 'تویوتا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'جگوار' in i['value'] and 'XJ' in i['value']:
        self['brand'] = 'جگوار'
        self['model'] = 'XJ'
    elif 'جگوار' in i['value']:
        self['brand'] = 'جگوار'
        self['model'] = '‌سایر مدل‌ها'

    elif 'جوی لانگ' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'جوی لانگ'
        self['model'] = 'ون'
    elif 'جوی لانگ' in i['value']:
        self['brand'] = 'جوی لانگ'
        self['model'] = '‌سایر مدل‌ها'

    elif 'جی‌ام‌سی' in i['value'] and 'S350' in i['value']:
        self['brand'] = 'جی‌ام‌سی'
        self['model'] = 'S350'
    elif 'جی‌ام‌سی' in i['value']:
        self['brand'] = 'جی‌ام‌سی'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'جی‌ای‌سی گونو' in i['value'] and 'G5' in i['value']:
        self['brand'] = 'جی‌ای‌سی گونو'
        self['model'] = 'G5'
    elif 'جی‌ای‌سی گونو' in i['value'] and 'GA3S' in i['value']:
        self['brand'] = 'جی‌ای‌سی گونو'
        self['model'] = 'GA3S'
    elif 'جی‌ای‌سی گونو' in i['value'] and 'GS5' in i['value']:
        self['brand'] = 'جی‌ای‌سی گونو'
        self['model'] = 'GS5'
    elif 'جی‌ای‌سی گونو' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'جی‌ای‌سی گونو'
        self['model'] = 'وانت'
    elif 'جی‌ای‌سی گونو' in i['value']:
        self['brand'] = 'جی‌ای‌سی گونو'
        self['model'] = '‌سایر مدل‌ها'
    
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
    elif 'جیپ' in i['value'] and 'KM' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'KM'
    elif 'جیپ' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = 'وانت'
    elif 'جیپ' in i['value']:
        self['brand'] = 'جیپ'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'چانگان' in i['value'] and 'CS35' in i['value']:
        self['brand'] = 'چانگان'
        self['model'] = 'CS35'
    elif 'چانگان' in i['value'] and 'CS35' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'چانگان'
        self['model'] = 'CS35 مونتاژ'
    elif 'چانگان' in i['value'] and 'EADO' in i['value']:
        self['brand'] = 'چانگان'
        self['model'] = 'EADO'
    elif 'چانگان' in i['value']:
        self['brand'] = 'چانگان'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'چری' in i['value'] and 'آریزو' in i['value'] and '5' in i['value']:
        self['brand'] = 'چری'
        self['model'] = '5'
    elif 'چری' in i['value'] and 'آریزو' in i['value'] and '5IE جدید' in i['value']:
        self['brand'] = 'چری'
        self['model'] = '5IE جدید'
    elif 'چری' in i['value'] and 'آریزو' in i['value'] and '5TE' in i['value']:
        self['brand'] = 'چری'
        self['model'] = '5TE'
    elif 'چری' in i['value'] and 'آریزو' in i['value'] and '6' in i['value']:
        self['brand'] = 'چری'
        self['model'] = '6'
    elif 'چری' in i['value'] and 'تیگو' in i['value'] and '5' in i['value']:
        self['brand'] = 'چری'
        self['model'] = '5'
    elif 'چری' in i['value'] and 'تیگو' in i['value'] and '7' in i['value']:
        self['brand'] = 'چری'
        self['model'] = '7'
    elif 'چری' in i['value'] and 'ویانا A15' in i['value']:
        self['brand'] = 'چری'
        self['model'] = 'ویانا A15'
    elif 'چری' in i['value']:
        self['brand'] = 'چری'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'داتسون' in i['value'] and 'سواری' in i['value']:
        self['brand'] = 'داتسون'
        self['model'] = 'سواری'
    elif 'داتسون' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'داتسون'
        self['model'] = 'وانت'
    elif 'داتسون' in i['value']:
        self['brand'] = 'داتسون'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'دانگ فنگ' in i['value'] and 'H30 کراس' in i['value']:
        self['brand'] = 'دانگ فنگ'
        self['model'] = 'H30 کراس'
    elif 'دانگ فنگ' in i['value'] and 'S30' in i['value']:
        self['brand'] = 'دانگ فنگ'
        self['model'] = 'S30'
    elif 'دانگ فنگ' in i['value']:
        self['brand'] = 'دانگ فنگ'
        self['model'] = '‌سایر مدل‌ها'

    elif 'دامای' in i['value'] and 'X7' in i['value']:
        self['brand'] = 'دامای'
        self['model'] = 'X7'
    elif 'دامای' in i['value']:
        self['brand'] = 'دامای'
        self['model'] = '‌سایر مدل‌ها'

    elif 'دایون' in i['value'] and 'Y5' in i['value']:
        self['brand'] = 'دایون'
        self['model'] = 'Y5'
    elif 'دایون' in i['value']:
        self['brand'] = 'دایون'
        self['model'] = '‌سایر مدل‌ها'

    elif 'دایهاتسو' in i['value']:
        self['brand'] = 'دایهاتسو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'دلیکا' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'دلیکا'
        self['model'] = 'ون'
    elif 'دلیکا' in i['value']:
        self['brand'] = 'دلیکا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'دوج' in i['value'] and 'کرنت' in i['value']:
        self['brand'] = 'دوج'
        self['model'] = 'کرنت'
    elif 'دوج' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'دوج'
        self['model'] = 'ون'
    elif 'دوج' in i['value']:
        self['brand'] = 'دوج'
        self['model'] = '‌سایر مدل‌ها'

    elif 'دوو' in i['value'] and 'اسپرو' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = 'اسپرو'
    elif 'دوو' in i['value'] and 'ریسر' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = 'ریسر'
    elif 'دوو' in i['value'] and 'سی یلو' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = 'سی یلو'
    elif 'دوو' in i['value'] and 'ماتیز' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = 'ماتیز'
    elif 'دوو' in i['value']:
        self['brand'] = 'دوو'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'دی‌اس' in i['value'] and 'کراس بک' in i['value'] and '4' in i['value']:
        self['brand'] = 'دی‌اس'
        self['model'] = 'کراس بک 4'
    elif 'دی‌اس' in i['value'] and 'کراس بک' in i['value'] and '7' in i['value']:
        self['brand'] = 'دی‌اس'
        self['model'] = 'کراس بک 7'
    elif 'دی‌اس' in i['value'] and '3' in i['value']:
        self['brand'] = 'دی‌اس'
        self['model'] = '3'
    elif 'دی‌اس' in i['value'] and '5' in i['value']:
        self['brand'] = 'دی‌اس'
        self['model'] = '5'
    elif 'دی‌اس' in i['value'] and '5LS' in i['value']:
        self['brand'] = 'دی‌اس'
        self['model'] = '5LS'
    elif 'دی‌اس' in i['value'] and '6' in i['value']:
        self['brand'] = 'دی‌اس'
        self['model'] = '6'
    elif 'دی‌اس' in i['value']:
        self['brand'] = 'دی‌اس'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'دیگنیتی' in i['value']:
        self['brand'] = 'دیگنیتی'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'دییر' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'دییر'
        self['model'] = 'وانت'
    elif 'دییر' in i['value']:
        self['brand'] = 'دییر'
        self['model'] = '‌سایر مدل‌ها'

    elif 'راین' in i['value'] and 'V5' in i['value']:
        self['brand'] = 'راین'
        self['model'] = 'V5'
    elif 'راین' in i['value']:
        self['brand'] = 'راین'
        self['model'] = '‌سایر مدل‌ها'
    
    elif 'رولزرویس' in i['value']:
        self['brand'] = 'رولزرویس'
        self['model'] = '‌سایر مدل‌ها'
    

    elif 'ریچ' in i['value'] and 'دوکابین' in i['value']:
        self['brand'] = 'ریچ'
        self['model'] = 'دوکابین'
    elif 'ریچ' in i['value']:
        self['brand'] = 'ریچ'
        self['model'] = '‌سایر مدل‌ها'
    

    elif 'ریگان' in i['value'] and 'کوپا' in i['value']:
        self['brand'] = 'ریگان'
        self['model'] = 'کوپا'
    elif 'ریگان' in i['value']:
        self['brand'] = 'ریگان'
        self['model'] = '‌سایر مدل‌ها'
    

    elif 'زامیاد' in i['value'] and 'پادرا' in i['value'] :
        self['brand'] = 'زامیاد'
        self['model'] = 'پادرا'
    elif 'زامیاد' in i['value'] and 'پادرا' in i['value'] and 'پلاس' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = 'پادرا پلاس'
    elif 'زامیاد' in i['value'] and 'درکا' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = 'درکا'
    elif 'زامیاد' in i['value'] and 'شوکا' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = 'شوکا'
    elif 'زامیاد' in i['value'] and 'Z 24' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = 'Z 24'
    elif 'زامیاد' in i['value']:
        self['brand'] = 'زامیاد'
        self['model'] = '‌سایر مدل‌ها'
    

    elif 'زوتی' in i['value'] and 'Z300 ورداتی' in i['value']:
        self['brand'] = 'زوتی'
        self['model'] = 'Z300 ورداتی'
    elif 'زوتی' in i['value']:
        self['brand'] = 'زوتی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'سانگ یانگ' in i['value'] and 'اکتیون' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'اکتیون'
    elif 'سانگ یانگ' in i['value'] and 'تیوولی' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'تیوولی'
    elif 'سانگ یانگ' in i['value'] and 'تیوولی' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'تیوولی مونتاژ'
    elif 'سانگ یانگ' in i['value'] and 'چیرمن' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'چیرمن'
    elif 'سانگ یانگ' in i['value'] and 'رکستون' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'رکستون'
    elif 'سانگ یانگ' in i['value'] and 'رکستون' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'مونتاژ رکستون'
    elif 'سانگ یانگ' in i['value'] and 'رودیوس' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'رودیوس'
    elif 'سانگ یانگ' in i['value'] and 'کایرون' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'کایرون'
    elif 'سانگ یانگ' in i['value'] and 'کوراندو' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'کوراندو'
    elif 'سانگ یانگ' in i['value'] and 'موسو' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'موسو'
    elif 'سانگ یانگ' in i['value'] and 'نیو اکتیون' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'نیو اکتیون'
    elif 'سانگ یانگ' in i['value'] and 'نیو کوراندو' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = 'نیو کوراندو'
    elif 'سانگ یانگ' in i['value']:
        self['brand'] = 'سانگ یانگ'
        self['model'] = '‌سایر مدل‌ها'

    elif 'سئات' in i['value'] and 'لئون' in i['value']:
        self['brand'] = 'سئات'
        self['model'] = 'لئون'
    elif 'سئات' in i['value']:
        self['brand'] = 'سئات'
        self['model'] = '‌سایر مدل‌ها'

    elif 'سوئیست' in i['value'] and 'DX 3' in i['value']:
        self['brand'] = 'سوئیست'
        self['model'] = 'DX 3'
    elif 'سوئیست' in i['value']:
        self['brand'] = 'سوئیست'
        self['model'] = '‌سایر مدل‌ها'

    elif 'سوبارو' in i['value'] and 'فارستر' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'فارستر'
    elif 'سوبارو' in i['value'] and 'لگاسی' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'لگاسی'
    elif 'سوبارو' in i['value'] and 'وی ویو' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'وی ویو'
    elif 'سوبارو' in i['value'] and 'X7' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'X7'
    elif 'سوبارو' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = 'وانت'
    elif 'سوبارو' in i['value']:
        self['brand'] = 'سوبارو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'سوزوکی' in i['value'] and 'کیزاشی' in i['value']:
        self['brand'] = 'سوزوکی'
        self['model'] = 'کیزاشی'
    elif 'سوزوکی' in i['value'] and 'گرند ویتارا' in i['value']:
        self['brand'] = 'سوزوکی'
        self['model'] = 'گرند ویتارا'
    elif 'سوزوکی' in i['value'] and 'گرند ویتارا' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'سوزوکی'
        self['model'] = 'گرند ویتارا مونتاژ'
    elif 'سوزوکی' in i['value']:
        self['brand'] = 'سوزوکی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'سیتروئن' in i['value'] and 'زانتیا' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = 'زانتیا'
    elif 'سیتروئن' in i['value'] and 'زانتیا' in i['value'] and '2' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = 'زانتیا 2 (فیس لیفت)'
    elif 'سیتروئن' in i['value'] and 'ژیان' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = 'ژیان'
    elif 'سیتروئن' in i['value'] and 'C3' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = 'C3 مونتاژ'
    elif 'سیتروئن' in i['value'] and 'C5' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = 'C5'
    elif 'سیتروئن' in i['value'] and 'C5' in i['value'] and 'جدید' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = 'C5 جدید'
    elif 'سیتروئن' in i['value']:
        self['brand'] = 'سیتروئن'
        self['model'] = '‌سایر مدل‌ها'

    elif 'سیناد' in i['value']:
        self['brand'] = 'سیناد'
        self['model'] = '‌سایر مدل‌ها'

    elif 'شاهین' in i['value'] and 'G' in i['value']:
        self['brand'] = 'شاهین'
        self['model'] = 'G'
    elif 'شاهین' in i['value']:
        self['brand'] = 'شاهین'
        self['model'] = '‌سایر مدل‌ها'

    elif 'شورولت' in i['value'] and 'ایمپالا' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'ایمپالا'
    elif 'شورولت' in i['value'] and 'بلر' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'بلر'
    elif 'شورولت' in i['value'] and 'بلیزر' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'بلیزر'
    elif 'شورولت' in i['value'] and 'رویال' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'رویال مونتاژ'
    elif 'شورولت' in i['value'] and 'سابربن' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'سابربن'
    elif 'شورولت' in i['value'] and 'فلیت' in i['value']  and 'مستر' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'فلیت مستر'
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
        self['model'] = 'نوا مونتاژ'
    elif 'شورولت' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'وانت'
    elif 'شورولت' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = 'ون'
    elif 'شورولت' in i['value']:
        self['brand'] = 'شورولت'
        self['model'] = '‌سایر مدل‌ها'

    elif 'فردا' in i['value'] and '511' in i['value']:
        self['brand'] = 'فردا'
        self['model'] = '511'
    elif 'فردا' in i['value'] and 'Sx5' in i['value']:
        self['brand'] = 'فردا'
        self['model'] = 'Sx5'
    elif 'فردا' in i['value'] and 'Sx6' in i['value']:
        self['brand'] = 'فردا'
        self['model'] = 'Sx6'
    elif 'فردا' in i['value'] and 'T5' in i['value']:
        self['brand'] = 'فردا'
        self['model'] = 'T5'
    elif 'فردا' in i['value']:
        self['brand'] = 'فردا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'فوتون' in i['value'] and 'ساوانا' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = 'ساوانا'
    elif 'فوتون' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = 'وانت'
    elif 'فوتون' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = 'ون'
    elif 'فوتون' in i['value']:
        self['brand'] = 'فوتون'
        self['model'] = '‌سایر مدل‌ها'

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
        self['model'] = '‌سایر مدل‌ها'

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
    elif 'فولکس' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'وانت'
    elif 'فولکس' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = 'ون'
    elif 'فولکس' in i['value']:
        self['brand'] = 'فولکس'
        self['model'] = '‌سایر مدل‌ها'

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
        self['model'] = '‌سایر مدل‌ها'

    elif 'فیات' in i['value'] and '500' in i['value']:
        self['brand'] = 'فیات'
        self['model'] = '500'
    elif 'فیات' in i['value'] and 'سی ینا' in i['value']:
        self['brand'] = 'فیات'
        self['model'] = 'سی ینا'
    elif 'فیات' in i['value']:
        self['brand'] = 'فیات'
        self['model'] = '‌سایر مدل‌ها'

    elif 'فیدلیتی' in i['value'] and 'پرایم' in i['value']:
        self['brand'] = 'فیدلیتی'
        self['model'] = 'پرایم'
    elif 'فیدلیتی' in i['value']:
        self['brand'] = 'فیدلیتی'
        self['model'] = '‌سایر مدل‌ها'

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
        self['model'] = '‌سایر مدل‌ها'

    elif 'کرایسلر' in i['value']:
        self['brand'] = 'کرایسلر'
        self['model'] = '‌سایر مدل‌ها'

    elif 'کوییک' in i['value'] and 'اتوماتیک' in i['value']:
        self['brand'] = 'کوییک'
        self['model'] = 'اتوماتیک'
    elif 'کوییک' in i['value'] and 'دنده‌ای' in i['value']:
        self['brand'] = 'کوییک'
        self['model'] = 'دنده‌ای'
    elif 'کوییک' in i['value']:
        self['brand'] = 'کوییک'
        self['model'] = '‌سایر مدل‌ها'

    elif 'کی‌ام‌سی' in i['value'] and 'K7' in i['value']:
        self['brand'] = 'کی‌ام‌سی'
        self['model'] = 'K7'
    elif 'کی‌ام‌سی' in i['value'] and 'T8' in i['value']:
        self['brand'] = 'کی‌ام‌سی'
        self['model'] = 'T8'
    elif 'کی‌ام‌سی' in i['value']:
        self['brand'] = 'کی‌ام‌سی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'گریت وال' in i['value'] and 'وینگل' in i['value'] and '5' in i['value'] and 'تک کابین' in i['value']:
        self['brand'] = 'گریت وال'
        self['model'] = 'وینگل 5 تک کابین'
    elif 'گریت وال' in i['value'] and 'وینگل' in i['value'] and '5' in i['value'] and 'دو کابین' in i['value']:
        self['brand'] = 'گریت وال'
        self['model'] = 'وینگل 5 دو کابین'
    elif 'گریت وال' in i['value'] and 'C30' in i['value']:
        self['brand'] = 'گریت وال'
        self['model'] = 'C30'
    elif 'گریت وال' in i['value'] and 'وانت' in i['value'] and 'وینگل 3' in i['value']:
        self['brand'] = 'گریت وال'
        self['model'] = 'وانت وینگل 3'
    elif 'گریت وال' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'گریت وال'
        self['model'] = 'ون'
    elif 'گریت وال' in i['value']:
        self['brand'] = 'گریت وال'
        self['model'] = '‌سایر مدل‌ها'

    elif 'لادا' in i['value'] and 'نیوا' in i['value']:
        self['brand'] = 'لادا'
        self['model'] = 'نیوا'
    elif 'لادا' in i['value']:
        self['brand'] = 'لادا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'لامبورگینی' in i['value']:
        self['brand'] = 'لامبورگینی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'لکسوس' in i['value'] and 'CT' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'CT'
    elif 'لکسوس' in i['value'] and 'ES' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'ES'
    elif 'لکسوس' in i['value'] and 'GS' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'GS'
    elif 'لکسوس' in i['value'] and 'IS' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'IS'
    elif 'لکسوس' in i['value'] and 'IS' in i['value'] and 'کروک' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'IS کروک'
    elif 'لکسوس' in i['value'] and 'LS' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'LS'
    elif 'لکسوس' in i['value'] and 'LX' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'LX'
    elif 'لکسوس' in i['value'] and 'NX 200t' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'NX 200t'
    elif 'لکسوس' in i['value'] and 'NX 300 H' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'NX 300 H'
    elif 'لکسوس' in i['value'] and 'RX' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = 'RX'
    elif 'لکسوس' in i['value']:
        self['brand'] = 'لکسوس'
        self['model'] = '‌سایر مدل‌ها'

    elif 'لندروز' in i['value'] and 'دیسکاوری' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'دیسکاوری'
    elif 'لندروز' in i['value'] and 'دیفندر' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'دیفندر'
    elif 'لندروز' in i['value'] and 'رنجرور' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'رنجرور'
    elif 'لندروز' in i['value'] and 'رنجرور' in i['value'] and 'ایووک' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'رنجرور ایووک'
    elif 'لندروز' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'مونتاژ'
    elif 'لندروز' in i['value'] and 'فریلندر' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = 'فریلندر'
    elif 'لندروز' in i['value']:
        self['brand'] = 'لندروز'
        self['model'] = '‌سایر مدل‌ها'

    elif 'لندمارک' in i['value'] and 'V7' in i['value']:
        self['brand'] = 'لندمارک'
        self['model'] = 'V7'
    elif 'لندمارک' in i['value']:
        self['brand'] = 'لندمارک'
        self['model'] = '‌سایر مدل‌ها'

    elif 'لوتوس' in i['value'] and 'الیزه' in i['value']:
        self['brand'] = 'لوتوس'
        self['model'] = 'الیزه'
    elif 'لوتوس' in i['value']:
        self['brand'] = 'لوتوس'
        self['model'] = '‌سایر مدل‌ها'

    elif 'لوکسیژن' in i['value'] and 'U6' in i['value']:
        self['brand'] = 'لوکسیژن'
        self['model'] = 'U6'
    elif 'لوکسیژن' in i['value']:
        self['brand'] = 'لوکسیژن'
        self['model'] = '‌سایر مدل‌ها'

    elif 'مازراتی' in i['value'] and 'کواتروپورته' in i['value']:
        self['brand'] = 'مازراتی'
        self['model'] = 'کواتروپورته'
    elif 'مازراتی' in i['value'] and 'گرن' in i['value'] and 'توریسمو' in i['value']:
        self['brand'] = 'مازراتی'
        self['model'] = 'گرن توریسمو'
    elif 'مازراتی' in i['value'] and 'گرن' in i['value'] and 'کبریو' in i['value']:
        self['brand'] = 'مازراتی'
        self['model'] = 'گرن کبریو'
    elif 'مازراتی' in i['value'] and 'گیبلی' in i['value']:
        self['brand'] = 'مازراتی'
        self['model'] = 'گیبلی'
    elif 'مازراتی' in i['value']:
        self['brand'] = 'مازراتی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'مزدا' in i['value'] and '2' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '2 مونتاژ'
    elif 'مزدا' in i['value'] and '3' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '3 مونتاژ'
    elif 'مزدا' in i['value'] and '323' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '323'
    elif 'مزدا' in i['value'] and '3N' in i['value'] and 'صندوق‌دار' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '3N صندوق‌دار مونتاژ'
    elif 'مزدا' in i['value'] and '3N' in i['value'] and 'هاچبک' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '3N هاچبک مونتاژ'
    elif 'مزدا' in i['value'] and '6' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '6'
    elif 'مزدا' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = 'وانت'
    elif 'مزدا' in i['value']:
        self['brand'] = 'مزدا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'مکث موتور' in i['value'] and 'کلوت' in i['value']:
        self['brand'] = 'مکث موتور'
        self['model'] = 'کلوت'
    elif 'مکث موتور' in i['value']:
        self['brand'] = 'مکث موتور'
        self['model'] = '‌سایر مدل‌ها'

    elif 'مکسوس' in i['value'] and 'ون' in i['value']:
        self['brand'] = 'مکسوس'
        self['model'] = 'ون'
    elif 'مکسوس' in i['value']:
        self['brand'] = 'مکسوس'
        self['model'] = '‌سایر مدل‌ها'

    elif 'میتسوبیشی' in i['value'] and 'اوتلندر' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'اوتلندر'
    elif 'میتسوبیشی' in i['value'] and 'اوتلندر' in i['value'] and 'PHEV' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'اوتلندر PHEV'
    elif 'میتسوبیشی' in i['value'] and 'پاجرو' in i['value'] and '2 در' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'پاجرو 2 در'
    elif 'میتسوبیشی' in i['value'] and 'پاجرو' in i['value'] and '4 در' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'پاجرو 4 در'
    elif 'میتسوبیشی' in i['value'] and 'پاجرو' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'میتسوبیشی'
        self['model'] = 'پاجرو مونتاژ'
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
        self['model'] = '‌سایر مدل‌ها'

    elif 'مینی' in i['value'] and 'کانتری من' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = 'کانتری من'
    elif 'مینی' in i['value'] and 'کلاب من' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = 'کلاب من'
    elif 'مینی' in i['value'] and 'کلاسیک' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = 'کلاسیک'
    elif 'مینی' in i['value'] and 'کوپر S' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = 'کوپر S'
    elif 'مینی' in i['value']:
        self['brand'] = 'مینی'
        self['model'] = '‌سایر مدل‌ها'

    elif 'نیسان' in i['value'] and 'آلتیما' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'آلتیما'
    elif 'نیسان' in i['value'] and 'ایکس تریل' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'ایکس تریل'
    elif 'نیسان' in i['value'] and 'پاترول 2 در' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'پاترول 2 در'
    elif 'نیسان' in i['value'] and 'پاترول 4 در' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'پاترول 4 در'
    elif 'نیسان' in i['value'] and 'پت فایندر' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'پت فایندر'
    elif 'نیسان' in i['value'] and 'تی ینا مونتاژ' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'تی ینا مونتاژ'
    elif 'نیسان' in i['value'] and 'تی ینا وارداتی' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'تی ینا وارداتی'
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
    elif 'نیسان' in i['value'] and 'قشقایی' in i['value'] and 'مونتاژ' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'قشقایی مونتاژ'
    elif 'نیسان' in i['value'] and 'قشقایی' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'قشقایی'
    elif 'نیسان' in i['value'] and 'ماکسیما مونتاژ' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'ماکسیما مونتاژ'
    elif 'نیسان' in i['value'] and 'ماکسیما وارداتی' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'ماکسیما وارداتی'
    elif 'نیسان' in i['value'] and 'مورانو' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'مورانو'
    elif 'نیسان' in i['value'] and 'وانت' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = 'وانت'
    elif 'نیسان' in i['value']:
        self['brand'] = 'نیسان'
        self['model'] = '‌سایر مدل‌ها'

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
        self['model'] = '‌سایر مدل‌ها'

    elif 'ون ایران خودرو' in i['value'] and 'غزال' in i['value']:
        self['brand'] = 'ون ایران خودرو'
        self['model'] = 'غزال'
    elif 'ون ایران خودرو' in i['value'] and 'وانا' in i['value']:
        self['brand'] = 'ون ایران خودرو'
        self['model'] = 'وانا'
    elif 'ون ایران خودرو' in i['value']:
        self['brand'] = 'ون ایران خودرو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'ون سایپا' in i['value'] and 'کاروان' in i['value']:
        self['brand'] = 'ون سایپا'
        self['model'] = 'کاروان'
    elif 'ون سایپا' in i['value']:
        self['brand'] = 'ون سایپا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'ون فاو' in i['value'] and 'سیبا' in i['value']:
        self['brand'] = 'ون فاو'
        self['model'] = 'سیبا'
    elif 'ون فاو' in i['value']:
        self['brand'] = 'ون فاو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'ون نارون' in i['value'] and 'تاکسی' in i['value']:
        self['brand'] = 'ون نارون'
        self['model'] = 'تاکسی'
    elif 'ون نارون' in i['value'] and 'شخصی' in i['value']:
        self['brand'] = 'ون نارون'
        self['model'] = 'شخصی'
    elif 'ون نارون' in i['value']:
        self['brand'] = 'ون نارون'
        self['model'] = '‌سایر مدل‌ها'

    elif 'هافی لوبو' in i['value'] and 'لوبو' in i['value']:
        self['brand'] = 'هافی لوبو'
        self['model'] = 'لوبو'
    elif 'هافی لوبو' in i['value']:
        self['brand'] = 'هافی لوبو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'هامر' in i['value'] and 'H2' in i['value']:
        self['brand'] = 'هامر'
        self['model'] = 'H2'
    elif 'هامر' in i['value']:
        self['brand'] = 'هامر'
        self['model'] = '‌سایر مدل‌ها'

    elif 'هاوال' in i['value'] and 'H2 مونتاژ' in i['value']:
        self['brand'] = 'هاوال'
        self['model'] = 'H2 مونتاژ'
    elif 'هاوال' in i['value'] and 'H6' in i['value']:
        self['brand'] = 'هاوال'
        self['model'] = 'H6'
    elif 'هاوال' in i['value'] and 'H6 مونتاژ' in i['value']:
        self['brand'] = 'هاوال'
        self['model'] = 'H6 مونتاژ'
    elif 'هاوال' in i['value'] and 'H9' in i['value']:
        self['brand'] = 'هاوال'
        self['model'] = 'H9'
    elif 'هاوال' in i['value'] and 'M4' in i['value']:
        self['brand'] = 'هاوال'
        self['model'] = 'M4'
    elif 'هاوال' in i['value'] and 'M4 مونتاژ' in i['value']:
        self['brand'] = 'هاوال'
        self['model'] = 'M4 مونتاژ'
    elif 'هاوال' in i['value']:
        self['brand'] = 'هاوال'
        self['model'] = '‌سایر مدل‌ها'

    elif 'هن تنگ' in i['value'] and 'X5 مونتاژ' in i['value']:
        self['brand'] = 'هن تنگ'
        self['model'] = 'X5 مونتاژ'
    elif 'هن تنگ' in i['value'] and 'X7 مونتاژ' in i['value']:
        self['brand'] = 'هن تنگ'
        self['model'] = 'X7 مونتاژ'
    elif 'هن تنگ' in i['value']:
        self['brand'] = 'هن تنگ'
        self['model'] = '‌سایر مدل‌ها'

    elif 'هوندا' in i['value'] and 'آکورد' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = 'آکورد'
    elif 'هوندا' in i['value'] and 'سیویک' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = 'سیویک'
    elif 'هوندا' in i['value'] and 'لجند' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = 'لجند'
    elif 'هوندا' in i['value'] and 'CR-V' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = 'CR-V'
    elif 'هوندا' in i['value'] and 'CR-X' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = 'CR-X'
    elif 'هوندا' in i['value']:
        self['brand'] = 'هوندا'
        self['model'] = '‌سایر مدل‌ها'

    elif 'هیلمن' in i['value']:
        self['brand'] = 'هیلمن'
        self['model'] = '‌سایر مدل‌ها'

    elif 'هیوسو' in i['value'] and 'T205' in i['value']:
        self['brand'] = 'هیوسو'
        self['model'] = 'T205'
    elif 'هیوسو' in i['value']:
        self['brand'] = 'هیوسو'
        self['model'] = '‌سایر مدل‌ها'

    elif 'یوآز' in i['value'] and 'پاتریوت' in i['value']:
        self['brand'] = 'یوآز'
        self['model'] = 'پاتریوت'
    elif 'یوآز' in i['value'] and 'پیکاپ' in i['value']:
        self['brand'] = 'یوآز'
        self['model'] = 'پیکاپ'
    elif 'یوآز' in i['value']:
        self['brand'] = 'یوآز'
        self['model'] = '‌سایر مدل‌ها'

    else:
        self['brand'] = "not_defined"
        self['model'] = "not_defined"