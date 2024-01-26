import requests
import os
import json
import base64

def v_set(k, v):
    json_value = json.dumps(v)
    b64_value = base64.b64encode(json_value.encode()).decode()
    url = f"{os.environ['KV_REST_API_URL']}/set/{k}/{b64_value}"
    headers = {"Authorization": f"Bearer {os.environ['KV_REST_API_TOKEN']}"}
    response = requests.get(url, headers=headers)
    return response.json()

def v_get(k):
    url = f"{os.environ['KV_REST_API_URL']}/get/{k}"
    headers = {"Authorization": f"Bearer {os.environ['KV_REST_API_TOKEN']}"}
    response = requests.get(url, headers=headers)
    if "result" in response.json():
        b64_value = response.json()["result"]
        json_value = base64.b64decode(b64_value.encode()).decode()
        value = json.loads(json_value)
        return value
    else:
        return None