import requests
import json

url = "https://m.lagou.com/listmore.json?pageNo=2&pageSize=15"
headers= {
    "User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

r = requests.get(url, headers =headers )

jason_dict = json.loads(r.content.decode())
jason=r.json()
# print(jason_dict)
    # content=jason.get("result")
    # for tem in content:
    #     print(tem)
#
jsaaa=jason_dict["content"]["data"]['page']['result']

for tem in  jsaaa:
    print(tem['positionName'])