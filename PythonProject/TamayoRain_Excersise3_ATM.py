#ATM
print("_____________________________________________")
print("Nice day! Welcome to Rain Bank!")
print("_____________________________________________")

tamayoRain_balance = 0.00

print("Note: remember the PIN you're going to input.")
tamayoRain_pin = input("Please enter a PIN: ")

print("_____________________________________________")
print("ATM account logged out")
print("_____________________________________________")

tamayoRain_attempt = 0

while tamayoRain_attempt < 3:
    tamayoRain_enteredPin = input("Enter your PIN: ")

    if tamayoRain_enteredPin == tamayoRain_pin:
        print("_____________________________________________")
        print("Login successfully!")

        while True:
            print("_____________________________________________")
            print("___________________ATM MENU__________________")

            print("1. Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Log out")

            tamayoRain_choice = input("Please enter the number of your choice: ")

            if tamayoRain_choice == "1":
                print("_____________________________________________")
                print("Your balance is: ", tamayoRain_balance)

            elif tamayoRain_choice == "2":
                tamayoRain_deposit = float(input("Enter the amount you want to deposit: "))
                tamayoRain_balance = tamayoRain_deposit + tamayoRain_balance
                print("Deposit successful. New balance: ", tamayoRain_balance)

            elif tamayoRain_choice == "3":
                tamayoRain_withdraw = float(input("Enter the amount: "))
                if tamayoRain_withdraw <= tamayoRain_balance:
                    tamayoRain_balance = tamayoRain_balance - tamayoRain_withdraw
                    print("Withdrew Successfully! Your balance is now: ", tamayoRain_balance)

                elif tamayoRain_withdraw > tamayoRain_balance:
                    print("Insufficient balance.")

            elif tamayoRain_choice == "4":
                print("Logged out.")
                break

            else:
                print("invalid option")

    else:
        tamayoRain_attempt += 1
        print("Incorrect PIN. Attempts remaining: ", 3 - tamayoRain_attempt)

if tamayoRain_attempt == 3:
    print("Too many attempts. Account locked for 3 days.")