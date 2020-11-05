from lxml import etree
import requests

url='https://movie.douban.com/subject/1292052/comments?status=P'

headers = {
    "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"

 }


r=requests.get(url,headers=headers)
text=r.text

html = etree.HTML(text)
href_list=html.xpath('//span[@class="short"]/text()')
for item in href_list:
    print(item)