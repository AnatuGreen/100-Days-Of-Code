#FizzBuzz

#Had to reverse engineer this one. 

for each in range(1,101):
    if each % 3 == 0 and each % 5 ==0: #Divisible by 3 and by 5
        each = "FizzBuzz"
        print(each)
    elif each % 5 == 0 and each % 3 != 0: #Divisible by 5 and not by 3
        each = "Buzz"
        print(each)
    elif each % 3 == 0 and each % 5 != 0: #Divisible by 3 and not by 5
        each = "Fizz"
        print(each)
    else:
        print(each) #All others
        
