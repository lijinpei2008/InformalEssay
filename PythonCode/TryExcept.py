class All:
    def __init__(self,Long,Wide):
        self.long = Long
        self.wide = Wide
    def Sun(self):
        if (self.long == self.wide):
            print("这是一个正方形!")
        else:
            print("这是一个长方形")
        return self.long * self.wide
key = True
while key:
    try:
        LongValue = input("请输入长")
        WideValue = input("请输入宽")
        l = int(LongValue)
        w = int(WideValue)
        a = All(l,w)
        a.Sun()
    except Exception as messages:
        print(messages)
    finally:
        stringValue = input("请按Y/y继续")
        if(stringValue == "Y") or (stringValue == "y"):
            key = True
        else:
            key = False
