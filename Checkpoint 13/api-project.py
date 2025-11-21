import requests
import random 

def get_movies():
    url = "https://api.watchmode.com/v1/"
    api_key = "qzZIdqeeAkLkHgoxh3r1sFLPv2RYtn3DiOZk4BTa"
    response = requests.get(url)
    return response.json()
def pick_random_movie(movies):
    return random.choice(movies)

def move_info(movie):
    print(f"Title: ",{movie["title"]})
    
