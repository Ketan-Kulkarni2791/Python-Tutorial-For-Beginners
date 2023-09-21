# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello World")

# checks if list still contains any element
a = [1, 2, 3, 4]
while a:
    print(a.pop())
print("Now the list is empty!")

# Python program to illustrate Single statement while block
count = 0
while (count < 5): count += 1; print("Hello World")

# Python program to demonstrate while-else loop
 
i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
 
i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")
    
    
# Initialize a counter
count = 0
 
# Loop infinitely
while True:
    # Increment the counter
    count += 1
    print(f"Count is {count}")
 
    # Check if the counter has reached a certain value
    if count == 10:
        # If so, exit the loop
        break
 
# This will be executed after the loop exits
print("The loop has ended.")

