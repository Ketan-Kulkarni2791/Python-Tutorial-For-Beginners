# Python program to show how to create a tuple    
# Creating an empty tuple    
empty_tuple = ()    
print("Empty tuple: ", empty_tuple)    
    
# Creating tuple having integers    
int_tuple = (4, 6, 8, 10, 12, 14)    
print("Tuple with integers: ", int_tuple)    
    
# Creating a tuple having objects of different data types    
mixed_tuple = (4, "Python", 9.3)    
print("Tuple with different data types: ", mixed_tuple)    
    
# Creating a nested tuple    
nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))    
print("A nested tuple: ", nested_tuple)  


# Python program to create a tuple without using parentheses    
# Creating a tuple    
tuple_ = 4, 5.7, "Tuples", ["Python", "Tuples"]    
# Displaying the tuple created    
print(tuple_)
# o/p: (4, 5.7, 'Tuples', ['Python', 'Tuples'])
# Checking the data type of object tuple_    
print(type(tuple_) )
# o/p: <class 'tuple'>  
# Trying to modify tuple_    
try:    
    tuple_[1] = 4.2    
except:    
    print(TypeError )
    # o/p: <class 'TypeError'>
    

# Python program to show how to create a tuple having a single element    
single_tuple = ("Tuple")    
print( type(single_tuple) )     # o/p: <class 'str'>   
# Creating a tuple that has only one element    
single_tuple = ("Tuple",)    
print( type(single_tuple) )     # o/p: <class 'tuple'>   
# Creating tuple without parentheses    
single_tuple = "Tuple",    
print( type(single_tuple) )     # o/p: <class 'tuple'> 