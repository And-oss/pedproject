import requests
from config import api , id

prompt = {
    "modelUri": f"gpt://{id}/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.8,
        "maxTokens": "3000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты ассистент дроид, способный писать код на bash, только на bash."
        },
        {
            "role": "user",
            "text": "привет , сможешь написать привет мир"
        }
    ]
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {api}"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text

with open('file.json' , 'w') as f:
    f.write(result)
    f.close()

print(result)