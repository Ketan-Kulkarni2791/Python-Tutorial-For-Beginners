""" Python program to find unique numbers in a given tuple """

T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
T2 = ()

for i in T1:
    if not i in T2:
        T2 += (i,)

print(T2)


""" Python program to find sum of all numbers in a tuple """

T1 = (1, 9, 1, 6, 3, 4)
T2 = 0

for i in T1:
    T2 += i
print(T2)

T2 = sum(T1)
print(T2)




