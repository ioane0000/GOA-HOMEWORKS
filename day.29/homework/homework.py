# 1

def num(numbers):
    total = 0
    for num in numbers:
        if num % 3 != 3:
            total += num
    return total

my_list = [1, 2, 3, 4, 5, 6, 7]
print(num(my_list))

# 2

def num1(name_list):
    result = []
    for name in name_list:
        if len(name) == 4:
            result.append(name)
    return result

names = ["Luka", "Nina", "Gio", "Ana", "Gela", "Dato"]
print(num1(names))

# 3

def num1(numbers):
    result = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            result.append(num)
    return result

nums = [10, 15, 30, 22, 45, 9, 50]
print(num1(nums))

# 4

#f-სტრინგი არის სპეციალური სტრიქონი Python-ში, რომელიც გამოიყენება ცვლადების და გამოსახულებების ჩასასმელად ტექსტში