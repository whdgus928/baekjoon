num=int(input())

for i in range(num):
    text=input()
    sum=0
    score=0
    
    for i in range(len(text)):
        if text[i]=='O':
            score=score+1
            sum=sum+score

        elif text[i]=='X':
            score=0

        else:
            break
        
    print(sum)

    
