from match import match
from menue import meal_db
from typing import List, Tuple, Callable, Any, Optional
import re








def get_name(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[0]








def get_mainIngredient(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[1]








def get_category(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[2]








def get_location(meal: Tuple[str, str, str, str, List[str]]) -> str:
    return meal[3]








def get_recipe(meal: Tuple[str, str, str, str, List[str]]) -> List[str]:
    return meal[4]








def recipe_by_name(matches: List[str]) -> List[str]:
    name = matches[0]
    result = set()
    for meal in meal_db:
        if get_name(meal).lower() == name.lower():
            result.update(get_recipe(meal))
    return list(result)








# def recipe_by_mainIngredient(matches: List[str]) -> List[str]:
#     mainIngredient = matches[0]
#     result = set()
#     for meal in meal_db:
#         if get_mainIngredient(meal).lower() == mainIngredient.lower():
#             result.update(get_recipe(meal))
#     return list(result)








# def recipe_by_category(matches: List[str]) -> List[str]:
#     category = matches[0]
#     result = set()
#     for meal in meal_db:
#         if get_category(meal).lower() == category.lower():
#             result.update(get_recipe(meal))
#     return list(result)








# def recipe_by_location(matches: List[str]) -> List[str]:
#     location = matches[0]
#     result = set()
#     for meal in meal_db:
#         if get_location(meal).lower() == location.lower():
#             result.update(get_recipe(meal))
#     return list(result)








def name_by_recipe(matches: List[str]) -> List[str]:
    recipe = matches[0]
    result = set()
    for meal in meal_db:
        if recipe.lower() in [step.lower() for step in get_recipe(meal)]:
            result.add(get_name(meal))
    return list(result)








def name_by_location(matches: List[str]) -> List[str]:
    location = matches[0]
    result = []
    for meal in meal_db:
        if location.lower() in get_location(meal).lower():
            result.append(get_name(meal))
    return result








def name_by_mainIngredient(matches: List[str]) -> List[str]:
    mainIngredient = matches[0]
    result = []
    for meal in meal_db:
        if mainIngredient.lower() in get_mainIngredient(meal).lower():
            result.append(get_name(meal))
    return result




def location_by_name(matches: List[str]) -> List[str]:
    name = matches[0]
    result = []
    for meal in meal_db:
        if name.lower() in get_name(meal).lower():
            result.append(get_location(meal))
    return result




def name_by_category(matches: List[str]) -> List[str]:
    category = matches[0]
    result = []
    for meal in meal_db:
        if category.lower() in get_category(meal).lower():
            result.append(get_name(meal))
    return result


def location_by_category(matches: List[str]) -> List[str]:
    category = matches[0]
    result = []
    for meal in meal_db:
        if category.lower() in get_category(meal).lower():
            result.append(get_location(meal))
    return result








def location_by_mainIngredient(matches: List[str]) -> List[str]:
    mainIngredient = matches[0]
    result = []
    for meal in meal_db:
        if mainIngredient.lower() in get_mainIngredient(meal).lower():
            result.append(get_location(meal))
    return result








def location_by_recipe(matches: List[str]) -> List[str]:
    recipe = matches[0]
    result = []
    for meal in meal_db:
        if recipe.lower() in [step.lower() for step in get_recipe(meal)]:
            result.append(get_location(meal))
    return result








def category_by_name(matches: List[str]) -> List[str]:
    name = matches[0]
    result = []
    for meal in meal_db:
        if name.lower() in get_name(meal).lower():
            result.append(get_category(meal))
    return result








def category_by_location(matches: List[str]) -> List[str]:
    location = matches[0]
    result = []
    for meal in meal_db:
        if location.lower() in get_location(meal).lower():
            result.append(get_category(meal))
    return result








def category_by_recipe(matches: List[str]) -> List[str]:
    recipe = matches[0]
    result = []
    for meal in meal_db:
        if recipe.lower() in [step.lower() for step in get_recipe(meal)]:
            result.append(get_category(meal))
    return result








def category_by_mainIngredient(matches: List[str]) -> List[str]:
    mainIngredient = matches[0]
    result = []
    for meal in meal_db:
        if mainIngredient.lower() in get_mainIngredient(meal).lower():
            result.append(get_category(meal))
    return result








def mainIngredient_by_recipe(matches: List[str]) -> List[str]:
    recipe = matches[0]
    result = []
    for meal in meal_db:
        if recipe.lower() in [step.lower() for step in get_recipe(meal)]:
            result.append(get_mainIngredient(meal))
    return result








def mainIngredient_by_name(matches: List[str]) -> List[str]:
    name = matches[0]
    result = []
    for meal in meal_db:
        if name.lower() in get_name(meal).lower():
            result.append(get_mainIngredient(meal))
    return result








def mainIngredient_by_category(matches: List[str]) -> List[str]:
    category = matches[0]
    result = []
    for meal in meal_db:
        if category.lower() in get_category(meal).lower():
            result.append(get_mainIngredient(meal))
    return result








def mainIngredient_by_location(matches: List[str]) -> List[str]:
    location = matches[0]
    result = []
    for meal in meal_db:
        if location.lower() in get_location(meal).lower():
            result.append(get_mainIngredient(meal))
    return result




def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt








pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what is the recipe for %"), recipe_by_name),
    (str.split("where is % from"), location_by_name),
    (str.split("what places make %"), location_by_category),
    (str.split("what places use % as a main ingredient"), location_by_mainIngredient),
    (str.split("what places have meals that include %"), location_by_recipe),
    (str.split("what type of dish is %"), category_by_name),
    (str.split("what dishes are made in %"), category_by_location),
    (str.split("what type of dish uses %"), category_by_recipe),
    (str.split("what category of food is % the main ingredient in"), category_by_mainIngredient),
    (str.split("what is the main ingredient of a meal that contains %"), mainIngredient_by_recipe),
    (str.split("what is the main ingredient in %"), mainIngredient_by_name),
    (str.split("what are the main ingredients in % dishes"), mainIngredient_by_category),
    (str.split("what are some common main ingredients in % cuisine"), mainIngredient_by_location),
    (str.split("what meals contain %"), name_by_recipe),
    (str.split("what meals are _"), name_by_category),
    (str.split("what meals are from %"), name_by_location),
    (str.split("what meals use % as a main ingredient"), name_by_mainIngredient),
    (["bye"], bye_action),
]








def search_pa_list(src: List[str]) -> List[str]:
    user_input = ' '.join(src).lower()
   
    for pattern, action in pa_list:
        match_result = match(pattern, user_input.split())
        if match_result is not None:
            responses = action(match_result)
            if not responses:
                return ["No answers"]
            return responses
   
    return ["I don't understand"]








def query_loop() -> None:
    print("Welcome to the recipe database!")
    while True:
        try:
            query = input("what would you like to know? ").strip()
            if query.lower() == "bye":
                break
            responses = search_pa_list(query.lower().split())
            if responses == ["I don't understand"]:
                print("I don't understand")
            elif responses == ["No answers"]:
                print("No answers")
            else:
                for response in responses:
                    print(response)
        except KeyboardInterrupt:
            break
    print("\nGet outta here! ")











if __name__ == "__main__":
    query_loop()
