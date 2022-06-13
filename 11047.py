n,k=map(int,input().split())

array=[]
count=0

for i in range(n):
    array.insert(0,int(input()))

for coin in array:
    count+=k//coin
    k%=coin

print(count)
