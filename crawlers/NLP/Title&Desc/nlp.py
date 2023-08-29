import dadmatools.pipeline.language as language
import json
from dadmatools.models.normalizer import Normalizer
from csv import DictReader,DictWriter

class Extractor:
    def extract_data_from_res(input_file_path,output_mode):
        """Extract Title And Description From Scrawler Output."""
        with open(input_file_path, 'r') as f:
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
                            if type(value) == type([]):
                                for desc in value:
                                    if desc != "not_defined":
                                        descs += desc.replace('\t','').replace('\n','').replace('\r','').strip() + " , "
                            else :
                                if value != "not_defined":        
                                    descs += value.replace('\t','').replace('\n','').replace('\r','').strip() + " , "
            
                # Extract Title and Description In Json File
                if output_mode == 'w':
                    with open('title&desc.json', output_mode,encoding='utf-8') as f2:
                        output = [
                            {
                                "title" : titles,
                                "desc" : descs
                            },
                        ]
                        json_object = json.dump(output,f2,ensure_ascii=False)
                        f2.writelines(json_object)
                else :
                    with open('title&desc.json', 'r',encoding='utf-8') as f3:
                        datas = json.load(f3)
                        output = {
                                "title" : titles,
                                "desc" : descs
                            }
                        datas.append(output)

                        with open('title&desc.json','w',encoding='utf-8') as f4:
                            json_object = json.dump(datas,f4,ensure_ascii=False)
                            f4.writelines(datas)
            except : None
    
    def combine_titles_and_descs():
        """Combine Crawlers Title and Description"""
        try :
            with open('title&desc.json', 'r') as f:
                datas = json.load(f)
                titles = ""
                descs = ""
                
                for data in datas:
                    titles += data['title']
                    descs += data['desc']
                
                return {
                    "title" : titles,
                    "desc" : descs
                }
        except : None

    def process_words_with_their_count(title_or_desc,output_mode):
        """Make a CSV File Which contains words with their count"""
        normalizer = Normalizer(
                full_cleaning=False,
                unify_chars=True,
                refine_punc_spacing=True,
                remove_extra_space=True,
                remove_puncs=False,
                remove_html=False,
                remove_stop_word=False,
                replace_email_with="<EMAIL>",
                replace_number_with=None,
                replace_url_with="",
                replace_mobile_number_with=None,
                replace_emoji_with=None,
                replace_home_number_with=None
            )
        normalizer = Normalizer(full_cleaning=True)
        normalized_text = normalizer.normalize(title_or_desc)

        pips = 'tok,kasreh' 
        nlp = language.Pipeline(pips)

        doc = nlp(normalized_text)
        dictionary = language.to_json(pips, doc)

        texts = []
        for item in dictionary[0]:
            for key, value in item.items():
                if key == "text":
                    texts.append(value)
        output = {i:texts.count(i) for i in texts}
        
        with open("result.csv",output_mode) as writtenFile :
            headers = ['Word','Count']
            writter = DictWriter(writtenFile,fieldnames=headers)

            writter.writeheader()

            for (key , value) in output.items() :
                writter.writerow({
                    'Word' : key,
                    'Count' : value
                })


Extractor.extract_data_from_res('../../eestkhdam/res.json','w')
Extractor.extract_data_from_res('../../estekhdam/res.json','a')
Extractor.extract_data_from_res('../../iranestekhdam/res.json','a')
Extractor.extract_data_from_res('../../irantalent/res.json','a')
Extractor.extract_data_from_res('../../jobinja/res.json','a')
Extractor.extract_data_from_res('../../jobvision/res.json','a')
Extractor.extract_data_from_res('../../karboom/res.json','a')

title_and_desc = Extractor.combine_titles_and_descs()
Extractor.process_words_with_their_count(title_and_desc['title'],'w')
Extractor.process_words_with_their_count(title_and_desc['desc'],'a')