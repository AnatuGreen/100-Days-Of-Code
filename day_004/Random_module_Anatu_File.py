import random
import my_module

# rand_integ=random.randint(1, 10)
# #The a: before 1 and b: before 10 above are pycharm hints. Do not write in your own code
# print(rand_integ)
# #Print something from a module created by me
# print(my_module.my_full_name)
#
# #How do we create random floating numbers
# #We use random floating using random.random() where. The float will be between 0 (included) and 1 (not included).
# #The 1st random is the module and the second is the function of the module.
#
# print(random.random()) # we can put it in a variable
#
# #Also, we can expand the random float by multiplying it with an integer of choice like 5 10 30 etc.
#
# random_0_to_20 = random.random() * 20
# #This will be a rand numb from 0 to 20
# # but not including 20 because each random float that is generated will multiply the int given, First the lower range (0)
# # will mult the int then the uper side of the range will
# print(random_0_to_20)

# There is also random.uniform(a,b) which will take two arguments
#
# Let us do a heads or tails game based on random number generated
#For this I will use round() to round the generated random float

print(round(random.random() * 10))

random_numb = round(random.random() * 10)

if random_numb <= 5:
    print("Heads")
else:
    print("Tails")

# randomint() would have been used for this too
