import requests


response=requests.get("http://www.baidu.com")

a=response.status_code

assert response.status_code==300

print(a)