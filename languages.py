import requests
import json
import os

data_str="""{
    "About": {
        "zh": "关于"
    },
    "About the App": {
        "zh": "退出APP"
    },
    "Clear Context": {
        "zh": "清除所有上下文"
    }
}"""

langs_data=json.loads(data_str)

def UText(k):
    l = os.getenv("ULANG") if os.getenv("ULANG") else "zh"
    if k in langs_data:
        if l in langs_data[k]:
            return langs_data[k][l] if langs_data[k][l] else k
        else:
            print(f"not supported lang: {l}")
            request_online(k,l)
            return k
    else:
        request_online(k,l)
        return k

def request_online(k,l):
    api_addr = "http://127.0.0.1:1850"
    project_id = "123"
    url = f"{api_addr}/{project_id}/{k}/{l}"  # Replace with the actual URL of your API endpoint

    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()["result"]
        return result
    else:
        print(f"Failed to get data. Status code: {response.status_code}")