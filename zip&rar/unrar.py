import rarfile
import zipfile

def un_rar(rar_file_name, path=None, pwd=None):
    if path == 'same':
        path = rar_file_name[0:-4]  # 解压到当前同名文件夹下
    elif path == None:              # 解压到当前文件夹
        pass
    else:                           # 解压到任意目录
        pass

    try:
        if rar_file_name.endswith('rar'):
            rar = rarfile.RarFile(rar_file_name)
            rar.extractall(path=path, pwd=pwd)
        elif rar_file_name.endswith('zip'):
            rar = zipfile.ZipFile(rar_file_name)
            rar.extractall(path=path, pwd=pwd.encode("ascii"))
        else:
            print('not zip or rar file, please check your file!')
            return
    except Exception as e:
        print(e)
    
    rar.close()

if __name__ == '__main__':
    un_rar('1.rar')
    # un_rar('2.zip', 'same', "123")
    # un_rar('3.rar', './5', '123')