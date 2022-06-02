referee=int(input())

text=input()

if text.count('A')==text.count('B'):
    print('Tie')

elif text.count('A')>text.count('B'):
    print('A')

elif text.count('A')<text.count('B'):
    print('B')
