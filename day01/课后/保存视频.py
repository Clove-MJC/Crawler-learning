import requests
import os

# 下载图片URL
url = 'http://v29-dy.ixigua.com/630419ab4ef75eb5bf0b29484113666c/5f9fda2f/video/tos/cn/tos-cn-ve-15/e315af7ba404448f846843cf2c35e10d/?a=1128&br=2994&bt=998&cr=0&cs=0&cv=1&dr=0&ds=6&er=&l=20201102170622010198067028520BC4FA&lr=&mime_type=video_mp4&qs=0&rc=ajM1ZWt1aHU2eDMzZmkzM0ApNjo8ZjlkPDtnNzU3ZTY4O2c1czVka3FlMGNfLS0tLS9zczM1MmI0MTU0LzAwXzQwXy06Yw%3D%3D&vl=&vr='

# 保存地址
path = "/Users/yuer/PycharmProjects/爬虫/"

# 构造下载图片url
down = path + url.split('/')[-1]+".mp4"
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
    print("爬取失败:",str(e))