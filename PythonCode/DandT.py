
tupleValue = ('1111','2222','333','44444')
dictionaryValue = {'Name':'Jeffrey','Age':'16','Sex':'Man','Birthday':'2001-2-3'}

def Change(tup,dic):
    dic_keys = ''
    dic_values = ''
    tup_values = ''
    #用循环来拼接字符串，拿到想要的内容
    for k,v in dic.items():
        dic_keys = dic_keys + k + "|"
        dic_values = dic_values + v + "|"
    for i in tup:
        tup_values = tup_values + i + "|"
    #使用分割将字符串切开
    dic_k = dic_keys.split("|")
    dic_v = dic_values.split("|")
    tup_v = tup_values.split("|")
    #开始转换拼接
    dicTwo = {dic_k[0]:tup_v[0],dic_k[1]:tup_v[1],dic_k[2]:tup_v[2],dic_k[3]:tup_v[3]}
    tup_v = (dic_v[0],dic_v[1],dic_v[2],dic_v[3])

    return dicTwo,tup_v

a,b = Change(tupleValue,dictionaryValue)
print(dictionaryValue,tupleValue)
print(a,b)
