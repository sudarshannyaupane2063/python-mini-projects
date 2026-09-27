#To create ATM simulation project

balance = 0
out = 0
pin = 1234
attempts = 5
while True:
    try:
        check = int(input("Enter 4-digit PIN to access ATM: "))
    except ValueError:
        print("PIN must contain numbers.")
        continue
    if check<1000 or check>9999:
        print("PIN must be 4 digits.")
    elif check == pin:
        print("----Welcome to ATM----")
        attempts = 5
    elif attempts>1:
        attempts-=1
        print(f"Incorrect PIN. (You have remaining {attempts} attempts!)")
    else:
        print("Entered incorrect PIN multiple times. Please try again later.")
        break
    while check == pin:
        print("Please enter:")
        print("    '1' for balance check\n    '2' for deposit\n    '3' for withdraw\n    '4' for exit")
        try:
            n = int(input("-> "))
        except ValueError:
            print("Please enter a number.")
            continue

        if n>4 or n<1:
            print("Enter correct number!")

        #Check balance 
        elif n==1:
            print(f"Your account balance is Rs.{balance}")

        #Deposit money
        elif n == 2:
            while True:
                try:
                    d = int(input("Enter amount you want to deposit: "))
                except ValueError:
                    print("Enter amount in number!")
                    continue
                if d<=0:
                    print("Zero and Negative deposit is not possible!")
                    continue
                balance += d
                print(f"You have total Rs.{balance} balance.")
                break

        #Withdraw money
        elif n ==3:
            while True:
                try:
                    w = int(input("Enter amount you want to withdraw: "))
                except ValueError:
                    print("Enter amount in number!")
                    continue
                if w<=0:
                    print("Zero and Negative withdrawal is not possible!")
                    continue
                elif w>balance:
                    print(f"Insufficient balance!! (You have only Rs.{balance} in account.)")
                    break
                else:
                    balance -= w
                    print(f"You have remaining Rs.{balance} balance.")
                    break

        #Exit ATM 
        elif n==4:
            print("Thank you.")
            out = 1
            break

    if out == 1:
        break

