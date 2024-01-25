import os
import json

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
        self.data = {}
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
    
    def export_code_lang(self,langs,lang_subfix):
        self.add_langs(langs)
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

