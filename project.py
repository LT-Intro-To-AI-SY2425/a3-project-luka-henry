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

    name = int(matches[0])
    result=[]
    for meal in meal_db:
        if get_name(meal) == name:
            result.append(get_recipe (meal))
    return result

def recipe_by_mainIngredient(matches: List[str]) -> List[str]:
    #takes input of an ingredient and returns recipies with the same ingredient

    mainIngredient = int(matches[1])
    result=[]
    for meal in meal_db:
        if get_mainIngredient(meal) == mainIngredient:
            result.append(get_recipe (meal))
    return result

def recipe_by_catagory(matches: List[str]) -> List[str]:
    #takes an input of the catagory the food falls into; eg breakfast or seafood and returns all recipies match catagory

    name = int(matches[0])
    result=[]
    for meal in meal_db:
        if get_name(meal) == name:
            result.append(get_recipe (meal))
    return result
pass  

def recipe_by_location(matches: List[str]) -> List[str]:
    #takes an input of a location and returns recipes from the specified location
    
    name = int(matches[0])
    result=[]
    for meal in meal_db:
        if get_name(meal) == name:
            result.append(get_recipe (meal))
    return result
pass

