# -*- coding: utf-8 -*-
import os,sys
import pandas as pd
import numpy as np

class err:
    _UNKNOWN = 10

dest_info_csv = r'C:\Users\DENG\Desktop\农林牧.csv'        #需要合并的表（用岛类型为4：农林牧业）
src_info_csv =  r'C:\Users\DENG\Desktop\权属证书.csv'         #需读取数据表（最大序号项目，用岛类型为空，其他权属为：林地四证）
all_info_csv = r'C:\Users\DENG\Desktop\islanduseinfo_part.csv'               #完整信息表

res_csv = r'C:\Users\DENG\Desktop\new_info.csv'             #写入结果的表

#读取信息
def get_info_list(filename):
    data = pd.read_csv(filename, header=None, skiprows=[0,0], sep=',') 
    part_id_all = list(data.values[:, 0])   #岛屿开发项目id值
    info_id_all = list(data.values[:, 1])   #岛屿id值

    type_all = list(data.values[:, 3])      #用岛类型
    
    #其余需要组合的字段

    cert_id_all = list(data.values[:, 12])  #证书类型
    cert_id_all = edit_nan_value(cert_id_all)

    contract_name = list(data.values[:, 16])  #审批合同名称
    contract_name = edit_nan_value(contract_name)
    
    contract_code = list(data.values[:, 17])  #审批合同编号
    contract_code = edit_nan_value(contract_code)

    contract_filename = list(data.values[:, 18])  #审批合同扫描文件名
    contract_filename = edit_nan_value(contract_filename)
    
    return part_id_all, info_id_all, type_all, cert_id_all, contract_name, contract_code, contract_filename
    

def edit_nan_value(value_list):
    try:
        res_value = []
        for value in value_list:
            if isinstance(value, float) and np.isnan(value):
                value = ''
            res_value.append(value)
        
        return res_value
    
    except Exception as e:
        print("执行 %s 函数发生错误：%s"  % (sys._getframe().f_code.co_name, e))
        return err._UNKNOWN


#创建写入信息列表
def create_info_list(write_part_id_all, write_type_all, write_cert_id_all, write_contract_name_all, write_contract_code_all, write_contract_filename_all):
    try:
        info_list = []
        for write_part_id, write_type, write_cert_id, write_contract_name, write_contract_code, write_contract_filename in zip(write_part_id_all, write_type_all, write_cert_id_all, write_contract_name_all, write_contract_code_all, write_contract_filename_all):
            info = '"%s","%s","%s","%s","%s","%s"' % (write_part_id, write_type, write_cert_id, write_contract_name, write_contract_code, write_contract_filename)
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

if __name__ == '__main__': 
    write_part_id_all, write_type_all, write_cert_id_all, write_contract_name_all, write_contract_code_all, write_contract_filename_all= [], [], [], [], [], []
    
    #1、读取源、目的两个csv文件
    src_part_id_all, src_info_id_all, src_type_all, src_cert_id_all, src_contract_name_all, src_contract_code_all, src_contract_filename_all = get_info_list(src_info_csv)
    dest_part_id_all, dest_info_id_all, dest_type_all, dest_cert_id_all, dest_contract_name_all, dest_contract_code_all, dest_contract_filename_all = get_info_list(dest_info_csv)
    all_part_id_all, all_info_id_all, all_type_all, all_cert_id_all, all_contract_name_all, all_contract_code_all, all_contract_filename_all = get_info_list(all_info_csv)
    
    src_num = len(src_part_id_all)
    dest_num  = 0
    src_update_num = 0
    infoid_list = []

    for src_part_id_1, src_info_id_1, src_type_1, src_cert_id_1, src_contract_name_1, src_contract_code_1, src_contract_filename_1 in zip(src_part_id_all, \
        src_info_id_all, src_type_all, src_cert_id_all, src_contract_name_all, src_contract_code_all, src_contract_filename_all):
        
        if src_info_id_1 in dest_info_id_all:
            dest_num+= 1

            dest_index = dest_info_id_all.index(src_info_id_1)
            dest_part_id = dest_part_id_all[dest_index]
            
            all_index = all_part_id_all.index(dest_part_id)
            
            #将源数据合并至目的字段之中
            #其他证书
            all_cert_id = all_cert_id_all[all_index]
            if all_cert_id != '' and src_cert_id_1 != '':
                all_cert_id = str(all_cert_id) + ',' + str(src_cert_id_1)
            elif all_cert_id == '' and src_cert_id_1 != '':
                all_cert_id = src_cert_id_1
                
            
            
            #审批合同名称
            all_contract_name = all_contract_name_all[all_index]
            if all_contract_name != '' and src_contract_name_1 != '':
                all_contract_name = str(all_contract_name) + '，' + str(src_contract_name_1)
            elif all_contract_name == '' and src_contract_name_1 != '':
                all_contract_name = src_contract_name_1
            

            #审批合同编号
            all_contract_code = all_contract_code_all[all_index]
            if all_contract_code != '' and src_contract_code_1 != '':
                all_contract_code = str(all_contract_code) + '，' + str(src_contract_code_1)
            elif all_contract_code == '' and src_contract_code_1 != '':
                all_contract_code = src_contract_code_1
            

            #审批合同文件扫描名
            all_contract_filename = all_contract_filename_all[all_index]
            if all_contract_filename != '' and src_contract_filename_1 != '':
                all_contract_filename = str(all_contract_filename) + '，' + str(src_contract_filename_1)
            elif all_contract_filename == '' and src_contract_filename_1 != '':
                all_contract_filename = src_contract_filename_1
            


            write_part_id_all.append(dest_part_id)
            write_type_all.append('4')
            write_cert_id_all.append(all_cert_id)
            write_contract_name_all.append(all_contract_name)
            write_contract_code_all.append(all_contract_code)
            write_contract_filename_all.append(all_contract_filename)

            infoid_list.append(src_info_id_1)

        else:
            write_part_id_all.append(src_part_id_1)
            write_type_all.append('4')
            write_cert_id_all.append(src_cert_id_1)  
            #证书扫描件  
            write_contract_name_all.append(src_contract_name_1)
            write_contract_code_all.append(src_contract_code_1)
            write_contract_filename_all.append(src_contract_filename_1)
            src_update_num +=1

    #重新输出csv文件
    info_list = create_info_list(write_part_id_all, write_type_all, write_cert_id_all, write_contract_name_all, write_contract_code_all, write_contract_filename_all)
    write_info_file(res_csv, info_list)
    #print('src_num=%d, dest_num=%d, src_update_num=%d' % (src_num, dest_num, src_update_num))
    #print(infoid_list)