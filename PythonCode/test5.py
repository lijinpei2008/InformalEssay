
def mum(fun):
    def nun(n):
        print("一个简单的函数", end=" ")
        fun(n)
    return nun

@mum
def num(n):
    print("一些汉字,第%s次调用"%n)
    n += 1


import random
X = random.randint(1, 10)
i = 0
while i < X:
    num(i)
    i += 1