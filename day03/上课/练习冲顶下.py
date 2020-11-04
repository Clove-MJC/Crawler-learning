import requests

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

r=requests.get("http://www.360buy.com",headers=header,allow_redirects=False)
print(r.url)
print(r.status_code)
print(r.headers)
print(r.headers.get("Location"))
print(r.history)
