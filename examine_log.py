import os, sys
import pandas as pd
import numpy as np

src_log_info = r'C:\Users\DENG\Desktop\审批日志数据0703\rizhi.csv'
user_info = r'C:\Users\DENG\Desktop\审批日志数据0703\wjmuser.csv'

res_csv = r'C:\Users\DENG\Desktop\examine_log.csv'

user_unit_list, user_name_list = [], []

table_id_list = []
exam_city_personname_list = []
exam_province_personname_list = []
exam_city_date_list = []
exam_province_date_list = []

chongfu = []

#获取用户信息
def get_user_info_list(filename):
    data = pd.read_csv(filename, header=None, skiprows=1,sep=',')

    user_unit = list(data.values[:,0]) #获取用户单位
    user_name = list(data.values[:,1]) #获取用户姓名
    
    return user_unit, user_name

#获取日志信息
def get_log_info_list(filename):
    data = pd.read_csv(filename, header=None, skiprows=1,sep=',')

    log_land_id = list(data.values[:,0]) #审批岛id
    log_user_name = list(data.values[:,1]) #审批用户
    log_operation = list(data.values[:,2]) #级别（地方、省级）
    log_examine_time = list(data.values[:,4]) #审批时间
    
    return log_land_id, log_user_name, log_operation, log_examine_time

#创建写入信息列表
def create_info_list(table_id_all, exam_city_personname_all, exam_province_personname_all, exam_city_date_all, exam_province_date_all):
    try:
        info_list = []
        for table_id_1, exam_city_personname_1, exam_province_personname_1, exam_city_date_1, exam_province_date_1 in zip\
            (table_id_all, exam_city_personname_all, exam_province_personname_all, exam_city_date_all, exam_province_date_all):
            info = '"%s","%s","%s","%s","%s"' % (table_id_1, exam_city_personname_1, exam_province_personname_1, exam_city_date_1, exam_province_date_1)
            info_list.append(info)           
        return info_list
    
    except Exception as e:  
        print("执行 %s 函数发生错误：%s"  % (sys._getframe().f_code.co_name, e))
        return False 

# 写回数据内容
def write_info_file(filename, info_list):
    fw = open(filename,'w', encoding = 'UTF-8')
    fw.write('"ID","EXAM_CITY_PERSONNAME","EXAM_PROVINCE_PERSONNAME","EXAM_CITY_DATE","EXAM_PROVINCE_DATE"\n')
    
    #对于新增开发项目的内容先写入另一个文件之中，以新增模式更新数据库
    for info in info_list:
        fw.write(info)
        fw.write('\n')
    fw.close()
    
    print ('成功创建：%s' % filename)
    return True  

def get_info(log_land_id_list, log_user_name_list, log_operation_list, log_examine_time_list):
    #日志
    for land_id in log_land_id_list:
        #land_id = 3698
        if land_id in chongfu:
            continue
        chongfu.append(land_id)
        index_all = []
        log_name_all = []
        log_operation_all = []
        log_examine_time_all = []
        #获取同一岛信息
        for index, ids in enumerate(log_land_id_list):
            if ids == land_id:
                index_all.append(index)
                log_name_all.append(log_user_name_list[index])
                log_operation_all.append(log_operation_list[index])
                log_examine_time_all.append(log_examine_time_list[index])
        #获取同一岛审核人与日期
        n = log_name_all[0]
        i = 1
        j = 1
        d_name = ''
        d_date = ''
        s_name = ''
        s_date = ''
        
        for index, name in enumerate(log_name_all):
            date = log_examine_time_all[index][0:4] + '年' + log_examine_time_all[index][5:7] + '月' + log_examine_time_all[index][8:] + '日'
            
            if log_operation_all[index] == '地方自查':
                if index == 0:
                    d_name = d_name + str(i) + '、' + get_unit(name) + '：' + name + ';'
                    d_date = d_date + str(i) + '、' + date + '；'
                    i = i + 1
                
                if name == n and index != 0:
                    d_date = d_date + date + '；'
                
                if name != n:
                    d_name = d_name + str(i) + '、' + get_unit(name) + '：' + name + ';'
                    if d_date != '':
                        d_date = d_date[:-1] + ';'
                    d_date = d_date + str(i) + '、' + date + '；'
                    i = i + 1
            else:
                if index == 0:
                    s_name = s_name + str(j) + '、' + get_unit(name) + '：' + name + ';'
                    s_date = s_date + str(j) + '、' + date + '；'
                    j = j + 1
                
                if name == n and index != 0:
                    s_date = s_date + date + '；'
                
                if name != n:
                    s_name = s_name + str(j) + '、' + get_unit(name) + '：' + name + ';'
                    if s_date != '':
                        s_date = s_date[:-1] + ';'
                    s_date = s_date + str(j) + '、' + date + '；'
                    j = j + 1
            n = name
        d_name = d_name[:-1]
        d_date = d_date[:-1]
        if s_name != '':
            s_name = s_name[:-1]
            s_date = s_date[:-1]
        exam_city_personname_list.append(d_name)
        exam_city_date_list.append(d_date)
        exam_province_personname_list.append(s_name)
        exam_province_date_list.append(s_date)
        table_id_list.append(land_id)
        
        
#获取单位         
def get_unit(name):
    for index, a in enumerate(user_name_list):
        if name == a:
            return user_unit_list[index]
    return


if __name__ == "__main__":
    user_unit_list, user_name_list = get_user_info_list(user_info)
    
    log_land_id_list, log_user_name_list, log_operation_list, log_examine_time_list = [], [], [], []

    log_land_id_list, log_user_name_list, log_operation_list, log_examine_time_list = get_log_info_list(src_log_info)

    get_info(log_land_id_list, log_user_name_list, log_operation_list, log_examine_time_list)
    info_list = create_info_list(table_id_list, exam_city_personname_list, exam_province_personname_list, exam_city_date_list, exam_province_date_list)
    write_info_file(res_csv, info_list)
    