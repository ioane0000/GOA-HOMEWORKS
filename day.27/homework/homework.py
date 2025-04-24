def to_uppercase(text):
    return text.upper()

result = to_uppercase("I love programming")
print(result)

#2

name = input("Enter your name: ")

first_letter = name[0].upper()

print("The first letter in uppercase is:", first_letter)

#3

sentence = input("Enter a sentence: ")

word = input("Enter the word you want to find: ")

position = sentence.find(word)

if position != -1:
    print(f"The word '{word}' was found at position {position}.")
else:
    print(f"The word '{word}' was not found in the sentence.")

#4

def num(arg1, arg2):
    upper_arg = arg1.upper()
    
    lower_arg = arg2.lower()
    
    result = upper_arg + lower_arg
    
    print("Result:", result)

    num("Hello", "WORLD")

