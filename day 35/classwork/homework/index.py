
user_food = []

for i in range(10):
    food = input("შეიყვანეთ საჭმლის სახელი: ")  
    user_food.append(food)  

print("თქვენი საჭმლების სია: ", user_food)

movies = ["Inception", "The Dark Knight", "Interstellar", "The Prestige", "Memento"]


reversed_movies_1 = list(reversed(movies))
print("ფილმების სია 1 მეთოდით:", reversed_movies_1)


reversed_movies_2 = movies[::-1]
print("ფილმების სია 2 მეთოდით:", reversed_movies_2)


first_name = "გიგი"
last_name = "მამასახლიშვილი"


full_name = first_name + " " + last_name


none_name = ""


for letter in full_name:
    none_name += letter + "გოა"  

print("შექმნილი ცვლადი none_name:", none_name)
