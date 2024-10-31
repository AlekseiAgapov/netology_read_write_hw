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

print(cook_book)