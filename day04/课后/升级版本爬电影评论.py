from lxml import etree
import requests


class DoubanSpider:
    def __init__(self):
        self.url_temp = "https://movie.douban.com/subject/1292052/comments?start={}&limit=20&status=P&sort=new_score"
        self.headers = {
            "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
            "cookie": '''ll="118171"; bid=YZ9qfYxNfQo; __utma=30149280.1204775035.1604544578.1604544578.1604544578.1; __utmc=30149280; __utmz=30149280.1604544578.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.24902190.1604544578.1604544578.1604544578.1; __utmc=223695111; __utmz=223695111.1604544578.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ct=y; _vwo_uuid_v2=D9756E312DF5551AEAF6A93EE6B2886EF|c159c5ce2c84b28395327d2d319e784e; ap_v=0,6.0; dbcl2="226119532:HEGiQELe1/I"; ck=8DOt; push_noty_num=0; push_doumail_num=0''',
            "Accept": '''text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'''

        }

    # 构造url列表
    def get_url_list(self):
        return [self.url_temp.format(i * 20) for i in range(5)]

    # 发送请求
    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.text

    # 保存html字符串
    def save_html(self, html_str, page_num):
        file_path = "第{}页.html".format(page_num)

        with open(file_path, "a", encoding='utf-8') as  f:
            html_str = etree.HTML(html_str)
            html_str = html_str.xpath('//span[@class="short"]/text()')
            for item in html_str:
                f.write(str(item)+'\n')

                # 实现主要逻辑

    def run(self):
        # 1。构造url列表
        url_list = self.get_url_list()
        # 2遍历发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_num = url_list.index(url) + 1  # 页面
            self.save_html(html_str, page_num)


if __name__ == "__main__":
    douban_spider = DoubanSpider()
    douban_spider.run()
