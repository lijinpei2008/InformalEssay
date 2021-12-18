def chengfa(n):
        for i in range(1,n):
                for j in range(1,i+1):
                        print(str(j) + 'X' + str(i) + '=' + str(i*j),end=" ")
                print()
chengfa(11)