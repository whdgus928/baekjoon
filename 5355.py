num=int(input())

for i in range(num):
    a=list(map(str,input().split()))
    for j in range(1,len(a)):
        if j==1:
            result=float(a[0])
        if a[j]=='@':
            result=result*3
        elif a[j]=='%':
            result=result+5
        elif a[j]=='#':
            result=result-7

    print(format(result,".2f"))

        
