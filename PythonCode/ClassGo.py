def Rectangular(Long,wide):
    if(type(Long) != type(1)) or (type(wide) != type(1)):
        return "请输入整数！!"
    if(Long == wide):
        message = "这是一个正方形,面积为："
    else:
        message = "这是一个长方形，面积为："
    area = str(Long * wide)
    return message + area
a = Rectangular('ss',1)
c = Rectangular(2,2)
e = Rectangular(12,4)
print(a)
print(c)
print(e)

class Rectangulars:
    def __init__(self,Long,Wide):
        self.long = Long
        self.wide = Wide
    def Area(self):
        if(type(self.long) != type(1)) or (type(self.wide) != type(1)):
            return "请输入整数！"
        if(self.long == self.wide):
            message = "这是一个正方形。面积是："
        else:
            message = "这是一个长方形。面积是："
        area = str(self.long * self.wide)
        return message + area
b = Rectangulars('123',11)
d = Rectangulars(12,12)
f = Rectangulars(10,5)
print(b.Area())
print(d.Area())
print(f.Area())