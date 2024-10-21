from match import match
from menue import meal_db
from typing import List, Tuple, Callable, Any, Optional

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

    name = (matches[0])
    result = set()
    for meal in meal_db:
        if get_name(meal) == name:
            result.update(get_recipe(meal))
    return list(result)

def recipe_by_mainIngredient(matches: List[str]) -> List[str]:
    #takes input of an ingredient and returns recipies with the same ingredient

    mainIngredient = (matches[0])
    result= set()
    for meal in meal_db:
        if get_mainIngredient(meal) == mainIngredient:
            result.update(get_recipe (meal))
    return list(result)

def recipe_by_catagory(matches: List[str]) -> List[str]:
    #takes an input of the catagory the food falls into; eg breakfast or seafood and returns all recipies match catagory

    catagory = (matches[0])
    result= set()
    for meal in meal_db:
        if get_catagory(meal) == catagory:
            result.update(get_recipe (meal))
    return list(result) 

def recipe_by_location(matches: List[str]) -> List[str]:
    #takes an input of a location and returns recipes from the specified location
    
    location = (matches[0])
    result= set()
    for meal in meal_db:
        if get_location(meal) == location:
            result.update(get_recipe (meal))
    return list(result)

def name_by_recipie(matches: List[str]) -> List[str]:
    if not matches or len(matches) != 1:
        return []  
    recipie = matches[0]
    result = set()
    for meal in meal_db:
        if recipie in get_recipe(meal):  
            result.add(get_name(meal))  

    return list(result) 

def name_by_locaion(matches: List[str]) -> List[str]:

    location = matches[0]
    result = []
    for meal in meal_db:
        if location in get_location(meal):
            result.append(get_name(meal))
    return(result)

def name_by_mainIngredient(matches: List[str]) -> List[str]:

    mainIngredient = matches[0]
    result = []
    for meal in meal_db:
        if mainIngredient in get_mainIngredient(meal):
            result.append(get_name(meal))
    return(result)


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (["what", "is", "the", "recipe", "for"], recipe_by_name),
    (["what", "recipes", "use"], recipe_by_mainIngredient),
    (["what", "recipes", "are", "there"], recipe_by_catagory),
    (["what", "recipes", "are", "from"], recipe_by_location),
    (["bye"], bye_action),
]

import re
from typing import List, Dict, Tuple, Union
def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    query_string = ' '.join(src)
    
    for pattern, action in pa_list:
        regex_pattern = re.sub(r'%|_', '(.*)', ' '.join(pattern))
        
        match = re.fullmatch(regex_pattern, query_string, re.IGNORECASE)
        if match:
            matches = list(match.groups())
            responses = action(matches)
            if not responses:
                return ["No answers"]
            return responses

    return ["I don't understand"]
# def search_pa_list(query: List[str]) -> Tuple[Optional[List[str]], Optional[Callable[[List[str]], List[Any]]]]:
#     """Finds the matching pattern and corresponding action based on the input query."""
#     for pattern, action in pa_list:
#         if all(word in query for word in pattern):
#             return pattern, action
#     return [], None

def query_loop() -> None:
    print("Welcome to the recipe database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            pattern, action = search_pa_list(query)

            if pattern and action:
                answers = action(query)
                if answers:
                    for answer in answers:
                        print(answer)
                else:
                    print("No recipes found.")
            else:
                print("Sorry, I didn't understand that.")

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()
#fix query loop