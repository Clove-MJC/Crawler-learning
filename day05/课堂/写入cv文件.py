import csv
headers = ['班级', '姓名', '性别', '手机号', 'QQ']

rows = [
    ["18级Python", '小王', '男', '13146060xx1', '123456xx1'],
    ["18级Python", '小李', '男', '13146060xx2', '123456xx2'],
    ["19级Python", '小赵', '女', '13146060xx3', '123456xx3'],
    ["19级Python", '小红', '女', '13146060xx4', '123456xx4'],
]

with open('test.csv', 'w') as f:
    # 创建一个csv的writer对象，这样才能够将写入csv格式数据到这个文件
    f_csv = csv.writer(f)
    # 写入一行（我们用第一行当做表头）
    f_csv.writerow(headers)
    # 写入多行行（当做数据）
    f_csv.writerows(rows)