scoreKor = int(input('국어점수를 입력하세요'))
scoreMath = int(input('수학점수를 입력하세요'))
scoreEng = int(input('영어점수를 입력하세요'))

avg = (scoreKor + scoreMath + scoreEng)/3

if avg >=90:
    print("A학적입니다")
elif avg >=80:
    print("B학점입니다")
elif avg >=70:
    print("C학점입니다")
elif avg >=60:
    print("D학점입니다")
else:
    print("F학점입니다")
