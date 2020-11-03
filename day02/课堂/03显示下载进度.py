# 导入网络请求库
import requests

# 发送请求
url = "http://v26-dy.ixigua.com/65d38396206f04596db9ac8abedc6b44/5fa0c50e/video/tos/cn/tos-cn-ve-15/e315af7ba404448f846843cf2c35e10d/?a=1128&br=2994&bt=998&cr=0&cs=0&cv=1&dr=0&ds=6&er=&l=2020110309482901019806704224557838&lr=&mime_type=video_mp4&qs=0&rc=ajM1ZWt1aHU2eDMzZmkzM0ApNjo8ZjlkPDtnNzU3ZTY4O2c1czVka3FlMGNfLS0tLS9zczM1MmI0MTU0LzAwXzQwXy06Yw%3D%3D&vl=&vr="

r = requests.get(url=url, stream=True)
# b保存
r_body_lenth = int(r.headers.get("Content-Length"))
with  open("a.mp4", "wb")as  f:
    write_all = 0
    for chunk in r.iter_content(chunk_size=100):
        write_all += f.write(chunk)
        print("下载进度:%02.2f%%" % (100 * write_all / r_body_lenth))
