import requests
import json
url='https://webapi.qingting.fm/api/mobile/rank'

headers= {
    "User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

r = requests.get(url, headers =headers )

jason=r.json()
print(jason)
rank_list=jason.get('rankinglist')
for temp in rank_list:
    print(temp.get('title'),temp.get("playCount"))