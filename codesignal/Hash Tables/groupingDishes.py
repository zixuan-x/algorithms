from collections import defaultdict

def groupingDishes(dishes):
    ingredients = defaultdict(list)
    for dish in dishes:
        dishName = dish[0]
        for i in range(1, len(dish)):
            ingredient = dish[i]
            ingredients[ingredient].append(dishName)
            
    result = []
    for ingredient in sorted(ingredients):
        if len(ingredients[ingredient]) >= 2:
            result.append([ingredient] + sorted(ingredients[ingredient]))

    return result