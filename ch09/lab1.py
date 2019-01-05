items = {"커피음료":7, '펜':3, '종이컵':2, '우유':1, '콜라':4, '책':5}

while input("계속하시겠습니까(Y/N)") == 'Y':
    product = input("물건의 이름을 입력하세요")
    symbol = input("파는 물건인가요(1), 추가하는 물건인가요(2)")
    nums = int(input(product, "의 갯수를 압력하세요"))
    if product not in items.keys():
       items[product] == nums
       continue 
    if symbol == "1":
        items[product] -= nums
    elif symbol =='2':
        items[product] += nums
    else:
        print("사는지 파는지 잘 모르겠습니다")
    items[product]= nums
    
print(items)
