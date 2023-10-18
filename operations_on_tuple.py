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