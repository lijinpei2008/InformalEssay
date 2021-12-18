class Rectangulars:
    def __init__(self,Long,Wide):
        self.long = Long
        self.wide = Wide
    def Area(self):

        if(isinstance(self.long,int) == False) or (isinstance(self.wide,int) == False):
            return "请输入整数！"

        if(self.long == self.wide):
            message = "这是一个正方形。面积是："
        else:
            message = "这是一个长方形。面积是："
        area = str(self.long * self.wide)
        return message + area

class Square(Rectangulars):
    #实现类的实例可调用
    def __call__(self, *args, **kwargs):
        print(format('边长是：%s'%self.wide))

    def __str__(self):
        #返回值 必须是字符串
        return self.Area()

a = Square('111','111')
a()
print(a)
b = Square(10,10)
b()
print(b)