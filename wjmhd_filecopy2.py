import os
import shutil
import pandas as pd


file_path = r'C:\Users\Administrator\Desktop\file.csv'
folder_path = r'C:\Users\Administrator\Desktop\folder.csv'

dest_path = r'E:\wjmhd' #目标路径

files_path = r'Z:\download\fileblocks'#文件路径

folder_id = []
folder_name = []
folder_parent = []

file_name= []
file_parent_folder = []
file_name_old = []


#河北省
fp_id = '9c1c8e2c-ba18-40a4-a3ca-c559fbe152d5'
#2102831000444-盘坨子
#fp_id = '8ca38dfc-528e-4ccb-9f78-7aaca4dba155'
#全国
#fp_id = '498d365d-38fe-4d60-be84-96b961c92c14'

#读取csv
def get_info_list(filename):
    data = pd.read_csv(filename, header=None, skiprows=[0,0], sep=',')

    list1 = list(data.values[:, 0])
    list2 = list(data.values[:, 1])
    list3 = list(data.values[:, 2])

    return list1, list2, list3

#创建文件目录
def creat_folder(folder_list):
    try:
        

    except Exception as e:
        print('创建文件失败：%s文件目录：%s' % (e, path))

def copy_file(fpf, new_file_path):
    try:
        index_1 = 0
        for fpf_ls in file_parent_folder:

            if fpf == fpf_ls:
                
                old_file_path = os.path.join(files_path, file_name_old[index_1])
                
                if file_name_old[index_1] in list_file_old:

                    shutil.copy(old_file_path, new_file_path)

                    src_file = os.path.join(new_file_path, file_name_old[index_1])
                    dst_file = os.path.join(new_file_path, file_name[index_1])

                    os.rename(src_file, dst_file)

            index_1 = index_1 + 1

    except Exception as e:
        print('复制文件失败：%s文件名称：%s' % (e, old_file_path))

#获取目录下所有文件（目录下没有文件夹）
def get_all_file(path, list_name):
    for filename in os.listdir(path):
        # file_path = os.path.join(path, filename)
        # if os.path.isdir(file_path):
        #     get_all_file(file_path, list_name)
        # else:
        list_name.append(filename)
    print('获取文件列表')


if __name__ == "__main__":
    folder_id, folder_name, folder_parent = get_info_list(folder_path)
    file_name, file_parent_folder, file_name_old = get_info_list(file_path)
    list_file_old = []
    get_all_file(files_path, list_file_old)
    creat_folder(fp_id, dest_path)
    