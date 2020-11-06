import json

import requests

import jsonpath


url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'

headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

response = requests.get(url,headers = headers)

html_str = json.loads(response.content.decode())

# print(html_str)

#从根节点开始，获取所有key为name的值
city_list = jsonpath.jsonpath(html_str, '$..name')

print(city_list)
