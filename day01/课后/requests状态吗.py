import requests


response=requests.get("http://www.baidu.com")

a=response.status_code
#断言
assert response.status_code==200

print(a)