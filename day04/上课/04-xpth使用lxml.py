from lxml import etree

text = '''<div class="list">1.<a href="/bbs-875052.html">阿里云服务器白嫖</a><br>2.<a href="/bbs-875026.html">k30s用那个巅峰抢</a><br>3.<a href="/bbs-866914.html">1000，收一张小天</a><br>4.<a href="/bbs-875049.html">寻求解决办法，真的好</a><br>5.<a href="/bbs-875053.html">ios14怎么改文件</a><br>6.<a href="/bbs-875054.html">8409来吃肉</a><br>7.<a href="/bbs-875032.html">k30s终于抢到了</a><br>8.<a href="/bbs-874849.html">王者太累了</a><br>9.<a href="/bbs-875050.html">又被强暴了</a></div>'''


html=etree.HTML(text)

href_list=html.xpath("//div[@class='list']/a/@href")
text_list=html.xpath("//div[@class='list']/a/text()")
# print(href_list,href_list2)

for temp in href_list:
    item=dict()
    item["href"]=temp
    item["text"]=text_list[href_list.index(temp)]
    print(item)