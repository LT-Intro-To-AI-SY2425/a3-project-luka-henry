from match import match
from menue import meal_db
from typing import List, Tuple, Callable, Any

def get_name(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[0]
def get_mainIngredient(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[1]
def get_catagory(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[2]
def get_location(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[3]
def get_recipe(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[4]



def recipe_by_name(matches: List[str]) -> List[str]:
    #takes input of name and returns assoicated recipe

    name = str(matches[0])
    result=[]
    for meal in meal_db:
        if get_name(meal) == name:
            result.append(get_recipe (meal))
    return result

def recipe_by_mainIngredient(matches: List[str]) -> List[str]:
    #takes input of an ingredient and returns recipies with the same ingredient

    mainIngredient = str(matches[1])
    result=[]
    for meal in meal_db:
        if get_mainIngredient(meal) == mainIngredient:
            result.append(get_recipe (meal))
    return result

def recipe_by_catagory(matches: List[str]) -> List[str]:
    #takes an input of the catagory the food falls into; eg breakfast or seafood and returns all recipies match catagory

    catagory = str(matches[2])
    result=[]
    for meal in meal_db:
        if get_catagory(meal) == catagory:
            result.append(get_recipe (meal))
    return result  

def recipe_by_location(matches: List[str]) -> List[str]:
    #takes an input of a location and returns recipes from the specified location
    
    location = str(matches[3])
    result=[]
    for meal in meal_db:
        if get_location(meal) == location:
            result.append(get_recipe (meal))
    return result

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("What is the recipe for _"), recipe_by_name),
    (str.split("What recipes use _"), recipe_by_mainIngredient),
    (str.split("What _ recipes are there"), recipe_by_catagory),
    (str.split("What recipes are from _"), recipe_by_location),

    (["bye"], bye_action),
]

#need to search list still

def query_loop() -> None:
    print("Welcome to the recipe database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            found = False

            for pattern, action in pa_list:
                if all(word in query for word in pattern):
                    answers = action(query)
                    if answers:
                        for answer in answers:
                            print(answer)
                    else:
                        print("No recipes found.")
                    found = True
                    break
            
            if not found:
                print("Sorry, I didn't understand that.")

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()