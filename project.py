from match import match
from typing import List, Tuple, Callable, Any

def get_recipe():

def get_ingredient():

def get_time():

def recipe_by_ingredient():
    #takes input of ingredient and returns a list of recipes with that ingredient
def recipe_by_time():
    #takes input of how long a recipe will take and returns recipies with the same prep time
def recipe_by_time_range():
    #takes an input two prep times and returns all recipies that take less than the max and more than the minimum
def recipe_before_time():
    #takes an input of prep time and returns all recipies that take less time to prep

# Replace with your PHP URL
# url = 'https://www.themealdb.com/api/json/v1/1/random.php'

# # Send a GET request
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Print the response content
#     print(response.text)
# else:
#     print(f"Error: {response.status_code}")

# def query_loop() -> None:
#     """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
#     characters and exit gracefully.
#     """
#     print("Welcome to the cooking database!\n")
#     while True:
#         try:
#             print()
#             query = input("Your query? ").replace("?", "").lower().split()
#             answers = search_pa_list(query)
#             for ans in answers:
#                 print(ans)

#         except (KeyboardInterrupt, EOFError):
#             break

#     print("\nSo long!\n")
# link = ""
# f = urllib.request.urlopen(link)
# myfile = f.read()
# print(myfile)

