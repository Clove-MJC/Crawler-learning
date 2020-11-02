import requests

response=requests.get("http://www.baidu.com")

print(response.headers)
#默认请求头,打印出来知道你不是正常用户
print(response.request.headers)

