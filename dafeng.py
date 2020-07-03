import os, sys
import shutil

src_path = r'C:\Users\DENG\Desktop\01-大丰区养殖用海现场调查成果电子数据集'
dest_path = r'C:\Users\DENG\Desktop'

hyz_path = r'C:\Users\DENG\Desktop\01-大丰区养殖用海现场调查成果电子数据集\04-养殖用海电子数据集\海域证'
ht_path = r'C:\Users\DENG\Desktop\01-大丰区养殖用海现场调查成果电子数据集\04-养殖用海电子数据集\合同'
tdz_path = r'C:\Users\DENG\Desktop\01-大丰区养殖用海现场调查成果电子数据集\04-养殖用海电子数据集\土地证'
yzz_path = r'C:\Users\DENG\Desktop\01-大丰区养殖用海现场调查成果电子数据集\04-养殖用海电子数据集\养殖证'


list_zh = [] #证号列表
list_zh_path = [] #证号所对应的地址

hyz_list = []   #海域证
ht_list = []    #合同
tdz_list = []   #土地证
yzz_list = []   #养殖证
not_type = []   #没有找到对应类型的文件
#复制证书扫描件
def copy_zssmj():
    for zh in list_zh:
        dest_file_path = os.path.join(dest_path, '大丰', zh, '扫描件')

        index1 = list_zh.index(zh)
        zh_path = list_zh_path[index1]

        src_path_3 = os.path.join(zh_path, '03-照片、视频、扫描件和现场测量图表', '扫描件')

        for src_path_file in os.listdir(src_path_3):
            file_path = os.path.join(src_path_3, src_path_file)

            if src_path_file in hyz_list or '海域证' in src_path_file:
                dest_file_path_1 = os.path.join(dest_file_path, '海域证')
                shutil.copy(file_path, dest_file_path_1)
            elif src_path_file in ht_list:
                dest_file_path_1 = os.path.join(dest_file_path, '合同')
                shutil.copy(file_path, dest_file_path_1)
            elif src_path_file in tdz_list:
                dest_file_path_1 = os.path.join(dest_file_path, '土地证')
                shutil.copy(file_path, dest_file_path_1)
            elif src_path_file in yzz_list or '养殖证' in src_path_file:
                dest_file_path_1 = os.path.join(dest_file_path, '养殖证')
                shutil.copy(file_path, dest_file_path_1)
            else:
                print('没有找到对应的类型，文件路径：%s' % (file_path))
                not_type.append(file_path)

#复制照片
def copy_photo():
    for zh in list_zh:
        
        dest_file_path = os.path.join(dest_path, '大丰', zh, '照片')
        
        index1 = list_zh.index(zh)
        zh_path = list_zh_path[index1]

        src_path_2 = os.path.join(zh_path, '03-照片、视频、扫描件和现场测量图表', '照片')
        
        for src_path_file in os.listdir(src_path_2):
            file_path = os.path.join(src_path_2, src_path_file)
            shutil.copy(file_path, dest_file_path)

#复制现场调查表中文件    
def copy_xcdzb():

    for zh in list_zh:

        dest_file_path = os.path.join(dest_path, '大丰', zh)

        index1 = list_zh.index(zh)
        zh_path = list_zh_path[index1]

        src_path_1 = os.path.join(zh_path, '02-现场调查表')
        
        for src_path_file in os.listdir(src_path_1):
            file_path = os.path.join(src_path_1, src_path_file)
            shutil.copy(file_path, dest_file_path)
                           
#获取目录下所有文件
def get_all_file(path, list_name):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isdir(file_path):
            get_all_file(file_path, list_name)
        else:
            list_name.append(filename)
    
#获取证号及对应地址
def get_zh(path, list_zh, list_zh_path):
    for name in os.listdir(path):
        dir_path = os.path.join(path, name)
        if os.path.isdir(dir_path) and name[:7] != '320904-':
            get_zh(dir_path, list_zh, list_zh_path)
        elif not os.path.isdir(dir_path):
            continue
        else:
            list_zh.append(name)
            list_zh_path.append(dir_path)

    #list_zh = list(set(list_zh))

#判断调查成果图中是否存在文件
def get_dccgt(path, list_name):
    for name in os.listdir(path):
        dir_path = os.path.join(path, name)
        if os.path.isdir(dir_path) and name != '01-调查成果图':
            get_dccgt(dir_path, list_name)
        elif not os.path.isdir(dir_path):
            continue
        else:
            for filename in os.listdir(dir_path):
                list_name.append(filename)
    return list_name

#创建目录
def creat_dir():
    try:
        dest_path_full = os.path.join(dest_path, '大丰')
        os.mkdir(dest_path_full)

        n = 0
        for i in list_zh:
            os.makedirs(os.path.join(dest_path_full, i, '照片'))
            os.mkdir(os.path.join(dest_path_full, i, '扫描件'))
            os.mkdir(os.path.join(dest_path_full, i, '扫描件', '海域证'))
            os.mkdir(os.path.join(dest_path_full, i, '扫描件', '合同'))
            os.mkdir(os.path.join(dest_path_full, i, '扫描件', '土地证'))
            os.mkdir(os.path.join(dest_path_full, i, '扫描件', '养殖证'))
            n = n + 1

        print('目录结构创建完成')

    except Exception as e:
        print('创建文件失败：%s文件目录：%s' % (e, list_zh[n]))

if __name__ == "__main__":
    #sys.setrecursionlimit(10000) #递归层数
    get_zh(src_path, list_zh, list_zh_path)
    get_all_file(hyz_path, hyz_list)
    get_all_file(ht_path, ht_list)
    get_all_file(tdz_path, tdz_list)
    get_all_file(yzz_path, yzz_list)
    #creat_dir()  #创建目录结构
    #copy_xcdzb()
    #copy_photo()
    #copy_zssmj()
    
     