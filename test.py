from config import api_token, secret_token
import requests
def __init__(self, url, api_key, secret_key):
    self.URL = url
    self.AUTH_HEADERS = {
        'X-Key': f'Key {api_token}',
        'X-Secret': f'Secret {secret_token}',
    }
def get_model(self):
    response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
    data = response.json()
    return data[0]['id']
[
	{
		"id": 1,
		"name": "string",
		"version": 1.0,
		"type": "TEXT2IMAGE"
	}
]
{
  "type": "GENERATE",
  "style": "string",
  "width": 1024,
  "height": 1024,
  "num_images": 1,
  "negativePromptUnclip": "яркие цвета, кислотность, высокая контрастность",
  "generateParams": {
    "query": "Пушистый кот в очках",
    "images": ["string"]
  }
}
