def say_hello():
    print("გამარჯობა!")


def sum_two_numbers(a, b):
    return a + b

def calculate_age(birth_year):
    current_year = 2024  
    return current_year - birth_year


def multiply(x, y):
    return x * y


def repeat_twice(word):
    return word * 2


if __name__ == "__main__":

    say_hello()


    result_sum = sum_two_numbers(5, 7)
    print(f"ჯამი: {result_sum}")


    age = calculate_age(1990)
    print(f"თქვენი ასაკი: {age} წლის.")


    result_multiply = multiply(3, 4)
    print(f"ნამრავლი: {result_multiply}")

  
    repeated_word = repeat_twice("გამარჯობა")
    print(f"გამეორებული სიტყვა: {repeated_word}")
