#this python code is only for Reeborg's World. that is why your ide will not recognize the functions.
#you can run this code in reeborg's world.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def move_robot():
    while front_is_clear() == True:
        move()
    while not at_goal() and front_is_clear() == True:
        move()
    if wall_in_front() == True:
        jump()
    elif front_is_clear() == True:
        move()
    elif not at_goal() and front_is_clear() == True:
        move()
    
while at_goal() != True:
    move_robot()
    
if at_goal() == True:
    done()