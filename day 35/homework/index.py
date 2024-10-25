user_food = []
for _ in range(10):
    food = input("რა გსურთ გასტუმრებლად? ")
    user_food.append(food)

print("თქვენი საჭმელი:", user_food)
movies = ["ფილმი 1", "ფილმი 2", "ფილმი 3"]

reversed_movies_1 = movies[::-1]

reversed_movies_2 = []
for movie in movies:
    reversed_movies_2.insert(0, movie)

print("პირველი ატრიალება:", reversed_movies_1)
print("მეორე ატრიალება:", reversed_movies_2)
name = "გიორგი დავითაშვილი"
none_name = ""
for letter in name:
    none_name += letter + "გოა"

print("შედეგი:", none_name)

