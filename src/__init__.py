import requests
import json

def truncate_response(response):
    parts = response.split('<think>')
    if len(parts) > 1:
        before_think = parts[0]
        remaining = parts[1].split('</think>')
        if len(remaining) > 1:
            result = before_think + remaining[1]
            print(result)
        else:
            print("No second part")
    else:
        print("No think part")

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application-json"
}

data = {
    "model": "deepseek-r1:1.5b",
    "prompt": "Why is the sky blue?",
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_text = response.content
    data = json.loads(response_text)
    truncate_response(data["response"])