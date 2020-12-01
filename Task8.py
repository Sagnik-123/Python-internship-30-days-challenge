# List down all the error types and check all the errors using a python program for all errors

print("So today we will get to know the ,different types of errors so Let's start")
# 1
print("1.Indexing error")
lsr = [10, 22, 42]
try:
    print(lsr[22])
except IndexError:
    print("The index is not found in the array")
# 2
print("2.Key error")
dic = {"Sagnik": "Dumdum", "Anik": "Belgharia", "Amin": "Kolkata"}
try:
    print(dic["Sam"])
except KeyError:
    print("Key not found in the respective dictionary")

# 3
print("3.Module Not Found Error")
try:
    import bytecode
except ModuleNotFoundError:
    print("The Module is not found and installed")

# 4
print("4.Division by zero Error")
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Divide by zero error enter other number")
    
    
# Design an simple calculator with try and except for all use cases


print("This is my first calculator in python")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4. DIVISION")

cal = int(input("Enter the choice you want to enter: 1 to 4 "))

if cal == 1:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    ans = a + b
    print("Addition = ", ans)

elif cal == 2:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    ans = a - b
    print("Subtract = ", ans)

elif cal == 3:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    ans = a * b
    print("Multiply = ", ans)

elif cal == 4:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    try:
        if b == 0:
            print("Division not possible")

    except ZeroDivisionError:
        print("Enter value other than zero")
    ans = a / b
    print("Divide= ", ans)

else:
    print("You have made an invalid choice")
    print("***** BYE *****")

# Print one message if the try block raises a NameError and another for other errors

try:
    print(y)
except NameError:
    print("The variable y is not defined")
except:
    print("Something else")

# Try getting an input inside the try except block

try:
    string = input("Enter a string : ")
    string_int = int(string)
    print(string_int)
except ValueError:
    print("Please enter a integer")




