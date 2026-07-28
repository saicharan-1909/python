# file = open("message.txt", "w")
# file.write("Hello, Python!")
# file.close()


# file = open("message.txt", "r")
# print(file.read())
# file.close()


# with open("message.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("notes.txt", "w") as file:
#     file.write("python\nmachine learning\nAI ")
# print("data written succesfully!")

# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)



# with open("languages.txt", "w") as file:
#     file.write("python")
#     file.write("\nC++")
#     file.write("\njava")
#     file.write("\njavascript")

# with open("languages.txt", "r") as file:
#     content = file.read()
#     print(content)



# try:
#     number = int(input("Enter a number:"))
#     print("cube = ", number **3)
# except ValueError:
#     print("please, Enter a valid number!")  


# try:
#     age = int(input("Enter your age:"))
# except ValueError:
#     print("please enter a valid age.")
# else:
#     print("you are", age, "years old.")
# finally:
#     print("Thank you for using this program!")



while True:
    print("\n========Expense Tracker========")
    print("1. Add expense")
    print("2. view expense")
    print("3. Exit")

    choice = (input("Enter your choice:"))

    if choice == "3":
        print("Thank you for using expense tracker!")
        break

    elif choice == "1":
          category = input("Enter your category:")
          try:
             amount = float(input("Enter amount:"))
    
             with open("day5/expenses.txt", "a") as file:
                file.write(f"{category} - {amount}\n")

             print("Expense added successfully!")
          except ValueError:
            print("Please Enter a Valid Amount.")

    elif choice == "2":
        try:
            with open("day5/expenses.txt", "r") as file:
                print("\n=======expenses=======")
                total = 0
                for line in file:
                    print(line.strip())

                    category, amount = line.strip().split("-")
                    amount = float(amount)
                    total += amount
                    print(f"\nTotal Expenses: ${total}")
        except FileNotFoundError:
            print("No Expenses Found Yet!")
    
