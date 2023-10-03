Var = ["Chandlar", "Joey", "Ross"]
print(Var)

# Python program to demonstrate Creation of List
 
# Creating a List
List = []
print("Blank List: ")
print(List)
 
# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
 
# Creating a List of strings and accessing using index
List = ["Monica", "Rachel", "Pheebe"]
print("\nList Items: ")
print(List[0])
print(List[2])

# Creating a List with the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)
 
# Creating a List with mixed type of values (Having numbers and strings)
List = [1, 2, 'The 100', 4, 'For', 6, 'The Office']
print("\nList with the use of Mixed Values: ")
print(List)

# Python program to demonstrate accessing of element from list
 
# Creating a List with the use of multiple values
List = ["Lagaan", "Vastav", "Tumbaad"]
 
# accessing a element from the list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['The Last Czar', 'Sense and Sensibility'], ['The Crown']]
 
# accessing an element from the Multi-Dimensional List using index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])


List = [1, 2, 'The 100', 4, 'For', 6, 'The Office']
 
# accessing an element using negative indexing
print("Accessing element using negative indexing")
 
# print the last element of list
print(List[-1])
 
# print the third last element of list
print(List[-3])


# Creating a List
List1 = []
print(len(List1))
 
# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))


# To take space separated input as a string split and store it to a list and print the string list
 
# input the list as string
string = input("Enter elements (Space-Separated): ")
 
# split the strings and store it to a list
lst = string.split() 
print('The list is:', lst)   # printing the list


# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input("Enter the integer elements:").strip().split()))[:n]
 
# printing the list
print('The list is:', lst) 