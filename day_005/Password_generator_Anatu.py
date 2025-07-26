#Random password generator
#Version 1: The easy

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ""

for each in range(1,nr_letters+1):
    random_letter = random.choice(letters)
    #print(random.choice(letters))
    password+=random_letter
   # print(password)

for each in range(1,nr_symbols+1):
    random_symb = random.choice(symbols)
    #print(random.choice(letters))
    password+=random_symb
   # print(password)

for each in range(1,nr_numbers+1):
    random_num = random.choice(numbers)
    #print(random.choice(letters))
    password+=random_num

print(password)
print(len(password)) #Length of password

# Now make the Password even harder. Just transform the already generated one

harder_pass = "" #Have a different accumulator for the string that will become a harder password
for each in range(1,len(password)+1):
    harder_pass += random.choice(password) #Randomize the already existing password

print(harder_pass)

