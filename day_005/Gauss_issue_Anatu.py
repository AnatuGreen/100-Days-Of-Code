#We can use the for loop with a range function to get all the numbers in a range
#either printed out or used by increments of 1 or we set the increment outselves

for num in range(1,12):
    print(num) #Will print 1,2,3...11. Range will not include the upper limit
    #If I want 12 added to the prints, I will have to make my range 1 to 13

for num2 in range(1,20, 2):
    print(num2) #1,3,5,7...

#Solving Gauss' problem

init = 0
for each in range(1,101):
    init += each
print(init) #5050
