import os, sys
import shutil
import pandas as pd
import numpy as np

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

data = pd.read_csv(filename, header=None, skiprows=1, sep=',')

xh = list(data.values[:, 0])
name = list(data.values[:, 1])
age = list(data.values[:, 2])

#print(xh)

#输出下标及对应位置的数值
# s1 = [1, 2, 3, 4, 5, 6]
# for index, nums in enumerate(s1):
#     print(index,nums)

list1 = []
list1.append('')
list1.append('')
list1.append('')
list1.append('1')
print(list1)