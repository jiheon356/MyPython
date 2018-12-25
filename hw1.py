import random
x=random.randint(0,99)
y=int(input("복권번호를 입력하시오(0~99까지)"))
print("당첨번호는 ",x," 입니다.")
x10=x//10
x1=x%10
y10=y//10
y1=y%10
if x1==y1 and x10==y10:
print("100만원 당첨입니다!")
elif x1!=y1 and x10!=y10:
