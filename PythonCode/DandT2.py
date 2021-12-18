
tupleValue = (1111,2222,333,4444)
dictionaryValue = {'A':9999,'B':8888,'C':7777,'D':6666}

def Change(tu,di):
    list1 = []

    for k in list(di.keys()):
        list1.append(di[k]) #将字典的value添加到列表内

    new_di = dict(zip(di.keys(),tu))
    new_tu = tuple(list1)

    return new_di,new_tu

a,b = Change(tupleValue,dictionaryValue)
print(tupleValue,dictionaryValue)
print(b,a)