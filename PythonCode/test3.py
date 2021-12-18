filePath = ""
fileNo = 0

Keys = True
while Keys:
    try:
        print("请输入一个文件的绝对路径，我将负责打开它。")
        FilePath = input()
        fileValue = open(FilePath,"r")
        print("请输入您想阅读的行数，我将负责打印这些内容。")
        FileNo = input()
        fileNo = int(FileNo)

        lineNo = 0
        TextValues = []
        for line in  fileValue.readlines():
            TextValues .append(line.strip())
            lineNo += 1

        no = 0
        print("文件内容位：")
        while no < fileNo:
            print(TextValues[no])
            no += 1

        print("文件总行数位：%s"%lineNo)

        fileValue.close()

    except ValueError as typeMessage:
        fileValue.close()
        print("输入不正确，文件已关闭！")
        print("请输入整数数字！错误信息如下：")
        print(typeMessage)

    except FileNotFoundError as FileMessage:
        print("文件打开失败！错误信息如下：")
        print(FileMessage)

    finally:
        print("请按Y/y继续")
        stringValue = input()
        if(stringValue == "Y") or (stringValue == "y"):
            Keys = True
        else:
            Keys = False

