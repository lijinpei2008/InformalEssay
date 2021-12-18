class People:
    def __init__(self,Name,Work):
        self.name = Name
        self.work = Work
    def eat(self):
        return self.name + "同学要去吃饭了\n"
    def sleep(self):
        return self.name + "同学要去睡觉了\n"
    def study(self):
        return self.name + "同学要去工作了，职业是：" + self.work + "\n"
    def message(self):
        return "大家好，我是" + self.name + "。我的职业是：" + self.work + "\n"


class Student(People):
    def __call__(self, *args, **kwargs):
        print("学生的一些信息：",self.name,self.work)
    def __str__(self):
        return self.eat() + self.sleep() + self.study() + self.message()

LiSi = Student('李四','程序员')
LiSi()
print(LiSi)