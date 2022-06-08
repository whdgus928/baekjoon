num=int(input())

for i in range(num):
    rotate,text=map(str,input().split())
    rotate=int(rotate)
    for j in range(len(text)):
        print(rotate*text[j],end='') 
    print('')


# end='' //띄워쓰기 제거
