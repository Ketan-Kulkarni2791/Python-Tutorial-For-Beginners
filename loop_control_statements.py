# # Continue statement
# for var in "Helloo World":
#     if var == "o":
#         continue
#     print(var)
#     print("Virat Kohli")


# # loop from 1 to 10
# for i in range(1, 11):
#     # If i is equals to 6,
#     # continue to next iteration
#     # without printing
#     if i == 6:
#         continue
#         print(i)
#     else:
#         # otherwise print the value
#         # of i
#         print(i, end=" ")               # Plz revise 'print' topic. 
        

# # Break Statement
# for i in range(10):
#     print(i)
#     if i == 2:
#         break

# # Python program to demonstrate break statement
  
# s = 'Helllooo World'
# # Using for loop
# for letter in s:
#     print(letter)
#     # break the loop as soon it sees 'l'
#     # or 'o'
#     if letter == 'l' or letter == 'o':          # Plz revise operators topic
#         break 
# print("Out of for loop"    )
# print()
  
# i = 0
  
# # Using while loop
# while True:
#     print(s[i])
#     # break the loop as soon it sees 'e'
#     # or 's'
#     if s[i] == 'e' or s[i] == 's':
#         break
#     i += 1
# print("Out of while loop ")

# num = 0
# for i in range(10):
#     num += 1
#     if num == 8:
#         break
#     print("The num has value:", num)
# print("Out of loop")


# # Pass Statement
# def my_function():
#     pass

# n = 10
# for i in range(n): 
#   # pass can be used as placeholder
#   # when code is to added later
#   pass

a = 10
b = 20
if(a<b):                # Plz revise if-else topic
  pass
else:
  print("b<a")
  
