import requests

url='https://bkimg.cdn.bcebos.com/pic/730e0cf3d7ca7bcbaff87c79b1096b63f724a8e1?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg'
r=requests.get(url)
with open('test.jpg',"w b") as  f:
    f.write(r.content)