#导入网络请求库
import requests
#发送请求
r=requests.get("https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2093143442,3189902132&fm=26&gp=0.jpg")
#b保存
with  open("a.png","wb")as  f:
    f.write(r.content)