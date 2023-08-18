# Int to Float

a = 5
f = float(a)
print(f)                    # o/p --> 5.0
print(type(f))              # o/p --> <class 'float'>

# Float to Int

a = 5.9
i = int(a)
print(i)                    # o/p --> 5
print(type(i))              # o/p --> <class 'int'>

# Int to String

a = 5
s = str(a)
print(s)                    # o/p --> 5
print(type(s))              # o/p --> <class 'str'>

print(5 + a)                # o/p --> 10
# print(5 + s)              # o/p --> TypeError: unsupported operand type(s) for +: 'int' and 'str'

# String to Float

a = "5.9"
f = float(a)
print(f)                    # o/p --> 5.9
print(type(f))              # o/p --> <class 'float'>

# String to Int

a = 5
b = 't'

n = int(a)
print(n)                    # o/p --> 5
print(type(n))              # o/p --> <class 'int'>

x = "5"
y= "4"
print(x + y)                # o/p --> 54 Concatenation of strings
print(int(x) + int(y))      # o/p --> 9

print(int(b))               # o/p --> ValueError: invalid literal for int() with base 10: 't'
print(type(b))



