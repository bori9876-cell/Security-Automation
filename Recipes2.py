import json

recipes = {
    "tacos": {
        "ingredients": ["beef", "cheese", "taco_shells"],
        "instructions": ["brown the beef in skillet", "add beef to taco shells", "add cheese on top of beef"]
    },
    "omelette": {
        "ingredients": ["eggs", "cheese"],
        "instructions": ["wisk eggs in a bowl", "pour into hot buttered egg pan", "flip when flippable", "cover with cheese", "after finished cooking, fold in half and serve"]
    },
    "spaghetti": {
        "ingredients": ["pasta", "sauce"],
        "instructions": ["make the pasta", "make the sauce", "mix together and serve"]
    } 
}

def load_recipes():
    global recipes
    try:
        with open("recipes.json", "r") as f:
            recipes = json.load(f)
    except:
        print("No saved recipes found. Using default recipes.")

def save_recipes():
    with open("recipes.json", "w") as f:
        json.dump(recipes, f)

def search_recipes():
    craving = input("Enter the food you are craving: ")
    matches = []
    for recipe_name, recipe_data in recipes.items():
        if craving.lower() in recipe_data["ingredients"]:
            print("-", recipe_name.title())            
            matches.append(recipe_name)
    if matches:
        recipe_choice = input("Please select a recipe from the list: ").lower()
        if recipe_choice in matches:            
            print(f"Ingredients for {recipe_choice}:")
            for ingredients_list in recipes[recipe_choice]["ingredients"]:
                print("-", ingredients_list.title())
    if not matches:
        print("Sorry, there are no recipes with that ingredient available.")

    print()

def add_recipe():
    recipe_name = input("Enter the name of the recipe you would like to add: ").lower()
    raw_ingredients = input("Enter the ingredients: ").split(",")
    instructions = input("Enter cooking instructions: ").split(",")
    clean_ingredients = []
    clean_instructions = []
    for item in raw_ingredients:
        clean_ingredients.append(item.strip())
    for item in instructions:
        clean_instructions.append(item.strip())
    recipes[recipe_name] = {
        "ingredients": clean_ingredients, "instructions": clean_instructions
    }
    save_recipes()
    print(recipe_name.title(), "added.")

def view_all_recipes():
    print("All Recipes:")
    for recipe_name in recipes:
        print("-", recipe_name.title())
    print()
    select_recipe = input("Select a recipe: ").lower()
    if select_recipe in recipes:
        print(f"Ingredients for {select_recipe}:")
        for ingredients_list in recipes[select_recipe]["ingredients"]:
            print("-", ingredients_list.title())
        print(f"Instructions for {select_recipe}:")
        for instruction_steps in recipes[select_recipe]["instructions"]:
            print("-", instruction_steps.title())
    else:
        print("Recipe not found.")

def delete_recipe():
    if not recipes:
        print("No recipes to delete")
        return
    for recipe_name in recipes:
        print("-", recipe_name.title())
    print()
    to_remove = input("Choose which recipe to delete :").lower().strip()
    if to_remove in recipes:
        while True:
            confirm = input(f"Are you sure you want to delete {to_remove}? 1. Yes\n 2. No").lower().strip()
            if confirm in ["1", "yes"]:
                del recipes[to_remove]
                save_recipes()
                print(to_remove.title(), "deleted.")
                break
            elif confirm in ["2", "no"]:
                print("Recipe not deleted")
                break
            else:
                print("Invalid choice, try again.")
    else:
        print("Recipe not found.")

load_recipes()

while True:
    menu_choice = input("Please choose from the following options:\n 1. Search Recipes\n 2. Add Recipe\n 3. View All Recipes\n 4. Delete Recipe\n 5. Exit\n")
    if menu_choice == "1":
        search_recipes()
    elif menu_choice == "2":
        add_recipe()
    elif menu_choice == "3":
        view_all_recipes()
    elif menu_choice == "4":
        delete_recipe()
    elif menu_choice == "5":
        print("Goodbye")
        break
    
    else:
        print("Invalid Entry")
        continue