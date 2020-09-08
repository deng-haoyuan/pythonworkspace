import os, sys
import shutil
import pandas as pd
import numpy as np
import shapefile

#src_path = r'E:\test\111\111.txt'
#dest_path = r'E:\test\333'

#shutil.copy(src_path, dest_path)

#index = os.path.dirname(src_path).rfind('\\')
#parend_filename = os.path.dirname(src_path)[index + 1:]
#print(parend_filename)

#a = '1234567'
#b = '124'

#print(b in a or '12' in b)

filename = r'C:\Users\DENG\Desktop\111.csv'

list_test = []
data = pd.read_csv(filename, header=None, skiprows=1, sep=',')

xh = list(data.values[:, 0])
name = list(data.values[:, 1])
age = list(data.values[:, 2])
list_test.append(xh)
list_test.append(name)
list_test.append(age)
#print(list_test[0][0])
print(os.path.exists(filename) is False)

#输出下标及对应位置的数值
# s1 = [1, 2, 3, 4, 5, 6]
# for index, nums in enumerate(s1):
#     print(index,nums)

# list1 = []
# list1.append('')
# list1.append('')
# list1.append('')
# list1.append('1')
# print(list1)
# path = r'C:\Users\DENG\Desktop\工作\资产清查系统\海域权属数据样例\海域权属数据.shp'
# shps = shapefile.Reader(path, encoding='gb18030')
# print(shps.fields)
#p = r'C:\Users\DENG\Desktop\wjmhd\福建省\漳州市\漳浦县\3506231001517-漳浦东礁\佐证材料1'
#print(os.path.exists(p))
# i = 0
# def test1():
#     i = 100
#     test2()
#     print(i)
# def test2():
#     i = 200
# if __name__ == "__main__":
#     test1()
#     print(i)