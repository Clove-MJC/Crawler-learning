import requests
import os

# 下载图片URL
url = 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png'

# 保存地址
path = "/Users/yuer/PycharmProjects/爬虫/"

# 构造下载图片url
down = path + url.split('/')[-1]
try:
    # 判断目录是否存在
    if not os.path.exists(path):
        os.mkdir(path)
    # 如果url不存在,则开始下载
    if not os.path.exists(down):
        r = requests.get(url)
        print(r)
        # 开始写文件，wb代表写二进制文件
        with open(down,'wb') as f:
            # 图片以二进制形式保存（r.content）
            f.write(r.content)
        print("图片下载成功")
    else:
        print("图片已经存在.")

except Exception as e :
    print("爬取失败:",str(e))