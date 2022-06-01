hour,minute,second=map(int,input().split())
cookTime=int(input())

second=second+cookTime

while second>=60:
    second=second-60
    minute=minute+1

while minute>=60:
    minute=minute-60
    hour=hour+1

while hour>=24:
    hour=hour-24

print(hour,minute,second)
