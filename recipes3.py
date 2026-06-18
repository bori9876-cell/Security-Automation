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

def display_recipe(recipe_name):
    print(f"Ingredients for {recipe_name}:")

    for ingredients in recipes[recipe_name]["ingredients"]:
        print("-", ingredients.title())

    print()

    print(f"Instructions for {recipe_name}:")

    step_number = 1

    for instructions in recipes[recipe_name]["instructions"]:
        print(f"Step {step_number}: {instructions.capitalize()}")
        step_number += 1

def save_recipes():
    with open("recipes.json", "w") as f:
        json.dump(recipes, f)

def search_recipes():
    craving = input("Enter the food you are craving: ")

    matches = []

    for recipe_name, recipe_data in recipes.items():
        if (
            craving.lower() in recipe_name or
            craving.lower() in recipe_data["ingredients"]:
        ):
            print("-", recipe_name.title())            
            matches.append(recipe_name)

    if matches:
        recipe_choice = input("Please select a recipe from the list: ").lower()
        if recipe_choice in matches:
            display_recipe(recipe_choice)

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
        display_recipe(select_recipe)

    else:
        print("Recipe not found.")

def edit_recipe():    
    if not recipes:
        print("No recipes to edit")
        return
    
    recipe_option = 1

    for recipe_name in recipes:
        print(f"{recipe_option}. {recipe_name.title()}")
        recipe_option += 1

    print()

    choose_recipe = input("Which recipe would you like to edit?: ").lower().strip()

    if choose_recipe in recipes:
        display_recipe(choose_recipe)
        while True:            
            edit_what = input("1: Edit ingredients?\n2: Edit instructions?\n3: Return to main menu\n Choose: ")
            if edit_what == "1":
                edited_ingredients = input("Please enter new ingredients: ").lower().strip()
                cleaned_ingredients = []
                for item in edited_ingredients.split(","):
                    cleaned_ingredients.append(item.strip())    
                recipes[choose_recipe]["ingredients"] = cleaned_ingredients
                save_recipes()
                break
            elif edit_what == "2":
                edited_instructions = input("Please enter new instructions: ").lower().strip()
                cleaned_instructions = []
                for item in edited_instructions.split(","):
                    cleaned_instructions.append(item.strip())
                recipes[choose_recipe]["instructions"] = cleaned_instructions
                save_recipes()
                break
            elif edit_what == "3":
                print("Returning to main menu")
                break
            else:
                print("Invalid choice, please choose again")
                continue
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
    menu_choice = input("Please choose from the following options:\n 1. Search Recipes\n 2. Add Recipe\n 3. View All Recipes\n 4. Delete Recipe\n 5. Edit Recipe\n 6. Exit\n")
    if menu_choice == "1":
        search_recipes()

    elif menu_choice == "2":
        add_recipe()

    elif menu_choice == "3":
        view_all_recipes()

    elif menu_choice == "4":
        delete_recipe()

    elif menu_choice == "5":
        edit_recipe()

    elif menu_choice == "6":
        print("Goodbye")
        break
    
    else:
        print("Invalid Entry")
        continue