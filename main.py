import requests
from pprint import pprint as print

sura = 1
oyat = 4
tafsir = "uzb-muhammadsodikmu"

url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"

response = requests.get(url_oyat)
# print(response.status_code)
res = response.json()
print(res['text'])