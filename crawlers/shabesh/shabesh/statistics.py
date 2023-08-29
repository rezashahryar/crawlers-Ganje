import logging

logging.basicConfig(filename="itemsLog",level=logging.INFO)

class ShabeshStats:
    fields = {
        "title" : 0,
        "city" : 0,
        "production" : 0,
        "token" : 0,
        "room" : 0,
        "area" : 0,
        "price" : 0,
        "deposit" : 0,
        "rent" : 0,
        "thumbnail" : 0,
    }
    count = 1

    def specify_the_broken_one(self,title):
        self.fields[title] += 1

    def item_added(self) : self.count += 1

    def calculate_the_broken_stats(self):
        broken_dict = self.fields.copy()

        broken_dict['title'] = (self.fields['title'] / self.count) * 100
        broken_dict['city'] = (self.fields['city'] / self.count) * 100
        broken_dict['production'] = (self.fields['production'] / self.count) * 100
        broken_dict['token'] = (self.fields['token'] / self.count) * 100
        broken_dict['room'] = (self.fields['room'] / self.count) * 100
        broken_dict['area'] = (self.fields['area'] / self.count) * 100
        broken_dict['price'] = (self.fields['price'] / self.count) * 100
        broken_dict['deposit'] = (self.fields['deposit'] / self.count) * 100
        broken_dict['rent'] = (self.fields['rent'] / self.count) * 100
        broken_dict['thumbnail'] = (self.fields['thumbnail'] / self.count) * 100

        logging.info(f"city : {broken_dict['city']}")
        logging.info(f"production : {broken_dict['production']}")
        logging.info(f"token : {broken_dict['token']}")
        logging.info(f"room : {broken_dict['room']}")
        logging.info(f"price : {broken_dict['price']}")
        logging.info(f"deposit : {broken_dict['deposit']}")
        logging.info(f"rent : {broken_dict['rent']}")

        with open('readme.txt', 'w') as f:
            try :
                for (key , value) in broken_dict.items():
                    f.writelines(f"broken-{key} : {value} %\n")
            except : None

        return broken_dict