import random

while True:
    x = random.randint(1,100)
    y = random.randint(1,100)
    print(x, '+', y, '의 값은?')
    userNo = int(input())
    if userNo == (x + y):
        print('정답')
        break
    else :
        print('오답')
        print('다시 하세요')
