a = 100
print(a)    # o/p --> 100

# Chain of assignment
a = b = c = 100
print(a, b, c)      # o/p --> 100 100 100

# Same variable can be used for different datatype
a = 13.5
print(a)  # o/p --> 13.5
var = "Now I m a string"
print(var)  # o/p --> Now I m a string

n = 300
print(n)

print(type(n))          # o/p: <class 'int'>

m = n
print(n, m)             # o/p: 300 300

m = 400
print(n, m)             # o/p: 300 400

m = n
print(n, m)


n = "Shobha"


abc = def1 = ghi = 1000
print(abc, ghi)                     # o/p : 1000 1000

abc = def1 = ghi = "Shobha"
print(def1)                         # o/p : Shobha

ghi = 500.500
print(abc, ghi)                     # o/p : Shobha 500.5

print(id(abc))                      # o/p : 1990347391984
print(id(def1), id(ghi))            # o/p : 1990347391984 1990347119120



######################################### Datatypes #########################################

# Integer

print(123123123123123123123123123123123123123123123123 + 1)
# o/p --> 123123123123123123123123123123123123123123123124

# Floating Point Numbers

print(4.2)          # o/p : 4.2
print(type(4.2))    # o/p : <class 'float'>
print(4.0)          # o/p : 4.0
print(0.2)          # o/p : 0.2
print(.2)           # o/p : 0.2

# String

print("Hello World")
print(type("Hello World"))  # o/p : <class 'str'>

print('Hello\n World')
print(type('Hello World'))  # o/p : <class 'str'>
