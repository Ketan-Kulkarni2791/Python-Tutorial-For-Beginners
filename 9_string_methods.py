# ------------------ capitalize() ------------------
# myStr = "heLLo WORLd"
# myStr = "Hello world"
# print(myStr.capitalize())           # o/p : Hello world

# # ------------------ casefold() ------------------
# myStr = "I LOVe PYThon"
# print(myStr.casefold())             # o/p : i love python

# ------------------ count() ------------------
myStr = "Python is a popular popular programming language!!"
print(myStr.count('p'))             # o/p : 5
print(myStr.count('popular'))       # o/p : 2

# ------------------ find() ------------------
myStr = "Python is a popular popular programming language!!"
print(myStr.find('popular'))        # o/p : 12

# ------------------ isalnum() ------------------
myStr = "Hello 123 world!!"
print(myStr.isalnum())              # o/p : False
myStr = "Hello123World"
print(myStr.isalnum())              # o/p : True

# ------------------ split() ------------------
myStr = "Python is a popular popular programming language!!"
print(myStr.split())                # o/p : ['Python', 'is', 'a', 'popular', 'popular', 'programming', 'language!!']

myStr = "Hello, world, what's, up"
print(myStr.split(','))             # o/p : ['Hello', ' world', " what's", ' up']
