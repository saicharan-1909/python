# class Car:

#     def __init__(self, brand, model):
#        self.brand = brand
#        self.model = model

# car1 = Car("toyota", "fortuner")
# print(car1.brand)
# print(car1.model)


# class Laptop:

#     def __init__(self, brand , ram):
#        self.brand = brand
#        self.ram = ram

# Laptop1 = Laptop("HP", 8)
# Laptop2 = Laptop("Dell", 12)
# print(Laptop1.brand , Laptop1.ram)
# print(Laptop2.brand , Laptop2.ram)


# class Student:


#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"name: {self.name}, age: {self.age} years old"

# student1 = Student("Sai", 19)
# student2 = Student("Vamshi", 20)
# student3 = Student("Shekar", 25)

# print(student1)
# print(student2)
# print(student3)





class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance



    def deposit(self, amount):
        self.balance += amount 
        print(f"${amount} deposited succesfully.")


    def withdraw(self, amount):

       if amount <=  self.balance:
        self.balance -= amount
        print(f"${amount} withdrawn succesfully.")
       else:
        print("insufficient balance!")


    def check_balance(self):
        print(f"Account holder: {self.name}")
        print(f"current balance: ${self.balance}")

name = input("Enter account holder name:")
balance = float(input("Enter initial balance:"))
account = BankAccount(name, balance)

while True:
    print("\n========BankAccount========")
    print(f"\n Welcome, {account.name}!")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice:")

    if choice == "1":
        amount = float(input("Enter amount to Deposit:"))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to Withdraw:"))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank for using bank account simulator!")
        print(account.name)
        break

    else:
        print("Invalid choice! please enter a number from 1 to 4")