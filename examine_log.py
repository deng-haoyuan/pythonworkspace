import os, sys
import pandas as pd
import numpy as np

src_log_info = r'C:\Users\DENG\Desktop\审批日志数据0703\rizhi.csv'
land_id_info = r'C:\Users\DENG\Desktop\审批日志数据0703\islanduseinfo.csv'
user_info = r'C:\Users\DENG\Desktop\审批日志数据0703\wjmuser.csv'

#获取海岛id
def get_land_id_list(filename):
    data = pd.read_csv(filename, header=None, skiprows=1, sep=',')
    land_id = list(data.values[:0]) #岛id
    return land_id

#获取用户信息
def get_user_info_list(filename):
    data = pd.read_csv(filename, header=None, skiprows=1,sep=',')

    user_unit = list(data.values[:0]) #获取用户单位
    user_name = list(data.values[:1]) #获取用户姓名
    
    return user_unit, user_name

#获取日志信息
def get_log_info_list(filename):
    data = pd.read_csv(filename, header=None, skiprows=1,sep=',')

    log_land_id = list(data.values[:0]) #审批岛id
    log_user_name = list(data.values[:1]) #审批用户
    log_examine_time = list(data.values[:2]) #审批时间
    
    return log_land_id, log_user_name, log_examine_time

#创建写入信息列表
def create_info_list(xx, xx):
    try:
        info_list = []
        for xx, xx in zip(xx, xx):
            info = '"%s","%s"' % (xx, xx)
            info_list.append(info)           
        return info_list
    
    except Exception as e:  
        print("执行 %s 函数发生错误：%s"  % (sys._getframe().f_code.co_name, e))
        return False 

# 写回数据内容
def write_info_file(filename, info_list):
    fw = open(filename,'w', encoding = 'UTF-8')
    fw.write('"ID","TYPE_NAME","OTHER_CERTIFICATE","EXAMCONTACT_NAME","EXAMCONTACT_CODE","EXAMCONTACT_FILENAME"\n')
    
    #对于新增开发项目的内容先写入另一个文件之中，以新增模式更新数据库
    for info in info_list:
        fw.write(info)
        fw.write('\n')
    fw.close()
    
    print ('成功创建：%s' % filename)
    return True  