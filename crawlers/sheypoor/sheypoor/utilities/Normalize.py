import sqlite3

from hazm import Normalizer
import datetime


def normalize_item(item, ad_type):
    for k, v in item.items():
        if k not in ['url', 'thumbnail', 'title', 'description', 'city_slug', 'brand', 'model', 'tip'] and isinstance(v, str):
            item[k] = remove_extra_character_and_normalize(v, check_space=False)
        elif k == 'title' or k == 'description':
            item[k] = normalize_text(v)

    if 'home' == ad_type:
        normalize_home_item(item)
    elif 'car' == ad_type:
        normalize_car_item(item)


def normalize_home_item(item):
    item['kitchen'] = normalize_kitchen(item['kitchen'])
    item['floor_covering'] = normalize_floor_covering(item['floor_covering'])
    item['price'] = clean_number(item['price'], False)
    item['deposit'] = clean_number(item['deposit'], False)
    item['rent'] = clean_number(item['rent'], False)


def normalize_kitchen(kitchen: str):
    if ('mdf' in kitchen or 'MDF' in kitchen or 'ام دی اف' in kitchen) and \
            ('open' in kitchen or 'OPEN' in kitchen or 'اوپن' in kitchen):
        return 'اوپن ام دی اف'
    if 'mdf' in kitchen or 'MDF' in kitchen or 'ام دی اف' in kitchen:
        return 'کابینت ام دی اف'
    if 'چوب' in kitchen or 'چوبی' in kitchen:
        return 'کابینت چوبی'
    if 'فلز' in kitchen or 'فلزی' in kitchen:
        return 'کابینت فلزی'
    if 'هایگلاس' in kitchen or 'هایگلس' in kitchen or 'higlass' in kitchen:
        return 'کابینت هایگلاس'
    if 'ممبران' in kitchen or 'membrane' in kitchen:
        return 'کابینت ممبران'
    return 'not_defined'


def normalize_floor_covering(floor_covering: str):
    if 'پارکت' in floor_covering:
        return 'پارکت'
    if 'سرامیک' in floor_covering or 'سرامیك' in floor_covering:
        return 'سرامیک'
    if 'سنگ' in floor_covering:
        return 'سنگ'
    if 'لمینت' in floor_covering or 'لمینیت' in floor_covering:
        return 'لمینیت'
    if 'موزاییک' in floor_covering or 'موزائیک' in floor_covering or 'موزاییك' in floor_covering or 'موزائیك' in floor_covering:
        return 'موزائیک'
    if 'موکت' in floor_covering:
        return 'موکت'
    return 'not_defined'


def normalize_car_item(item):
    item['color'] = normalize_color(item['color'])
    item['cash_installment'] = normalize_cash_installment(
        item['cash_installment'])
    item['chassis_type'] = normalize_chassis_type(item['chassis_type'])
    item['price'] = clean_number(item['price'], False)
    item['fuel'] = normalize_fuel(item['fuel'])
    item['gear_box'] = normalize_gear_box(item['gear_box'])
    item['production'] = normalize_production(item['production'])
    item['consumption'] = normalize_consumption(item['consumption'])


def normalize_consumption(consumption):
    try:
        if ',' in consumption:
            return int(consumption.replace(',', ''))
        if ' ' in consumption:
            return int(consumption.replace(' ', ''))
    except:
        return -1
    return -1


def normalize_brand(brand: str):
    brand = brand.upper()

    brand = brand.replace('هاچبک', '')
    brand = brand.replace('هاچبك', '')
    brand = brand.replace('هاچ بك', '')
    brand = brand.replace('هاچ بک', '')
    brand = brand.replace('صندوقدار', '')
    brand = brand.replace('صندوق دار', '')
    brand = brand.replace('مونتاژ', '')
    brand = brand.replace('سدان', '')
    brand = brand.replace('سواری', '')

    if 'وانت' in brand or 'سایر' in brand or 'قطعات' in brand or 'دیگر' in brand:
        return 'not_defined'
    if 'آیودی' in brand or 'ایودی' in brand or 'آئودی' in brand or 'ائودی' in brand or 'AUDI' in brand:
        return 'آئودی'
    if 'آریسان' in brand or 'اریسان' in brand:
        return 'آریسان'
    if 'آریو' in brand or 'اریو' in brand or 'زوتی' in brand:
        return 'زوتی آریو'
    if 'آلفا رومئو' in brand or 'آلفارومئو' in brand or 'آلفارومیو' in brand or 'الفارومئو' in brand or 'الفارومیو' in brand or 'ALFA ROMEO' in brand:
        return 'آلفارومئو'
    if 'اس دبلیو ام' in brand or 'SWM' in brand:
        return 'اس دبلیو ام'
    if 'اس وای ام' in brand or 'SYM' in brand:
        return 'اس وای ام'
    if 'MG' in brand or 'ام جی' in brand:
        return 'ام جی'
    if 'BMW' in brand or 'ب ام و' in brand or 'بی ام و' in brand:
        return 'بی ام و'
    if 'DS' in brand or 'دی اس' in brand:
        return 'دی اس'
    if 'سیتروین' in brand or 'سیتروئن' in brand:
        return 'سیتروئن'
    if 'دانگ' in brand and 'فنگ' in brand:
        return 'دانگ فنگ'        
    if 'فولکس' in brand:
        return 'فولکس'
    if 'کیا' in brand:
        return 'کیا'
    if 'گک' in brand:
        return 'گک'
    if 'بوگوارد' in brand:
        return 'بوگوارد'
    if 'پژو' in brand:
        return 'پژو'
    if 'پراید' in brand:
        return 'پراید'
    if 'سمند' in brand:
        return 'سمند'
    if 'آئودی' in brand:
        return 'آئودی'
    if 'آریسان' in brand:
        return 'آریسان'
    if 'آریو' in brand:
        return 'آریو'
    if 'آلفا رومئو' in brand:
        return 'آلفا رومئو'
    if 'آمیکو' in brand:
        return 'آمیکو'
    if 'اپل' in brand:
        return 'اپل'
    if 'اس دبلیو ام' in brand:
        return 'اس دبلیو ام'
    if 'ام جی' in brand:
        return 'ام جی'
    if 'ام وی ام' in brand:
        return 'ام وی ام'
    if 'ایسوزو' in brand:
        return 'ایسوزو'
    if 'بایک' in brand:
        return 'بایک'
    if 'برلیانس' in brand:
        return 'برلیانس'
    if 'بسترن' in brand:
        return 'بسترن'
    if 'بنز' in brand:
        return 'بنز'
    if 'بورگوارد' in brand:
        return 'بورگوارد'
    if 'بی ام و' in brand:
        return 'بی ام و'
    if 'بی وای دی' in brand:
        return 'بی وای دی'
    if 'بیسو' in brand:
        return 'بیسو'
    if 'پاژن' in brand:
        return 'پاژن'
    if 'پروتون' in brand:
        return 'پروتون'
    if 'پورشه' in brand:
        return 'پورشه'
    if 'پیکان' in brand:
        return 'پیکان'
    if 'تارا' in brand:
        return 'تارا'
    if 'تویوتا' in brand:
        return 'تویوتا'  
    if 'تیبا' in brand:
        return 'تیبا'
    if 'جک' in brand:
        return 'جک'
    if 'جیپ' in brand:
        return 'جیپ'
    if 'جیلی' in brand:
        return 'جیلی'
    if 'چانگان' in brand:
        return 'چانگان'
    if 'چری' in brand:
        return 'چری'
    if 'دامای' in brand:
        return 'دامای'
    if 'دانگ فنگ' in brand:
        return 'دانگ فنگ'
    if 'دنا' in brand:
        return 'دنا'
    if 'دوو' in brand:
        return 'دوو'
    if 'دی اس' in brand:
        return 'دی اس'
    if 'رانا' in brand:
        return 'رانا'
    if 'رنو' in brand:
        return 'رنو'
    if 'ریگان' in brand:
        return 'ریگان'
    if 'سانگ یانگ' in brand:
        return 'سانگ یانگ'
    if 'ساینا' in brand:
        return 'ساینا'
    if 'سوبارو' in brand:
        return 'سوبارو'
    if 'سوزوکی' in brand:
        return 'سوزوکی'
    if 'سیتروئن' in brand:
        return 'سیتروئن'
    if 'شاهین' in brand:
        return 'شاهین'
    if 'فاو' in brand:
        return 'فاو'
    if 'فردا' in brand:
        return 'فردا'
    if 'فوتون' in brand:
        return 'فوتون'
    if 'فولوکس واگن' in brand:
        return 'فولوکس واگن'
    if 'فیات' in brand:
        return 'فیات'
    if 'کاپرا' in brand:
        return 'کاپرا'
    if 'کارا' in brand:
        return 'کارا'
    if 'کوییک' in brand:
        return 'کوییک'
    if 'کیا' in brand:
        return 'کیا'
    if 'گریت وال' in brand:
        return 'گریت وال'
    if 'گک کونو' in brand:
        return 'گک کونو'
    if 'لکسوس' in brand:
        return 'لکسوس'
    if 'لند مارک' in brand:
        return 'لند مارک'
    if 'لندرور' in brand:
        return 'لندرور'
    if 'لوتوس' in brand:
        return 'لوتوس'
    if 'لوکسژن' in brand:
        return 'لوکسژن'
    if 'لیفان' in brand:
        return 'لیفان'
    if 'مازراتی' in brand:
        return 'مازراتی'
    if 'مزدا' in brand:
        return 'مزدا'
    if 'میتسوبیشی' in brand:
        return 'میتسوبیشی'
    if 'مینی' in brand:
        return 'مینی'
    if 'نیسان' in brand:
        return 'نیسان'
    if 'ولوو' in brand:
        return 'ولوو'
    if 'هایما' in brand:
        return 'هایما'
    if 'هن تنگ' in brand:
        return 'هن تنگ'
    if 'هوندا' in brand:
        return 'هوندا'
    if 'هیوندای' in brand:
        return 'هیوندای'
    if 'یواز' in brand:
        return 'یواز'

    return brand


def normalize_color(color: str):
    color = color.replace('ئ', 'ی')
    if 'سایر' in color:
        return 'not_defined'
    if 'قهو' in color:
        return 'قهوه ای'
    return color


def normalize_cash_installment(cash_installment: str):
    if 'اقساطی' in cash_installment or 'قسطی' in cash_installment:
        return 'قسطی'
    return cash_installment


def normalize_chassis_type(chassis_type: str):
    chassis_type = chassis_type.replace('هاچبک', 'هاچ بک')
    chassis_type = chassis_type.replace('هاچبك', 'هاچ بک')
    chassis_type = chassis_type.replace('هاچ بك', 'هاچ بک')

    if 'سواری' in chassis_type or 'سدان' in chassis_type or 'صندوق' in chassis_type:
        return 'سواری'
    elif 'کوپه' in chassis_type or 'کروک' in chassis_type or 'کروك' in chassis_type:
        return 'کوپه/کروک'
    elif 'نیمه' in chassis_type:
        return 'نیمه شاسی'
    elif 'شاسی' in chassis_type:
        return 'شاسی بلند'
    elif 'وانت' in chassis_type:
        return 'وانت'
    elif 'ون' in chassis_type:
        return 'ون'
    elif 'استیشن' in chassis_type:
        return 'استیشن'
    else:
        return 'not_defined'


def normalize_fuel(fuel: str):
    if 'دیزل' in fuel or 'گازوییل' in fuel or 'گازوئیل' in fuel or 'گازویل' in fuel:
        return 'گازوئیل'
    if 'هیبرید' in fuel:
        return 'هیبریدی'
    if ('گاز' in fuel and 'بنز' in fuel) or 'دو' in fuel:
        return 'دوگانه سوز'
    return fuel


def normalize_gear_box(gear_box: str):
    if 'دنده' in gear_box:
        return 'دنده ای'
    if 'اتومات' in gear_box:
        return 'اتوماتیک'

    return gear_box


def normalize_production(production):
    production = clean_number(production)
    if production > (datetime.datetime.today().year - 620):
        return production - 621
    return production


def normalize_text(text: str):
    n = Normalizer()
    try:
        text = n.normalize(text)
        text = text.replace('‌', ' ')
        text = text.replace('"', ' ')
        text = text.replace("'", ' ')
        text = text.replace("\\", ' ')
        return text
    except:
        return None


def remove_extra_character_and_normalize(text: str, listing=False, check_space=True):
    text = normalize_text(text)
    text = convert_digits(text)
    if check_space:
        text = check_space_with_digit(text)
    text = remove_extra("(", text)
    text = remove_extra(")", text)
    text = remove_extra("-", text)
    text = remove_extra("_", text)
    text = remove_extra(",", text)
    text = remove_extra("،", text)
    text = remove_extra("*", text)
    text = remove_extra("/", text)
    text = remove_extra(".", text)
    text = remove_extra("#", text)
    text = remove_extra("%", text)
    text = remove_extra("$", text)
    text = remove_extra("=", text)
    text = remove_extra("+", text)
    text = remove_extra("\\", text)
    text = remove_extra("<", text)
    text = remove_extra(">", text)
    text = remove_extra("|", text)
    text = remove_extra("[", text)
    text = remove_extra("]", text)
    text = remove_extra("{", text)
    text = remove_extra("}", text)
    if listing:
        return [t.strip() for t in text.split()]
    return " ".join([t.strip() for t in text.split()])


def remove_extra(key, text: str):
    c_index = text.find(key)
    if c_index + 1 >= len(text) or c_index <= 0:
        return text.replace(key, "")
    if text[c_index + 1] == " " or text[c_index - 1] == " ":
        return text.replace(key, "")
    return text.replace(key, " ")


def convert_digits(text: str):
    result = ""
    for c in text:
        if c == '۰':
            result += '0'
        elif c == '۱':
            result += '1'
        elif c == '۲':
            result += '2'
        elif c == '۳':
            result += '3'
        elif c == '۴':
            result += '4'
        elif c == '۵':
            result += '5'
        elif c == '۶':
            result += '6'
        elif c == '۷':
            result += '7'
        elif c == '۸':
            result += '8'
        elif c == '۹':
            result += '9'
        else:
            result += c
    return result


def normalize_and_compare(c1, c2):
    if isinstance(c1, str) and isinstance(c2, str):
        c1 = normalize_text(c1)
        c2 = normalize_text(c2)
    return c1 == c2


def check_space_with_digit(text: str):
    result = ""
    for t in text:
        if t.isdigit() and not result[-1:].isdigit() and result[-1:] != " ":
            result += " " + t

        elif result[-1:].isdigit() and not t.isdigit() and t != " ":
            result += " " + t

        else:
            result += t

    return result.strip()


def clean_number(data, int_type=True):
    data = convert_digits(str(data))
    if str(data) == "-1":
        if int_type:
            return int(data)
        return data
    clean_data = "-1"
    for c in str(data):
        if c.isdigit():
            if clean_data == "-1":
                clean_data = ""
            clean_data += c
    if int_type:
        return int(clean_data)
    return clean_data


def convert_alphabetic_number_to_integer(number):
    if number == 'بدون اتاق':
        return 0
    elif number == 'یک':
        return 1
    elif number == 'دو':
        return 2
    elif number == 'سه':
        return 3
    elif number == 'چهار':
        return 4
    else:
        return 5
