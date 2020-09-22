import os
import shutil
import pandas as pd
import zipfile
import datetime
from flask import Flask
from wsgiref.simple_server import make_server

file_path = r'C:\Users\DENG\Desktop\file.csv'
folder_path = r'C:\Users\DENG\Desktop\folder.csv'

dest_path = r'E:\wjmhd' #目标路径

files_path = r'E:\wjmhd\测试文件'#文件路径

folder_id = []
folder_name = []
folder_parent = []

file_name= []
file_parent_folder = []
file_name_old = []
#2102831000444-盘坨子
#fp_id = '8ca38dfc-528e-4ccb-9f78-7aaca4dba155'

#读取csv
def get_info_list(filename):
    data = pd.read_csv(filename, header=None, skiprows=[0,0], sep=',')

    list1 = list(data.values[:, 0])
    list2 = list(data.values[:, 1])
    list3 = list(data.values[:, 2])

    return list1, list2, list3

#删除文件
def delete_folder(path, file_news):
    try:
        shutil.rmtree(path)
    except Exception as e:
        return '删除文件夹失败, %s' % e
    return 'success'

#压缩岛文件夹为zip
def zip_ya(fp_ls, d_path):
    index = folder_id.index(fp_ls)
    folder_dir = folder_name[index]
    path = os.path.join(d_path, folder_dir)
    file_news = path + '.zip'
    
    filelist = []
    if os.path.exists(file_news):
        delete_folder(path, file_news)
        return '文件已存在'
    try:    
        for root, dirs, files in os.walk(path):
            # 不过滤空文件夹
            if not files and not dirs:
                filelist.append(root)
            for name in files:
                filelist.append(os.path.join(root, name))
        zf = zipfile.ZipFile(file_news, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(path):]
            zf.write(tar,arcname)
        zf.close()      
    except Exception as e:
        return '压缩文件夹失败：%s' % e
    return delete_folder(path, file_news)

#创建海岛文件夹
def creat_land_folder(fp_ls):
    try:
        d_path = dest_path
        path = os.path.join(d_path, folder_name[folder_id.index(fp_ls)])
        os.mkdir(path)
        creat_folder(fp_ls, path)
    except Exception as e:
        return '创建文件夹失败：%s' % e
    return zip_ya(fp_ls, d_path)

#创建下级文件目录
def creat_folder(fp_ls, d_path):
    try:
        index = 0
        for fp in folder_parent:
            if fp == fp_ls:
                path = os.path.join(d_path, folder_name[index])
                os.mkdir(path)
                id_ls = folder_id[index]
                #复制文件
                copy_file(id_ls, path)
                creat_folder(id_ls, path)
                id_ls = ''
            index = index + 1
    except Exception as e:
        return '创建文件夹失败：%s' % e

def copy_file(fpf, new_file_path):
    try:
        index_1 = 0
        for fpf_ls in file_parent_folder:
            if fpf == fpf_ls:               
                old_file_path = os.path.join(files_path, file_name_old[index_1])
                
                #if file_name_old[index_1] in list_file_old:

                shutil.copy(old_file_path, new_file_path)
                src_file = os.path.join(new_file_path, file_name_old[index_1])
                dst_file = os.path.join(new_file_path, file_name[index_1])

                os.rename(src_file, dst_file)

            index_1 = index_1 + 1

    except Exception as e:
        return '复制文件失败：%s' % e

#获取目录下所有文件（目录下没有文件夹）
def get_all_file(path, list_name):
    for filename in os.listdir(path):
        list_name.append(filename)
    print('获取文件列表')
    

app = Flask(__name__)
app.debug=True
@app.route('/')
def hello_world():
    return 'index'

@app.route('/<string:folder_id>')
def show_post(folder_id): 
    
    return creat_land_folder(folder_id)

if __name__ == '__main__':
    folder_id, folder_name, folder_parent = get_info_list(folder_path)
    file_name, file_parent_folder, file_name_old = get_info_list(file_path)
    
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.run()