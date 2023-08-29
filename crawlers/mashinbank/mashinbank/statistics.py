import logging

logging.basicConfig(filename="itemsLog",level=logging.INFO)

class MashinBankStats:
    fields = {
        "title" : 0,
        "province" : 0,
        "production" : 0,
        "token" : 0,
        "brand" : 0,
        "consumption" : 0,
        "price" : 0,
        "color" : 0,
        "cash_installment" : 0,
        "gear_box" : 0,
        "company" : 0,
        "chassis_type" : 0,
        "model" : 0,
        "body_condition" : 0,
        "fuel" : 0
    }
    count = 1

    def specify_the_broken_one(self,title):
        self.fields[title] += 1

    def item_added(self) : self.count += 1

    def calculate_the_broken_stats(self):
        broken_dict = self.fields.copy()

        broken_dict['title'] = (self.fields['title'] / self.count) * 100
        broken_dict['province'] = (self.fields['province'] / self.count) * 100
        broken_dict['production'] = (self.fields['production'] / self.count) * 100
        broken_dict['token'] = (self.fields['token'] / self.count) * 100
        broken_dict['brand'] = (self.fields['brand'] / self.count) * 100
        broken_dict['consumption'] = (self.fields['consumption'] / self.count) * 100
        broken_dict['price'] = (self.fields['price'] / self.count) * 100
        broken_dict['color'] = (self.fields['color'] / self.count) * 100
        broken_dict['cash_installment'] = (self.fields['cash_installment'] / self.count) * 100
        broken_dict['gear_box'] = (self.fields['gear_box'] / self.count) * 100
        broken_dict['company'] = (self.fields['company'] / self.count) * 100
        broken_dict['chassis_type'] = (self.fields['chassis_type'] / self.count) * 100
        broken_dict['model'] = (self.fields['model'] / self.count) * 100
        broken_dict['body_condition'] = (self.fields['body_condition'] / self.count) * 100
        broken_dict['fuel'] = (self.fields['fuel'] / self.count) * 100

        logging.info(f"title : {broken_dict['title']}")
        logging.info(f"province : {broken_dict['province']}")
        logging.info(f"production : {broken_dict['production']}")
        logging.info(f"token : {broken_dict['token']}")
        logging.info(f"brand : {broken_dict['brand']}")
        logging.info(f"consumption : {broken_dict['consumption']}")
        logging.info(f"price : {broken_dict['price']}")
        logging.info(f"color : {broken_dict['color']}")
        logging.info(f"cash_installment : {broken_dict['cash_installment']}")
        logging.info(f"gear_box : {broken_dict['gear_box']}")
        logging.info(f"company : {broken_dict['company']}")
        logging.info(f"chassis_type : {broken_dict['chassis_type']}")
        logging.info(f"model : {broken_dict['model']}")
        logging.info(f"body_condition : {broken_dict['body_condition']}")
        logging.info(f"fuel : {broken_dict['fuel']}")

        with open('readme.txt', 'w') as f:
            try :
                for (key , value) in broken_dict.items():
                    f.writelines(f"broken-{key} : {value} %\n")
            except : None

        return broken_dict