
def calculate_sum(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0

def greet_user(name):
    print(f"გამარჯობა, {name}!")


def calculate_user_inputs():
    a = int(input("შეიყვანეთ პირველი მთელი რიცხვი: "))
    b = int(input("შეიყვანეთ მეორე მთელი რიცხვი: "))
    total = calculate_sum(a, b)
    print(f"ჯამი: {total}")


def check_number():
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number > 5:
        return "შენ გადახვედი შემდეგ ეტაპზე"
    else:
        return "შენ არ გადახვედი შემდეგ ეტაპზე"
