import requests, random

response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/hello')
if ("example" in response.json()[0]['meanings'][0]['definitions'][0]):
    print(1)
else:
    print(2)
print(response.json()[0]['meanings'][0]['definitions'][0]['example'])

