import requests


r=requests.get("http://www.baidu.com")
#进行解码
r.encoding='utf-8'

print(r.text)

#直接用这种方法也可以解码
print(r.content.decode())