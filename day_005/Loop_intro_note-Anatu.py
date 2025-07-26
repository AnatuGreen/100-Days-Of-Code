#Loops allow us iterate through lists, strings and other iterable data structures and possibly do something with the individual results like run code 
#without repetition

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print((f"{fruit} Juice is healthy!"))

string = "Anatu"

for each in string:
    print(each) #String is iterable but int is not. List is also iterable
    
