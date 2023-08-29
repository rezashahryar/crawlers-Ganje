import logging

logging.basicConfig(filename="itemsLog",level=logging.INFO)

class JobVisionStats:
    fields = {
        "city" : 0,
        "education" : 0,
        "insurnace" : 0,
        "cooperation" : 0,
        "salary" : 0,
        "gender" : 0,
        "experience" : 0,
        "teleworking" : 0,
    }
    count = 1

    def specify_the_broken_one(self,title):
        self.fields[title] += 1

    def item_added(self) : self.count += 1

    def calculate_the_broken_stats(self):
        broken_dict = self.fields.copy()

        broken_dict['city'] = (self.fields['city'] / self.count) * 100
        broken_dict['education'] = (self.fields['education'] / self.count) * 100
        broken_dict['insurnace'] = (self.fields['insurnace'] / self.count) * 100
        broken_dict['cooperation'] = (self.fields['cooperation'] / self.count) * 100
        broken_dict['salary'] = (self.fields['salary'] / self.count) * 100
        broken_dict['gender'] = (self.fields['gender'] / self.count) * 100
        broken_dict['experience'] = (self.fields['experience'] / self.count) * 100
        broken_dict['teleworking'] = (self.fields['teleworking'] / self.count) * 100

        # logging.info(f"city : {broken_dict['city']}")
        logging.info(f"education : {broken_dict['education']}")
        logging.info(f"insurance : {broken_dict['insurnace']}")
        logging.info(f"cooperation : {broken_dict['cooperation']}")
        logging.info(f"salary : {broken_dict['salary']}")
        logging.info(f"gender : {broken_dict['gender']}")
        logging.info(f"experience : {broken_dict['experience']}")
        logging.info(f"teleworking : {broken_dict['teleworking']}")

        with open('readme.txt', 'w') as f:
            try :
                for (key , value) in broken_dict.items():
                    f.writelines(f"broken-{key} : {value} %\n")
            except : None

        return broken_dict