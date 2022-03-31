import requests

response = requests.put('https://jsonbase.com/demo_bucket/xxxddd', headers=headers, params=data)

print(response.json())