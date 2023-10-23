# Python program to show how to access tuple elements    
# Creating a tuple    
tuple_ = ("Python", "Tuple", "Ordered", "Collection")    
print(tuple_[0])        # o/p: Python
print(tuple_[1])        # o/p: Tuple   
# trying to access element index more than the length of a tuple    
try:    
    print(tuple_[5])     
except Exception as e:    
    print(e)            # o/p: tuple index out of range   
# trying to access elements through the index of floating data type    
try:    
    print(tuple_[1.0])     
except Exception as e:    
    print(e)            # o/p: tuple indices must be integers or slices, not float   
# Creating a nested tuple    
nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))
# Accessing the index of a nested tuple    
print(nested_tuple[0][3])   # o/p: 1         
print(nested_tuple[1][1])   # o/p: 6


# Python program to show how negative indexing works in Python tuples    
# Creating a tuple    
tuple_ = ("Python", "Tuple", "Ordered", "Collection")    
# Printing elements using negative indices    
print("Element at -1 index: ", tuple_[-1])                  
# o/p: Element at -1 index:  Collection 
print("Elements between -4 and -1 are: ", tuple_[-4:-1])
# o/p: Elements between -4 and -1 are:  ('Python', 'Tuple', 'Ordered')


# Python program to show how slicing works in Python tuples    
# Creating a tuple    
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")    
# Using slicing to access elements of the tuple    
print("Elements between indices 1 and 3: ", tuple_[1:3])
# o/p: Elements between indices 1 and 3:  ('Tuple', 'Ordered')  
# Using negative indexing in slicing    
print("Elements between indices 0 and -4: ", tuple_[:-4])
# o/p: Elements between indices 0 and -4:  ('Python', 'Tuple')
# Printing the entire tuple by using the default start and end values.     
print("Entire tuple: ", tuple_[:])
# o/p: Entire tuple:  ('Python', 'Tuple', 'Ordered', 'Immutable', 'Collection', 'Objects')


# Python program to show how to delete elements of a Python tuple    
# Creating a tuple    
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")    
# Deleting a particular element of the tuple    
try:     
    del tuple_[3]    
    print(tuple_)    
except Exception as e:    
    print(e)            # o/p: 'tuple' object does not support item deletion  
# Deleting the variable from the global space of the program    
del tuple_    
# Trying accessing the tuple after deleting it    
try:    
    print(tuple_)    
except Exception as e:    
    print(e)            # o/p: name 'tuple_' is not defined 
    

# Python program to show repetition in tuples    
tuple_ = ('Python',"Tuples")    
print("Original tuple is: ", tuple_)        # o/p: Original tuple is:  ('Python', 'Tuples')  
# Repeting the tuple elements    
tuple_ = tuple_ * 3    
print("New tuple is: ", tuple_)   
# o/p: New tuple is:  ('Python', 'Tuples', 'Python', 'Tuples', 'Python', 'Tuples')


# Creating tuples  
T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)  
T2 = ('python', 'java', 'python', 'Tpoint', 'python', 'java')  
# counting the appearance of 3  
res = T1.count(2)  
print('Count of 2 in T1 is:', res)      # o/p: Count of 2 in T1 is: 5 
# counting the appearance of java  
res = T2.count('java')  
print('Count of Java in T2 is:', res)   # o/p: Count of java in T2 is: 2



my_tuple = ( 4, 2, 5, 6, 7, 5)
print(my_tuple.index(5))        # o/p: 2

# Creating tuples
Tuple = ( 1, 3, 4, 2, 5, 6 )
# getting the index of 3
res = Tuple.index(3)
print('Index of 3 is', res)     # o/p: Value of Index of 3 is 1


# Creating tuples
Tuple = ( 3, 3, 5, 7, 3, 3 )
# getting the index of 3
res = Tuple.index(3)
print('Index of 3 is', res)     # o/p: Index of 3 is 0

# alphabets tuple
alphabets = ('G', 'e', 'e', 'k', 's', 'f', 'o',
             'r', 'G', 'e', 'e', 'k', 's')
# scans 'G' from index 4 to 10 and returns its index
index = alphabets.index('G', 4, 10)
print('Index of G in alphabets from index 4 to 10:', index)
# o/p: Index of G in alphabets from index 4 to 10: 8


t = ('G', 'F', 'G')
# accessing element not present in the tuple
print(t.index('i'))
# o/p: ValueError: tuple.index(x): x not in tuple


# Python program to show how to perform membership test for tuples    
# Creating a tuple    
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")    
# In operator    
print('Tuple' in tuple_)            # o/p: True   
print('Items' in tuple_)            # o/p: False  
# Not in operator    
print('Immutable' not in tuple_)    # o/p: False    
print('Items' not in tuple_)        # o/p: True


# Python program to show how to iterate over tuple elements    
# Creating a tuple    
tuple_ = ("Python", "Tuple", "Ordered", "Immutable")    
# Iterating over tuple elements using a for loop    
for item in tuple_:    
    print(item)




# Python3 code to demonstrate working of Edit objects inside tuple Using Access Methods
# initializing tuple
test_tuple = (1, [5, 6, 4], 9, 10)
# printing original tuple
print("The original tuple : " + str(test_tuple))
# o/p: The original tuple : (1, [5, 6, 4], 9, 10)
# Edit objects inside tuple Using Access Methods
test_tuple[1][2] = 14       
# printing result
print("The modified tuple : " + str(test_tuple))
# o/p: The modified tuple : (1, [5, 6, 14], 9, 10)



# Python3 code to demonstrate working of Edit objects inside tuple Using pop() + index()
# initializing tuple
test_tuple = (1, [5, 6, 4], 9, 10)
# printing original tuple
print("The original tuple : " + str(test_tuple))
# o/p: The original tuple : (1, [5, 6, 4], 9, 10)
# Edit objects inside tuple Using pop() + index()
test_tuple[1].pop(2)
test_tuple[1].insert(2, 14)    
# printing result
print("The modified tuple : " + str(test_tuple))
# o/p: The modified tuple : (1, [5, 6, 14], 9, 10)




# Initial tuple
my_tuple = (1, 2, 3, 4, 5)
# Convert the tuple to a list
my_list = list(my_tuple)
# Edit the list
my_list[2] = 10
# Convert the list back to a tuple
my_tuple = tuple(my_list)
# Print the updated tuple
print(my_tuple)
# o/p: (1, 2, 10, 4, 5)



# Using lambda function to modify the tuple
modify_tuple = lambda tup, index, new_val: tup[:index] + (new_val,) + tup[index+1:]
# Example usage
tup = (1, [5, 6, 4], 9, 10)
new_tup = modify_tuple(tup, 1, [5, 6, 14])
print(new_tup)
# o/p: (1, [5, 6, 14], 9, 10)



# Initial tuple
my_tuple = (1, 2, 3, 4, 5)
# Convert the tuple to a list
my_list = list(my_tuple) 
# Edit the list using slicing
my_list[2:3] = [10]
# Convert the list back to a tuple
my_tuple = tuple(my_list)
# Print the updated tuple
print(my_tuple)     # o/p: (1, 2, 10, 4, 5)



# Given input
tpl = (1, [5, 6, 4], 9, 10)
# Create a new tuple with the modified object
modified_tpl = tpl[:1] + ([tpl[1][0], tpl[1][1], 14] + tpl[1][3:],) + tpl[2:]
# Output
print("The modified tuple:", modified_tpl)
# o/p: The modified tuple: (1, [5, 6, 14], 9, 10)


# --------------------------------------- Unpack Tuple Items -------------------------------------

t1 = (1 ,2)
t1 = 1 ,2
type (t1)       # o/p: <class 'tuple'>

tup1 = (10,20,30)
x, y, z = tup1
print ("x: ", x, "y: ", "z: ",z)    # o/p: x: 10 y: 20 z: 30

tup1 = (10,20,30)
x, y = tup1             # o/p: ValueError: too many values to unpack (expected 2)
x, y, p, q = tup1       # o/p: ValueError: not enough values to unpack (expected 4, got 3)

tup1 = (10,20,30)
x, *y = tup1
print ("x: ", "y: ", y) # o/p: x: y: [20, 30]

tup1 = (10,20,30, 40, 50, 60)
x, *y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)     # o/p: x: 10 y: [20, 30, 40, 50] z: 60

tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)     # o/p: x: [10, 20, 30, 40] y: 50 z: 60
