num=int(input())
sort=[]
for i in range(num):
    a=int(input())
    sort.append(a)

sort.sort()

for i in range(num):
    print(sort[i])
