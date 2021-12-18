#复制文件
def  CopyFile(oleFile,newFile):
    with open(oleFile,'r') as old,\
        open(newFile,'w') as new:
        #将源文件读出来
        content = old.read()
        #将读出来的文件写到新的文件内
        new.write(content)
        #刷新缓存
        new.flush()
        print('复制成功！')

CopyFile('yuyu.py','lijinpei/Hello.py')

#遍历某目录下所有文件和文件夹
import os
def ListAll(path):
    listPath = os.listdir(path)
    print(listPath)

    #循坏目录下的所有文件和文件夹
    for i in listPath:
        #拼接绝对路径
        fullPath = os.path.join(path,i)

        #判断是不是文件夹 如果是文件夹，则再次调用自己，进行查询
        if (os.path.isdir(fullPath)):
            ListAll(fullPath)
        else:
            print(fullPath)

ListAll('/home/pyvip/projects/tmp/')