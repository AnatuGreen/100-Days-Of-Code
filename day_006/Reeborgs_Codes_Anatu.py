#Reeborg's Part 1

def turn_right():
     turn_left()
     turn_left()
     turn_left()
     
def make_square():
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()

make_square()

# Part 2

#Make turn right function using 3 turn lefts
def turn_right():
     turn_left()
     turn_left()
     turn_left()

#All Required for each complete jump shall be made into a function
def one_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#We need 6 jumps to complete challenge so define loop with range

for jump in range(1,7):
    one_jump()



