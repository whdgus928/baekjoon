m = int(input())
n = int(input())

sum=0

for i in range(n,0,-1):
    if m<=i*i and i*i<=n:
        sum=sum+i*i
        min=i*i
        
if sum==0:
    print(-1)
else:
    print(sum)
    print(min)
