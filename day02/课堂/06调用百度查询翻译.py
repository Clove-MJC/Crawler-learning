import json
import requests
#设置url
url = "https://fanyi.baidu.com/sug"
#设置请求头
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
#设置参数
params = {"kw": "good"}
#发送post请求
r = requests.post(url=url, headers=headers, params=params)
#格式进行转换字典转换成字符串
text_dict =json.loads(r.text)
k=text_dict.get("data")[0].get('k')
v=text_dict.get("data")[0].get('v')
print(k)
print(v)

print(r.text)
