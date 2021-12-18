
def Sorting(n,args):
    if(n == True):
        for i in range(len(args) -1):
            item = False
            for j in range(len(args)-1-i):
                if(args[j] > args[j+1]):
                    args[j],args[j+1] = args[j+1],args[j]
                    item = True
            if not item:
                break
    else:
        for i in range(len(args) -1):
            item = False
            for j in range(len(args)-1-i):
                if(args[j] < args[j+1]):
                    args[j],args[j+1] = args[j+1],args[j]
                    item = True
            if not item:
                break
    print(args)

Sorting(True,[1,5,2,4,3,6,1,23,0])
Sorting(False,[1,5,2,4,3,6,1,23,0])
