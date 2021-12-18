import time
def NewTime(fun):
    def RunTime(*args,**kwargs):
        t0 = time.time()
        fun(*args,**kwargs)
        run = time.time() - t0
        return run
    return RunTime
@NewTime
def TestType():
    i = 0
    while i < 35:
        type(123)
        i += 1
@NewTime
def TestIsinstance():
    j = 0
    while j < 35:
        isinstance(123,int)
        j += 1
#当循环次数效于35则Type速度快，当循环次数等于35次两者一样快，大于35次Isinstance速度快
a = TestType()
b = TestIsinstance()
if(a > b):
    print("Type计算类型速度快")
elif (a < b):
    print("Isinstance计算类型速度快")
else:
    print("两者计算速递一样快")
print(a)
print(b)
