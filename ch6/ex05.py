sumAll = 0
while True:
    print('점수를 입렵하세요', end='')
    userNo = int(input())
    sumAll = sumAll + userNo
    if userNo == 0:
        break
