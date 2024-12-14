
with open ('file.txt', encoding='utf-8') as file:
    cook_book = {}
    data = file.read().split('\n\n')
    for block in data:
        x = block.split('\n')
        name = x.pop(0)
        x.pop(0)
        ingridients = [i.split('|') for i in x]
        cook_book[name] = []
        for el in ingridients:
            cook_book[name].append({'ingredient_name':el[0].strip(), 'quantity':int(el[1].strip()), 'measure':el[2].strip()})
    print(cook_book)





