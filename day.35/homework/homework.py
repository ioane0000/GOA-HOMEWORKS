#Custom ფუნქცია (ანუ "ჩვენი ფუნქცია") არის ისეთი ფუნქცია, რომელსაც ჩვენ თვითონ ვწერთ, კონკრეტული ამოცანის შესასრულებლად.
def sum_numbers(a, b):
    return a + b  

num1 = int(input("num 1: "))
num2 = int(input("num 2:"))

result =  sum_numbers(num1, num2)
print("equals:", result)

#2

def check_even_or_odd(number):
    if number % 2 == 0:
        print("its odd")
    else:
        print("its even")

num = int(input("put your number"))

check_even_or_odd(num)

#3

def square_number(number):
    return number ** 2  

num = int(input("put your number: "))

result = square_number(num)
print("square of number:", result)

#4

def to_uppercase(text):
    return text.upper() 

user_text = input("text: ")

result = to_uppercase(user_text)
print("big letters:", result)

#5

def print_full_name(name, surname):
    print("users full name:", name, surname)
