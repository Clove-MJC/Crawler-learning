import requests


url="http://www.baidu.com"


response=requests.get(url)

#这是打印状态吗
print(response.status_code)
#这是看是什么类型
print(type(response.text))


