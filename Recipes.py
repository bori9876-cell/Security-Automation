recipes = {
    "tacos": ["beef", "cheese", "taco_shells"],
    "omelette": ["eggs", "cheese"],
    "spaghetti": ["pasta", "sauce"]
}
while True:
    craving = input("Enter the food you are craving: ")
    matches = []

    for recipe_name, ingredients in recipes.items():
        if craving.lower() in ingredients:
            print("-", recipe_name.title())            
            matches.append(recipe_name)

    if matches:
        recipe_choice = input("Please select a recipe from the list: ").lower()
        if recipe_choice in matches:            
            print(f"Ingredients for {recipe_choice}:")
            for ingredients_list in recipes[recipe_choice]:
                print("-", ingredients_list.title())

    if not matches:
        print("Sorry, there are no recipes with that ingredient available.")

    print()

    retry = input("Search again? y/n: ")
    if retry.lower() != "y":
        break