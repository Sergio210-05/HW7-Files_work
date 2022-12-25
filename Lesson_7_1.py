
cook_book = {}


def book(file, dictionary=cook_book):
    with open(file, 'rt', encoding='utf8') as formula:
        for line in formula:
            # dish = line
            ingridients = formula.readline()
            # print('Количество ингридиентов:', ingridients)
            dish = line.replace('\n', '')
            dictionary[dish] = []
            for pos in range(int(ingridients)):
                ing = formula.readline().split(' | ')
                # print(ing)
                dictionary[dish].append({'ingredient_name': ing[0], 'quantity': int(ing[1]),
                                         'measure': ing[2].replace('\n', '')})
            formula.readline()


def get_shop_list_by_dishes(dishes, person_count, book=cook_book):
    products_list = {}
    for dish in dishes:
        for ing in book[dish]:
            if ing['ingredient_name'] in list(products_list.keys()):
                products_list[ing['ingredient_name']]['quantity'] += ing['quantity'] * person_count
            else:
                products_list[ing['ingredient_name']] = \
                {'measure': ing['measure'], 'quantity': ing['quantity'] * person_count}
    return products_list


book('recipes.txt')
# print()
# print(cook_book)
products = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)
print(products)
# help(open)
