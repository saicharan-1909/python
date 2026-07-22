#1 print("Hello, World!")

#2 print("Name: SaiCharan")
# print("Age: 19")

#3 a = int(input("enter first number:"))
# b = int(input("enter the second number:"))
# sum = a + b
# print("sum =", sum)

#4 length = float(input("enter the length:"))
# width = float(input("enter the width:"))
# area = length * width
# print("area of the rectangle is:", area)

#5 a = int(input("enter a number:"))
# b = int(input("enter second number:"))
# a,b = b,a
# print("ater swaping")
# print("first number is:",a) 
# print("second number is:",b)

#6 celsius = float(input("enter temperature in celsius:"))
# fahrenheit = (celsius * 9/5) + 32
# print("temperature in fahrenheit:",fahrenheit)

#7 num = int(input("Enter a num:"))
# square = num ** 2
# cube = num ** 3
# print("square=",square)
# print("cube=",cube)

#8 principal = int(input("Enter the principal amount:"))
# rate = int(input("Enter the rate of intrest:"))
# time = int(input("Enter the time (years):"))
# simple_intrest = principal * rate * time
# print("simple intrest =:",simple_intrest)

#9 num = int(input("Enter a number:"))
# if num % 2 == 0:
#  print("The num is even")
# else:
#  print("The number is odd")

#10 mini project "number guessing game"
import random
secret_number = random.randint(1,100)
attempts = 0
print("Wellcome to the number guessing game")
print("I am thinking a number between 1 to 100")

while True:
    guess = int(input("Enter your guess:"))
    attempts += 1


    if guess == secret_number:
      print("congratulations! you guess correct!")
      print(f"you took {attempts} attempts")
      break
    elif guess > secret_number:
      print("Too High! try again!")
    else :
      print("Too Low! try again!")