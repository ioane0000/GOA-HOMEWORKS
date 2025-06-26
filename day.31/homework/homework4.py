
my_name = "ioane"

user_name = input("Enter your name: ")

my_first = my_name[0].lower()
my_last = my_name[-1].lower()

user_first = user_name[0].lower()
user_last = user_name[-1].lower()

if my_first == user_first and my_last == user_last:
    print(2)
elif my_first == user_first or my_last == user_last:
    print(1)
else:
    print(0)
