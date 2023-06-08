from pprint import pprint
with open('text 1.txt', 'rt', encoding='utf-8') as file:
    departmens = {}
    for line in file:
        name_of_the_dish = line.strip()
        ingredient_count = int(file.readline())
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()

        departmens[name_of_the_dish] = ingredients


#pprint(f'cook_book {departmens} sort_dicts=False')
pprint(departmens, sort_dicts=False)