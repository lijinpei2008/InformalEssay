#f = open('/home/pyvip/projects/123.py')
#content = f.read()
#print(content)
#f.close()

try:
    g = open('/home/pyvip/projects/123.txt')
    print("文件已经打开！")
    content = g.read()
    print(content)
    a = b
except NameError as name:
    print(name)
finally:
    g.close()
    print("\n文件已经关闭！")
