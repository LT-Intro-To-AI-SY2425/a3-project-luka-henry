from typing import List

meal_db: List[str, str, str, str, List[str]] = [
    (
        "Beef Brisket Pot Roast",  # name
        "Beef",  # main ingredient
        "Beef",  # category
        "USA", #location of meal
        [
            "Beef Brisket",
            "Salt",
            "Onion",
            "Garlic",
            "Thyme",
            "Rosemary",
            "Bay Leaves",
            "beef stock",
            "Carrots",
            "Mustard",
            "Potatoes"
        ],  # other inredients
    ),
    (
        "Three Fish Pie",  # name
        "Fish",  # main ingredient
        "Seafood",  # category
        "UK" #location of meal
        [
            "Potatoes",
            "Butter",
            "Milk",
            "Gruyère",
            "Butter",
            "Leek",
            "Plain Flour",
            "White Wine",
            "Milk",
            "Parsley",
            "Salmon",
            "Haddock",
            "Smoked Haddock",
            "Eggs"
        ],  # other inredients
    ),
    (
        "Kung Po Prawns",  # name
        "Prawns",  # main ingredient
        "Seafood",  # category
        "China" #location of meal
        [
            "Prawns",
            "Soy Sauce",
            "Tomato Puree",
            "Corn Flour",
            "Caster Sugar",
            "Sunflower Oil",
            "Peanuts",
            "Chilli",
            "Brown Sugar",
            "Garlic Clove",
            "Water Chestnut",
            "Ginger" 
        ],  # other inredients
    ),
    (
        "Irish stew",  # name
        "Beef",  # main ingredient
        "Beef",  # category
        "Ireland" #location of meal
        [
            "whole wheat",
            "lamb loin chops",
            "olive oil",
            "shallots",
            "carrots",
            "turnips",
            "celeriac",
            "charlotte potatoes",
            "white wine",
            "caster sugar",
            "fresh thyme",
            "oregano",
            "chicken stock"
        ],  # other inredients
    ),
    (
        "Chicken Basquaise",  # name
        "Chicken",  # main ingredient
        "Chicken",  # category
        "Italy" #location of meal
        [
            "Chicken",
            "Butter",
            "Olive Oil",
            "Red Onions",
            "Red Pepper",
            "Chorizo",
            "Sun-Dried Tomatoes",
            "Garlic",
            "Basmati Rice",
            "Tomato Puree",
            "Paprika",
            "Bay Leaves",
            "Thyme",
            "Chicken Stock",
            "Dry White Wine",
            "Lemons",
            "Black Olives",
            "Salt",
            "Pepper"
        ],  # other inredients
    ),
    (
        "Boulangère Potatoes",  # name
        "Potatoes",  # main ingredient
        "Side",  # category
        "France" #location of meal
        [
            "Onions",
            "Thyme",
            "Olive Oil",
            "Potatoes",
            "Vegetable Stock"
        ],  # other inredients
    ),
    (
        "Chocolate Souffle",  # name
        "Chocolate",  # main ingredient
        "Dessert",  # category
        "France" #location of meal
        [
            "Single Cream",
            "Caster Sugar",
            "Dark Chocolate",
            "Butter",
            "Butter",
            "Caster Sugar",
            "Dark Chocolate",
            "Double Cream",
            "Egg Yolks",
            "Egg White",
            "Double Cream",
            "Icing Sugar"
        ],  # other inredients
    ),
    (
        "Spanish Tortilla",  # name
        "Potatoes",  # main ingredient
        "Vegetarian",  # category
        "Spain" #location of meal
        [
            "Onion",
            "Olive Oil",
            "Butterm",
            "Potatoes",
            "Garlic",
            "Eggs",
            "Parsley",
            "Baguette",
            "Vine Tomatoes",
        ],  # other inredients
    ),
    (
        "Beef stroganoff",  # name
        "Beef",  # main ingredient
        "Beef",  # category
        "Russia" #location of meal
        [
            "Olive Oil",
            "Onions",
            "Garlic",
            "Butterm",
            "Mushrooms",
            "Beef Fillet",
            "Plain Flour",
            "Creme Fraiche",
            "English Mustard",
            "Beef Stock",
            "Parsley"
        ],  # other inredients
    ),
    (
        "Chicken Enchilada Casserole",  # name
        "Chicken",  # main ingredient
        "Chicken",  # category
        "Mexico" #location of meal
        [
            "Enchilada sauce",
            "shredded Monterey Jack cheese",
            "corn tortillas",
            "chicken breasts"

        ],  # other inredients
    ),
    (
        "Cajun spiced fish tacos",  # name
        "Fish",  # main ingredient
        "Seafood",  # category
        "Mexico" #location of meal
        [
            "cajun",
            "cayenne pepper",
            "white fish",
            "vegetable oil",
            "flour tortilla",
            "avocado",
            "little gem lettuce",
            "spring onion",
            "salsa",
            "sour cream",
            "lemon",
            "garlic"

        ],  # other inredients
    ),
    (
        "Krispy Kreme Donut",  # name
        "Donut",  # main ingredient
        "Dessert",  # category
        "USA" #location of meal
        [
            "Yeast",
            "Water",
            "Sugar",
            "Salt",
            "Eggs",
            "Shortening",
            "Flour",
            "Canola Oil",
            "Milk",
            "Sugar",
            "Vanilla",
            "Boiling Water",
            "Butter"
        ],  # other inredients
    ),
    (
        "Pumpkin Pie",  # name
        "Pumpkin",  # main ingredient
        "Dessert",  # category
        "USA" #location of meal
        [
            "Pumpkin",
            "Shortcrust Pastry",
            "Plain Flour",
            "Caster Sugar",
            "Salt",
            "Nutmeg",
            "Cinnamon",
            "Eggs",
            "Butter",
            "Milk",
            "Icing Sugar"
        ],  # other inredients
    ),
    (
        "Grilled eggplant with coconut milk",  # name
        "Eggplant",  # main ingredient
        "Vegetarian",  # category
        "Philippines" #location of meal
        [
            "Egg Plants",
            "Coconut Milk",
            "Lemon Juice",
            "Salt",
            "Red Pepper Flakes",
            "Onions"

        ],  # other inredients
    ),
    (
        "Lasagne",  # name
        "Lasagne",  # main ingredient
        "Pasta",  # category
        "Italy" #location of meal
        [
            "Olive Oil",
            "Bacon",
            "Onion",
            "Celery",
            "Carrots",
            "Garlic",
            "Minced Beef",
            "Tomato Puree",
            "Chopped Tomatoes",
            "Honey",
            "Lasagne Sheets",
            "Creme Fraiche",
            "Mozzarella Balls",
            "Parmesan Cheese",
            "Basil Leaves"
        ],  # other inredients
    ),
    (
        "Brown Stew Chicken",  # name
        "Chicken",  # main ingredient
        "Chicken",  # category
        "Jamaica" #location of meal
        [
            "Chicken",
            "Tomato",
            "Onions",
            "Garlic Clove",
            "Red Pepper",
            "Carrots",
            "Lime",
            "Thyme",
            "Allspice",
            "Soy Sauce",
            "Cornstarch",
            "Coconut Milk",
            "Vegetable Oil"
        ],  # other inredients
    ),
    
]