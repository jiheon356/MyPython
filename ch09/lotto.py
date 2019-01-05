import random

numbers = []

while(len(numbers)<6):
    num = random.randint(1,46)
    print(num)
    if num in numbers:
        continue
    else :
        numbers.append(num)

print(numbers)
