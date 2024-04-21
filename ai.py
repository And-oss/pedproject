api = "AQVN0TlD2PWbz_NsY_fVd4X13lp0g3xz8GIvz_cv"
id = "b1go51mogaeuh0gh7qbc"
import requests

prompt = {
    "modelUri": f"gpt://{id}/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
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
print(result)