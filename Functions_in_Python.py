# Use of Functions in Python

# Functions in Python Definition
# def <function_name>(<parameters>):
#   <sentences>

# In Python there are two types of functions:
# - Built-in Functions      -> Original functions that doesn't need to be installed or defined
# - User-Defined Functions  -> Created by the User

# A Global Variable
lastName = "Boc"

# A Simple Print Function
def printFunction():
    print("First Function")

    # A Local Variable
    name = "Seba"

    # Print both Variables
    print("Name:", name, "LastName:", lastName)

printFunction()


# Functions with Parameters
def perimeterSquare(large, unit):
    perim = large*4
    print("The perimeter of the Square is:", perim, unit)
    return perim

# You can call the function with parameters setting the parameters in order, like below
perimeterSquare(25, "cms")

# But also you can call with parameters unordered if you put the name of each parameter
perimeterSquare( unit= "cms", large= 20)



# A Function in Python can return more than one result
# If we take a function that returns more than one result, it can be assigned to more than one variable as it is written below
# If the function returns different values but there is only one variable in the call, the return value is a tuple
def doubleAndTripleFunction(num):
    """Returns the Double and Triple value of the parameter"""
    double = num*2
    triple = num*3
    return double, triple

num5d, num5t = doubleAndTripleFunction(5)
print(num5d, num5t)

num10 = doubleAndTripleFunction(10)
print(num10)
    