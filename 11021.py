num=int(input())

for i in range(num):
    x,y=map(int, input().split())

    print('Case #{}: {}'.format(i+1,x+y))
