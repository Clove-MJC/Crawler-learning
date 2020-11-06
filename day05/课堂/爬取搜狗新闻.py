import requests
from bs4 import BeautifulSoup


url = "https://weixin.sogou.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}

r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, features="lxml")
# 获取标签

ul_tag = soup.select('ul[class="news-list"]')
h3_list = ul_tag[0].select("h3")
for temp_tag in h3_list:
    print(temp_tag.select("a")[0].get_text(), temp_tag.select("a")[0].get("href"))
    print()
