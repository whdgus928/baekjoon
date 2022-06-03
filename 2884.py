hour, minute=map(int,input().split())

minute=minute-45
while minute<0:
    hour=hour-1
    minute=minute+60

while hour<0:
    hour=hour+24

print(hour,minute)
