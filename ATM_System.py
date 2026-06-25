# ATM 

# initial Data
pin = "1234"
balance = 5000
mini_statement = []

# Function for checking PIN
def authenticate():
    entered_pin = input("Enter your Pin: ")
    if entered_pin == pin:
        print("Login Sucessfull \n")
        return True
    else:
        print("Incorrect PIN")
        return False



# Main ATM Function
def atm_system():
    global balance, pin, mini_statement
    while True:
        print("\n====================ATM MENU ========================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Exit")
        print("=======================================================")
        choice = input(" Enter Your Choice: ")
        
        if choice == "1":
            print(f"Current Balance: ₹{ balance }")
            mini_statement.append(f"checked Balance: ₹{balance}")
        
        elif choice == "2":
            amount = float(input("enter Deposit Amount: "))
            if amount > 0:
                balance += amount
                print(f" ₹{amount} Deposited Sucessfully")
                print(f"updated Balance : ₹{balance}")
                mini_statement.append(f"Deposited ₹{amount} | Remaining Balance {balance}")
            else:
                print("Invalid amount")
        
        elif choice == "3":
            amount = float(input("enter Withdraw Amount: "))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"₹{amount} WIthdraw Successfully")
                    print(f"Remaining Balance ₹ {balance}")
                    mini_statement.append(f"Withdraw ₹{amount} | Remaining Balance ₹{balance}")
                else:
                    print("Insufficient balance")
            else:
                print("Invalid Amount")
        
        elif choice == "4":
            old_pin = input("Enter Old PIN: ")
            if old_pin == pin:
                new_pin = input("Enter New Pin: ")
                confirm_pin = input("Confirm New Pin: ")
                if new_pin == confirm_pin:
                    pin = new_pin
                    print("PIN changed Successfully")
                    mini_statement.append("PIN Changed")
                else:
                    print(" PIN Mismatch ")
            else: 
                print("Wrong Old Pin Entered")
        
        elif choice == "5":
            print("\n-----------------MINI STATEMENT----------------------")
            if len(mini_statement) == 0:
                print("No Transactions Yet ")
            else:
                for t in mini_statement:
                    print(" ->", t)
        
        elif choice == "6":
            print(" Thank You For Using ATM")
            print("Exiting System...")
            break

        else:
            print("Invalid Choice")



# program start
if authenticate():
    atm_system()
else:
    print(" Access Denied")
