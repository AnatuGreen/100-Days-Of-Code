states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(len(states_of_america)) #Checks the length of the list i.e how many items in it

# print(states_of_america[50]) # This will give a "IndexError: list index out of range" error because 50 is off by 1.
#The last item on the list above has index of 49 not 50. So we can get rid of this off by 1 error by removing 1 from the number of states

print(states_of_america[50-1]) #50-1 == 49 so it is same as print(states_of_america[49])

#We can make nested lists to group more related items in a list of generally related things

class_list_all = ["May", "Jane", "Emma", "Dan", "Chioma", "Henro"]
print(class_list_all)
#List males different and females diff but under same list
class_list_all = [["May", "Jane","Chioma",], ["Emma", "Dan",  "Henro"]]
print(class_list_all)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][2])
#When you have two nested lists or more, you can access what is in the second sub-list or 3rd by something like the above:
#Tomatoes is prnted because we aare saying: In the lst whose index comes just after the name of the main list, use the second supplied
#index to get the item at the second index.

