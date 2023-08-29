import datetime
from persiantools.jdatetime import JalaliDate
from iranestekhdam.utilities.db_work import get_province


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

def check_educatuin_is_valid(education):
    education_list = ["دیپلم" , "فوق دیپلم " , "کاردانی" , "لیسانس" , "کارشسناسی" , "فوق لیسانس" 
    , "کارشناسی ارشد" , "دکترا" , "فوق دکترا"]

    return education in education_list

def extract_province_city_iranestekhdam(text: str):
    tex = text.strip()

    group1 = {
        'خ_جنوبی': {'p': 'خراسان جنوبی', 'c': 'بیرجند'},
        'خ- شمالی': {'p': 'خراسان شمالی', 'c': 'بجنورد'},
        'خ-رضوی': {'p': 'خراسان رضوی', 'c': 'مشهد'},
        'هرمزگان': {'p': 'هرمزگان', 'c': 'بندرعباس'},
        'چ - و - ب': {'p': 'چهارمحال بختیاری', 'c': 'شهرکرد'},
        'لرستان': {'p': 'لرستان', 'c': 'خرم آباد'},
        'گیلان': {'p': 'گیلان', 'c': 'رشت'},
        'مازندران': {'p': 'مازندران', 'c': 'ساری'},
        'مرکزی': {'p': 'مرکزی', 'c': 'اراک'},
        'کردستان': {'p': 'کردستان', 'c': 'سنندج'},
        'ک-و-ب': {'p': 'کهکیلویه و بویراحمد', 'c': 'یاسوج'},
        'آ_شرقی': {'p': 'آذربایجان شرقی', 'c': 'تبریز'},
        'آ.غربی': {'p': 'آذربایجان غربی', 'c': 'ارومیه'},
        'اردبیل': {'p': 'اردبیل', 'c': 'اردبیل'},
        'اصفهان': {'p': 'اصفهان', 'c': 'اصفهان'},
        'البرز': {'p': 'البرز', 'c': 'کرج'},
        'ایلام': {'p': 'ایلام', 'c': 'ایلام'},
        'بوشهر': {'p': 'بوشهر', 'c': 'بوشهر'},
        'تهران': {'p': 'تهران', 'c': 'تهران'},
        'خوزستان': {'p': 'خوزستان', 'c': 'اهواز'},
        'زنجان': {'p': 'زنجان', 'c': 'زنجان'},
        'سمنان': {'p': 'سمنان', 'c': 'سمنان'},
        'س - و - ب': {'p': 'سیستان و بلوچستان', 'c': 'زاهدان'},
        'فارس': {'p': 'فارس', 'c': 'شیراز'},
        'قزوین': {'p': 'قزوین', 'c': 'قزوین'},
        'قم': {'p': 'قم', 'c': 'قم'},
        'کرمان': {'p': 'کرمان', 'c': 'کرمان'},
        'کرمانشاه': {'p': 'کرمانشاه', 'c': 'کرمانشاه'},
        'کهگیلویه و بویراحمد': 'یاسوج',
        'گلستان': {'p': 'گلستان', 'c': 'گرگان'},
        'همدان': {'p': 'همدان', 'c': 'همدان'},
        'یزد': {'p': 'یزد', 'c': 'یزد'},
    }

    group2 = {
        'تهران و ورامین': {'p': 'تهران', 'c': 'تهران'},
        'گل گهر سیرجان': {'p': 'کرمان', 'c': 'سیرجان'},
    }

    if tex in group1.keys():
        return group1[tex]

    if 'استان' in tex:
        temp = tex.split()
        if 'استان' in temp[0]:
            if ' '.join(temp[1:]) in group1.keys():
                return group1[' '.join(temp[1:])]
        
        else:
            return {'p': 'تهران', 'c': 'تهران'}

    if 'سراسر' in tex:
        return {'p': 'تهران', 'c': 'تهران'}

    if tex in group2.keys():
        return group2[tex]

    return get_province(tex)

def is_extracted_item_valid(token , city , province):
    return not (len(str(token)) == 0 or token == -1 or len(city) == 0 or city == 'not_defined' \
            or len(province) == 0 or province == 'not_defined')