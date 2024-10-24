###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = int(input('enter your pin: '))
while pin == 1111:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check PIN")
    print("6. Change PIN")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        print("Your PIN number is: 1111")
    elif choice == '6':
        new_PIN = int(input('Enter your new PIN number: '))
    else:
        print("Invalid option. Please try again.")
