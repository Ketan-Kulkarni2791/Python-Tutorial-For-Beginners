n = 4
for i in range(0, n):
    print(i)

# Question: iterable vs non-iterable in python

# Iterating over a list
print("List Iteration")
l = ["Rachit", "Ketan", "Rahul"]
print(l)
print(type(l))              # o/p: <class 'list'>
for i in l:
    print(i)
    print(type(i))          # o/p: <class 'str'>
    if i == "Rahul":
        print("Naam to suna hi hoga !")
    

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("Rachit", "Ketan", "Rahul")
for i in t:
    print(i)
    

# Iterating over a String
print("\nString Iteration")
s = "Hello World"
for i in s:
    print(i)
    

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)