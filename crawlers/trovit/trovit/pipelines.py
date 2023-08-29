# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.utils.log import logger
import psycopg2 as psycopg2

from trovit.utilities.Normalize import normalize_item
from trovit.utilities.configs import server_db, local_db

# class TrovitPipeline:
#     def process_item(self, item, spider):
#         return item

class TrovitPipeline:
    def open_spider(self, spider):
        # db_config = local_db
        db_config = server_db
        self.conn = psycopg2.connect(
            database=db_config["database"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"])
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        ad_type = 'foreign_home'

        normalize_item(item, ad_type)

        if self.not_exist(item['token'], ad_type):
           self.save_data(item)

    def save_data(self, item):
        try:
            self.cursor.execute(
                "INSERT INTO foreign_home (" +
                (("token," if self.insertThis(item['token']) else "") +
                 ("source_id," if self.insertThis(item['source_id']) else "") + 
                 ("time," if self.insertThis(item['time']) else "") + 
                 ("title," if self.insertThis(item["title"]) else "") +
                 ("category," if self.insertThis(item["category"]) else "") +
                 ("sub_category," if self.insertThis(item["subcategory"]) else "") +
                 ("country," if self.insertThis(item["country"]) else "") +
                 ("province," if self.insertThis(item["province"]) else "") +
                 ("city," if self.insertThis(item["city"]) else "") +
                 ("room," if self.insertThis(item["room"]) else "") +
                 ("bathroom," if self.insertThis(item["bathroom"]) else "") +
                 ("area," if self.insertThis(item["area"]) else "") +
                 ("moneyunit," if self.insertThis(item["moneyunit"]) else "") +
                 ("price," if self.insertThis(item["price"]) else "") +
                 ("deposit," if self.insertThis(item["deposit"]) else "") +
                 ("rent," if self.insertThis(item["rent"]) else "") +
                 ("url," if self.insertThis(item["url"]) else "") +
                 ("thumbnail," if self.insertThis(item["thumbnail"]) else "")).strip(",") +
                 (",description" if self.insertThis(item["description"]) else "") +
                 ") " +
                 "values (" +
                 ((f"{item['token']}," if self.insertThis(item["token"]) else "") +
                  (f"{item['source_id']}," if self.insertThis(item["source_id"]) else "") +
                  (f"{item['time']}," if self.insertThis(item["time"]) else "") +
                  (f"'{item['title']}'," if self.insertThis(item["title"]) else "") +
                  (f"'{item['category']}'," if self.insertThis(item["category"]) else "") +
                  (f"'{item['subcategory']}'," if self.insertThis(item["subcategory"]) else "") +
                  (f"'{item['country']}'," if self.insertThis(item["country"]) else "") +
                  (f"'{item['province']}'," if self.insertThis(item["province"]) else "") +
                  (f"'{item['city']}'," if self.insertThis(item["city"]) else "") +
                  (f"{item['room']}," if self.insertThis(item["room"]) else "") +
                  (f"{item['bathroom']}," if self.insertThis(item["bathroom"]) else "") +
                  (f"{item['area']}," if self.insertThis(item["area"]) else "") +
                  (f"'{item['moneyunit']}'," if self.insertThis(item["moneyunit"]) else "") +
                  (f"{item['price']}," if self.insertThis(item["price"]) else "") +
                  (f"{item['deposit']}," if self.insertThis(item["deposit"]) else "") +
                  (f"{item['rent']}," if self.insertThis(item["rent"]) else "") +
                  (f"'{item['url']}'," if self.insertThis(item["url"]) else "") +
                  (f"'{item['thumbnail']}'," if self.insertThis(item["thumbnail"]) else "")).strip(",") +
                  (f",'{item['description']}'" if self.insertThis(item["description"]) else "") +
                  " )")
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            logger.critical(f"storing foreign_home failed: {e}")
        return item

    def not_exist(self, token, ad_type):
        try:
            self.cursor.execute(f"select exists(select 1 from {ad_type} where token = {token} )")
            data = self.cursor.fetchall()
            # logger.warning(f"{str(data[0])} {str(data[0][0])}")
            if data[0][0] == True:
                return False
        except Exception as e:
            self.conn.rollback()
            logger.critical(f"pipeline => not_exist: {e}")
        return True

    def insertThis(self, v):
        return str(v) != '-1' and v != 'not_defined' and v != 'notdefined' and v != 'not defined' and str(v) != '-1.0' and v != 'not-defined' \
               and v != 'NOTDEFINED' and v != 'NOT DEFINED' and len(str(v)) != 0 and v is not None