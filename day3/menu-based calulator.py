# def greet():
#     print("Wellcome to Python!")
# greet()


# def square(number):
#     return number ** 2

# result = square(5)
# print(result)


# def cube(number):
#     return number ** 3

# result = cube(3)
# print(result)


# def square(number):
#     print(number ** 2)

# square(5)
# square(25)
# square(50)

# def maximum(a,b):
#     if a>b:
#         return a 
#     else:
#         return b

# result = maximum(90,76)
# print(result)
    

# def marimum(a,b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
#     else:
#         return ("both numbers are equal")

# result = maximum(50,50)
# print(result)    


def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b

print(add(10 , 8))
print(subtract(46 , 29))
print(multiply(63 , 77))
print(divide(88 , 47))

while True:
    print("\n-------calculator-------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("enter your choice(1-5): ")
    print("You selected:", choice)
    if choice == "5":
       print("thank you for using the calculator!")
       break 

    if choice in ["1","2","3","4"]:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

    if choice == "1":
        print("result =", add(num1,num2))

    elif choice == "2":
        print("result =", subtract(num1,num2))
    elif choice == "3":
        print("result =", multiply(num1,num2))
    elif choice == "4":
        print("result =", divide(num1,num2))
    else:
        print("Thank you for using calculator!")
        break        