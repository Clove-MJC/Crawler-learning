import requests

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
url="http://www.baidu.com"
reponse=requests.get(url,headers=header)
print(reponse.content.decode())