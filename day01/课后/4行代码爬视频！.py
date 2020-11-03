#导入网络请求库
import requests
#发送请求
r=requests.get("http://v29-dy.ixigua.com/630419ab4ef75eb5bf0b29484113666c/5f9fda2f/video/tos/cn/tos-cn-ve-15/e315af7ba404448f846843cf2c35e10d/?a=1128&br=2994&bt=998&cr=0&cs=0&cv=1&dr=0&ds=6&er=&l=20201102170622010198067028520BC4FA&lr=&mime_type=video_mp4&qs=0&rc=ajM1ZWt1aHU2eDMzZmkzM0ApNjo8ZjlkPDtnNzU3ZTY4O2c1czVka3FlMGNfLS0tLS9zczM1MmI0MTU0LzAwXzQwXy06Yw%3D%3D&vl=&vr=")
#b保存
with  open("a.mp4","wb")as  f:
    f.write(r.content)