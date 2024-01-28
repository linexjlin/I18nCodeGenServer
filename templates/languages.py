import requests
import os

langs_data={languages_json}


def UText(k):
    l = os.getenv("ULANG") if os.getenv("ULANG") else "default"
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
    url = f"{api_addr}/{project_id}/key"  # Replace with the actual URL of your API endpoint

    params = {'k': k,'l':l}
    response = requests.get(url,  params=params)

    if response.status_code == 200:
        result = response.json()["result"]
        return result
    else:
        print(f"Failed to get data. Status code: {response.status_code}")