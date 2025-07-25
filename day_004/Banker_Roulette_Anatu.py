import random

#Who will pay the bill game

# My solution:

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

rand_num_picker = random.randint(0,4)

print(f"Tonight the bill payer is: {friends[rand_num_picker]}!!!")

#Angela suggested using random.choice() as in the python doc

print(random.choice(friends)) # Very short and nice
