#def calculating functions

def multiplication(num1, num2):
    return num1 * num2

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

#user enter numbers
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

#choose operations
print("Select operation 1-Add, 2-Sub, 3-Mul, 4-Divide")
operation = int(input("Choose operation 1/2/3/4: "))

if operation == 1:
    print(addition(num1, num2))

elif operation == 2:
   print(subtraction(num1, num2))

elif operation == 3:
   print(multiplication(num1, num2))

elif operation == 4:
   print(divide(num1, num2))

else:
   print("Enter correct operation")