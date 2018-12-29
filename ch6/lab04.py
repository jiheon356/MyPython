bread = ['호밀빵','위트', '화이트']
meats = ['미트볼', '소시지','닭가슴살']
vegies = ['양상추', '토마토', '오이']
sauce = ['마요네즈', '허니 머스타드', '칠리']

for bread in breads:
    for meat in meats:
        for vegi in vegies:
            for sauce in sauces:
                print(bread,'+', meat, '+', vegi, '=', sauce)
