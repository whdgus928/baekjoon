hour,minute=map(int,input().split())
cookTime=int(input())


minute=minute+cookTime

while minute>=60:
    minute=minute-60
    hour=hour+1

while hour>=24:
    hour=hour-24

print(hour,minute)

