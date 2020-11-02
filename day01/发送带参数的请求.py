import requests
headers={'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
params={"wd":"python牛逼么"}

url_temp="http://www.baidu.com"

r=requests.get(url_temp,headers=headers,params=params)
print(r.request.url)

#使用format方法拼接格式化

url="http://www.baidu.com/s?wd={}".format("马晋川")
r=requests.get(url,headers=headers)
print(r.request.url)