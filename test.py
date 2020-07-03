import os, sys
import shutil
import pandas as pd
import numpy as np

src_path = r'E:\test\111\111.txt'
dest_path = r'E:\test\333'

#shutil.copy(src_path, dest_path)

#index = os.path.dirname(src_path).rfind('\\')
#parend_filename = os.path.dirname(src_path)[index + 1:]
#print(parend_filename)

a = '1234567'
b = '124'

print(b in a or '12' in b)