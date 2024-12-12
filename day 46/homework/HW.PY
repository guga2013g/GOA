# 1

import random

def random_animal():
    animals = ["dog", "d", "sadd", "tt", "es", "bear"]
    random_animal = random.choice(animals)
    print(f"New random animal: {random_animal}")


random_animal()

# 2

import random

def random_movies():
    movies = ["Inception", "The Dark Knight", "Titanic", "The Matrix", "Interstellar", "The Godfather"]
    random_movies = random.sample(movies, 4)  
    print("Your random 4 movies are:")
    for movie in random_movies:
        print(movie)


random_movies()

# 3

import random

def random_name():
    names = ["John", "Alice", "Bob", "Eve", "Charlie"]
    name_str = ""
    for _ in range(5):  
        name_str += random.choice(names) + " <3 "
    print(name_str)


random_name()

# 4

import random

def random_fruit():
    fruits = ["apple", "MAN", "CURRY", "IDK"]
    favorite_fruit = random.choice(fruits)
    print(f"Your favorite random fruit is: {favorite_fruit}")


random_fruit()

# 5

import random

def favorite_animals():
    animals_list = []
    for i in range(4):
        animal = input(f"Please enter your favorite animal #{i+1}: ")
        animals_list.append(animal)
    random_animal = random.choice(animals_list)
    print(f"Your random favorite animal is: {random_animal}")

favorite_animals()
