import os
import json
import threading
from utils import extract_code_from_markdown
from ai import query_ai
from dotenv import load_dotenv
import os

load_dotenv()

"""
{
    "About": {
        "zh": "关于"
    },
    "About the App": {
        "zh": "退出APP"
    },
    "Clear Context": {
        "zh": "清除所有上下文"
    }
}
"""
class Core:
    def __init__(self, id=""):
        self.id = id
        default_data={
            "APP": {
                "default":"APP",
            }
        }
        self.data = default_data
        self.data_path = f"data/{id}"
        self.data_json = f"data/{id}/data.json"
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
        self.load()

    def load(self):
        if  os.path.isfile(self.data_json):
            self.data = json.load(open(self.data_json, "r"))

    def save(self):
        json.dump(self.data, open(self.data_json, "w"),ensure_ascii=False,indent=4)

    def update(self,data):
        self.data = data

    def delete(self,k):
        del self.data[k]

    def add(self,k):
        self.data[k]={"default":k}

    def add_lang(self,l):
        for k in self.data:
            if l not in self.data[k]:
                self.data[k][l]=""

    def add_langs(self,ls):
        for l in ls:
            self.add_lang(l)

    def get(self,k,l):
        if k in self.data:
            if l in self.data[k]:
                return self.data[k][l] if self.data[k][l] else k
            else:
                print(f"not supported lang: {l}")
                return k
        else:
            self.add(k)
            self.save()
            return k
        return k
    
    def merge_in(self,old_key,new_translated):
        translated = self.data[old_key]
        for l in new_translated:
            translated[l]=new_translated[l]
        self.data[old_key]=translated

    def clean_translated(self):
        new_data = {}
        for key, translations in self.data.items():

            translation_finish = True
            for lang, text in translations.items():
                if len(text)==0:
                    translation_finish=False
                    break
                
            if translation_finish:
                print("all translaion complete",translations)
                continue

            has_translation = False
            new_translations = {}
            for lang, text in translations.items():
                if text and not has_translation:
                    has_translation = True
                elif text and has_translation:
                    continue
                new_translations[lang] = text
            new_data[key] = new_translations
        return new_data

    def translate(self):
        #batches = []
        data = self.clean_translated()
        batch_size=10
        keys = list(data.keys())
        num_batches = len(keys) // batch_size + (1 if len(keys) % batch_size != 0 else 0)

        thread=None
        for i in range(num_batches):
            start_idx = i * batch_size
            end_idx = min(start_idx + batch_size, len(keys))
            batch_keys = keys[start_idx:end_idx]
            batch = {key: data[key] for key in batch_keys}
            thread = threading.Thread(target=self.translate_batch, args=(batch,))
            thread.start()
            #batches.append(batch)

        if thread:
            thread.join()

    def translate_batch(self,batch_data):
        src_json = json.dumps(batch_data,ensure_ascii=False,indent=2)
        ## translate by AI
        ## update one by one
        prompt = [{"role":"system","content":"Be a helpful assistant."}]
        content = f"""
下面的 json 是一个软件的多国语言软件的 UI翻译，帮我补全剩余的翻译，直接给我结果并以```json开头
```json
{src_json}
```
"""
        print(content)
        ocr_message = {"role":"user","content":content}
        prompt.append(ocr_message)
        res = query_ai(messages=prompt)
        codes = extract_code_from_markdown(res)

        if len(codes)>0:
            res_batch_data = json.loads(codes[0])
            print(res_batch_data)
            for k in res_batch_data:
                self.merge_in(k,res_batch_data[k])
        
    def export_code_lang(self,langs,lang_subfix):
        self.add_langs(langs)
        self.translate()
        self.save()
        # define the file path
        file_path = f"templates/languages{lang_subfix}"

        # read the content of the file
        with open(file_path, "r") as file:
            server_addr = os.getenv("SERVER_API_ADDR") if os.getenv("SERVER_API_ADDR") else "http://127.0.0.1:1850"
            languages_json = json.dumps(self.data,ensure_ascii=False,indent=4)
            file_content = file.read()
            file_content= file_content.replace("{languages_json}",languages_json,-1).replace(
                "{api_addr}",server_addr,-1
            ).replace(
                "{project_id}",self.id,-1
            )
            return file_content