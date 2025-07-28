#Make turn right function using 3 turn lefts
def turn_right():
     turn_left()
     turn_left()
     turn_left()

# All Required for each complete jump or move (updated)
# shall be made into a function
def one_jump():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    

while not at_goal():
    one_jump()   
done()
        

    
