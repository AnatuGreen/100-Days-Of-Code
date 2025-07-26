student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

#Using for loop to get the max number in a list
#My solution
max_num = student_scores[0] #Start with assumption that the first score is the highest one and assign that a variable
for score in student_scores: #loop through the scores
    if score > student_scores[0]: #If you see any score greater than the initial,
        max_num = score     # Let it overwrite the already set max number
print(max_num)  #When all is done, print out the new max numb if any or print the original one if it stands. Note the indentation so that we have only one print
