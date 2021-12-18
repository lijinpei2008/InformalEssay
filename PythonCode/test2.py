import random

Keys = True
while Keys:
    print("我们来玩猜数字的游戏！请输入你猜的数字:")
    X = random.randint(1, 100)
    print("偷偷告诉你结果是:",X)
    try:
        i = 0
        while i < 6:
            NoValue = input()
            noValue = int(NoValue)
            if i == 5:
                print("六次没猜中，游戏结束！")
                i = 100
            elif noValue < X:
                i += 1
                print("您输入的数字偏小，请重新输入!这是第%s次（提示，用二分法来缩小范围）"%i)
            elif noValue > X:
                i += 1
                print("您输入的数字偏大，请重新输入!这是第%s次（提示，用二分法来缩小范围）"%i)
            else:
                i += 1
                print("恭喜您，猜对了！一共用了%s次" % i)
                i = 100

    except ValueError as ValueMessage:
        print("请输入数字，错误信息：%s"%ValueMessage)

    finally:
        print("重新开始，请按Y/y继续")
        stringValue = input()
        if (stringValue == "Y") or (stringValue == "y"):
            Keys = True
        else:
            Keys = False