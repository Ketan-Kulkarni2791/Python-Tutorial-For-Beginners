# A simple Python function
def my_fun():
  print("Hello World")
  
# Driver code to call a function
my_fun()


# Here a,b are the parameters
def sum(a,b):
  print(a+b)
    
sum(1,2)


def sum(a,b):
  print(a+b)
    
# Here the values 1,2 are arguments
sum(1,2)

#### Positional argument
def person_name(first_name,second_name):
  print(first_name+second_name)
    
# First name is Chandlar placed first
# Second name is Bing place second
person_name("Chandlar","Bing")

#### Keyword Arguement
def person_name(first_name,second_name):
  print(first_name+second_name)
  
# Here we are explicitly assigning the values 
person_name(second_name="Bing",first_name="Chandlar")


# Python Function With Parameters
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
 
    return num3
 
# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

#### Python function with default argument
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
 
 
# Driver code (We call myFun() with only argument)
myFun(10)


#### Example 1: Variable length non-keywords argument
# Python program to illustrate *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Chandlar', 'Rachel', 'Joey', 'Monica', 'Pheebe', 'Ross')


#### Example 2: Variable length keyword arguments
# Python program to illustrate *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# Driver code
myFun(first='Hello', mid='MF', last='World')