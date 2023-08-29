from codecs import utf_8_decode, utf_8_encode
import json
from dadmatools.models.normalizer import Normalizer

class Extractor:
    def extract_data_from_res():
        """Extract Title And Description From Scrawler Output."""
        with open('../res.json', 'r') as f:
            titles = ""
            descs = ""
            try :
                # Combine Items Title And Description
                datas = json.load(f)
                for data in datas:
                    for (key , value) in data.items():
                        if key == "title":    
                            titles += value + " , "
                        if key == "description":
                            descs += value.replace('\t','').replace('\n','').replace('\r','').strip() + " , "

                # Extract Title and Description In Json File
                with open('NLP/Title&Desc/../../title&desc.json', 'w',encoding='utf-8') as f:
                    try :    
                        output = {
                            "title" : titles,
                            "desc" : descs
                        }
                        json_object = json.dump(output,f,ensure_ascii=False)

                        f.write(json_object)
                    except : None
            except : None

Extractor.extract_data_from_res()