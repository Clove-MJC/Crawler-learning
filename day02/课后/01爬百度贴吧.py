import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

    # 构造url列表
    def get_url_list(self):
        # url_list = []
        # for i in range(20 ):
        #     url_list.append(self.url_temp.format(i * 50))
        # return url_list
        #使用简化版本构造url
        return [self.url_temp.format(i*50) for i in range(20)]

    # 发送请求
    def parse_url(self, url):
        print(url)
        response = requests.get(url, self.headers)
        return response.content.decode()

    # 保存html字符串
    def save_html(self, html_str, page_num):
        file_path = "{}第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding='utf-8') as  f:
            f.write(html_str)
            f.close()

    # 实现主要逻辑
    def run(self):
        # 1。构造url列表
        url_list = self.get_url_list()
        # 2便利发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_num = url_list.index(url) + 1  # 页面
            self.save_html(html_str, page_num)


if __name__ == "__main__":
    tieba_spider = TiebaSpider("iphone")
    tieba_spider.run()
