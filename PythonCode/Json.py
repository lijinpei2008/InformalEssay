import json
import os

data = {
    'name':'李津沛',
    'age':22,
    'list':[1,2,3],
    'tuple':(4,5,6),
    'True':True,
    'None':None
}

jsonValue = json.dumps(data,ensure_ascii=False)
print(jsonValue)
print(type(jsonValue))

dictValue = json.loads(jsonValue)
print(dictValue)
print(type(dictValue))

for k in list(dictValue.keys()):
    print(k)

path = os.getcwd()
print(path)
path1 = os.path.dirname(path)
print(path1)
path2 = os.path.basename(path)
print(path2)