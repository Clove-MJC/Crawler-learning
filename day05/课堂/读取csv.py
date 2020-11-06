import csv

with open('test.csv')as  f:
    fs_csv=csv.reader(f)
    print(fs_csv)
