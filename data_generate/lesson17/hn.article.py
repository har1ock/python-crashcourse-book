import requests
import json

# Зробити виклик через API та зберегти відповідь.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Дослідити структуру даних.
response_dict = r.json()
readeble_file = 'data_generate/lesson17/readeble_hn_data.json'
with open(readeble_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
    