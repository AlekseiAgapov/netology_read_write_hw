# Open the file for reading
with open('recipes.txt', 'r', encoding='utf-8') as file:
    # Create an empty dictionary
    cook_book = {}
    # Start the WHILE loop that will ensure reading the file until the end
    while True:
        dish_name = file.readline().strip()
        if not dish_name:
            break
        # For each dish read the number of ingredients
        number_of_ingredients = int(file.readline().strip())
        # For each ingredient read the name, quantity and measure of the quantity. Store in a list of lists.
        ingredients = []
        for _ in range(number_of_ingredients):
            ingredient_summary = file.readline().strip()
            ingredient = {
                'ingredient_name': ingredient_summary.split(' | ')[0],
                'quantity': int(ingredient_summary.split(' | ')[1]),
                'measure': ingredient_summary.split(' | ')[2]
            }
            ingredients.append(ingredient)
        # Add the list to the initial dictionary
        cook_book[dish_name] = ingredients
        # The dishes are separated with an empty line. Add a command to read it before proceeding to the next dish.
        empty_line = file.readline().strip()


def get_shop_list_by_dishes(dishes, person_count):
    """
    The function takes a list of dishes and a number of people for whom the meal is going to be cooked.
    It returnes a shopping list: a dictionary with quantity of each ingredient that has to be bought.
    """
    # Create an empty dictionary to write the results
    result_dict = {}
    # Iterate between the elements of the list "dishes" and save the data: name, required quantity and measure in three variables
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            result_quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            # Check if the ingredient is already in the result_dict and add the data to the result dictionary
            if ingredient_name in result_dict:
                result_dict[ingredient_name]['quantity'] += result_quantity
            else:
                result_dict[ingredient_name] = {
                    'measure': measure,
                    'quantuty': result_quantity
                }
    
    return result_dict

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))