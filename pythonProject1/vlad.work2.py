dishes_list = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
                         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
                         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}],
               'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
                                    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
                                    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
                                    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}],
               'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
                                        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
                                        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}],
               'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
                           {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
                           {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
                           {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
                           {'ingredient_name': 'Помидор', 'quantity': 3, 'measure': 'шт'}]}


def get_shop_list_by_dishes(dishes, person_count):
    dishes_count = {}
    for i in dishes:
        for d in dishes_list[i]:
            if d['ingredient_name'] not in dishes_count:
                dishes_count[d['ingredient_name']] = {'measure': d['measure'], 'quantity': d['quantity'] * person_count}
            else:
                dishes_count[d['ingredient_name']]['quantity'] += (person_count * d['quantity'])
    print(dishes_count)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
