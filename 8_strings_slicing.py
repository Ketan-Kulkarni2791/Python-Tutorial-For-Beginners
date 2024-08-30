myStr = "Hello World"

print(myStr[2:7])                                       # o/p : llo W

print(myStr[:9])                                        # o/p : Hello Wor

print(myStr[4:])                                        # o/p : o World

print(myStr[:])                                         # o/p : Hello World

print(myStr[4:len(myStr)])                              # o/p : o World

print(myStr[:len(myStr)] + myStr[len(myStr):])            # o/p : Hello World

print(len(myStr))                                         # o/p : 11
print(myStr[len(myStr):])

print(myStr[4:4])                                          # o/p : ''
print(myStr[6:4])                                          # o/p : ''

# lhs : rhs