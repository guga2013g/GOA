#                       0            1
favourit_fruit_list=["marwyvi" , "banani"]
print(favourit_fruit_list[0])
print(favourit_fruit_list[1])
 
movie_list=["ხვიჩა და გოჩა" , "რობიზონ კრუზო" , "10000 კილომეტრი წყალვ ქვეშ" , "ჩარლი ჩაპლინი" , "შაქრო და ზაქრო" ]
print(movie_list[0])
print(movie_list[1])
print(movie_list[2])
print(movie_list[3])

num=0

for i in range(10):

    num = i 


print()    
print(num)

animal_list=["dog" , "parrot" , "rabbit"]

friends_list = ["nika", "andria", "daviti"]


for friend in friends_list:
    print(f"gamarjoba {friend}")




favorite_colors = ["blue", "green", "red"]


favorite_colors.insert(0, "purple")


print(favorite_colors)


number_list = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]


print(number_list)


for i in range(10):
    print(i)


# შექმენი სია 10 წიგნის სახელით
book_list = [
    "tom soieris tavgadasavali",
    "kukaracha",
    "10000 kilometri wyal qvesh",
    "dzagli",
    "magdanas lurja",
    "xazarula",
    "deda",
    "boshebi",
    "didro",
    "patara princi"
]


favorite_book = "kukaracha"


try:
    index = book_list.index(favorite_book)
    print(f"The index of '{favorite_book}' is {index}.")
except ValueError:
    print(f"'{favorite_book}' is not in the list.")



cities_to_visit = [
    "Tokyo",
    "Paris",
    "New York",
    "Sydney",
    "Barcelona"
]


cities_to_visit.reverse()

print(cities_to_visit)

numbers = [1,2,3,4,5]
for number in numbers:
   result=number*2
   print(result)


fruits = ["apple", "banana", "orange"]


print(fruits)


 
numbers = [10, 20, 30, 40]


print(numbers[0])




cities = ["New York", "Paris", "Tokyo", "Sydney", "Barcelona"]


list_length = len(cities)


print("Number of elements in the list:", list_length)

