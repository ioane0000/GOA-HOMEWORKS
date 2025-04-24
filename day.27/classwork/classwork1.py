def num1(a, b):
    return a * b

result = num1(10, 2)
print(result)

#2

def say_hello(name):
    print(f"hello, {name}")

name = "jumberi"
say_hello(name)

#3

def num(a, b, c):
    print(a + b + c)

num(5, 40, 15) 

#4

def num(a, b):
    return str(a) + str(b)

result = num("hello, ", "ushangi")
print(result)  

#5

#replace() მეთოდი გამოიყენება სტრიქონში არსებული ტექსტის სხვა ტექსტით ჩანაცვლებისთვის.
#იგი აბრუნებს ახალ სტრიქონს, სადაც ყველა მითითებული ნაწილი შეცვლილია მითითებული მნიშვნელობით.

#6

#upper() – ყველა ასოს აქცევს დიდ ასოდ.

#7

# N1
text = "i love programing"
position = text.find("programing")
print(position) 

# N2
sentence = "today is a good day"
index = sentence.find("lovely day")
print(index) 

#გვიბრუნებს პირველივე ადგილს, სადაც მოსაძებნი ტექსტი ჩანს.თუ ვერ პოულობს აბრუნებს -1-ს.

#8
# N1
text = "hello"
print(text.capitalize())

#2
name = "GIALO"
print(name.capitalize())

#9

# N1

text = "how you doing"
print(text.swapcase())

# N2

msg = "hello"
print(msg.swapcase())










