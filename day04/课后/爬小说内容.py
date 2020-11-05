import requests
from lxml import etree

url = 'http://book.zongheng.com/chapter/957547/60100317.html'
headers = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",

}



for i  in  range(20):
    r = requests.get(url, headers)
    text = r.text
    html = etree.HTML(text)
    html_xs = html.xpath('//div[@class="content"]/p/text()')

    next_url = html.xpath('//a[@class="nextchapter"]/@href')
    title=html.xpath('//div[@class="title_txtbox"]/text()')
    print(title)
    url=str(next_url)[2:-2]
    print(url)
    with open('小说/%s.txt'%title, 'a', encoding='utf-8')as f:
        for item in html_xs:
            f.write(item + '\n')