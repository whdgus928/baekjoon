a,b,c=map(int,input().split())
middle=0

if a<b:
    if b<c:
        middle=b
    else:
        if a<c:
            middle=c
        else:
            middle=a
else:
    if a<c:
        middle=a
    else:
        if b<c:
            middle=c
        else:
            middle=b

print(middle)
