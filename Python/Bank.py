FILE="bankDetail.txt"

def Update(name, passw, balance):
    with open(FILE,'r') as file:
        lines=file.readlines()

    with open(FILE, 'w') as file:
        for line in lines:
            n, p, b = line.strip().split(',')
            if n.lower() == name.lower() and p == passw:
                file.write(f"{n},{p},{balance}\n")
                updated = True
            else:
                file.write(line)
    
    if updated:
        print("Account balance updated successfully.")
    else:
        print("Account not found or incorrect password.")

def deposit(name, pword, balance):
    depositAmt=input("Enter the amount you want to deposit: $")
    while True:
        if depositAmt.isdigit():
            break
        else:
            print("Please enter a valid number")
    depositAmt=int(depositAmt)
    balance=int(balance)
    balance+=depositAmt
    Update(name, pword, balance)
    print(f"Your current balance is ${balance}")
    homePage(name, pword, balance)
    return balance

def withdraw(name, pword, balance):
    withdrawAmt=input("Enter the amount you want to withdraw: $")
    while True:
        if withdrawAmt.isdigit():
            break
        else:
            print("Please enter a valid number")
    withdrawAmt=int(withdrawAmt)
    balance=int(balance)
    balance-=withdrawAmt
    Update(name, pword, balance)
    print(f"Your current balance is ${balance}")
    homePage(name, pword, balance)
    return balance

def checkBalance(n, p, b):
    print(f"your current balance is ${b}")
    homePage(n,p,b)

def accountRegister():
    fname=input("Enter your first name: ")
    password=input("Enter Your password: ")
    balance=0
    with open(FILE,'a') as file:
        file.write(f"{fname},{password},{balance}\n")
    print("Account successfully registered.")
    main()

def homePage(n,p,b):
    print("1. Deposit\n2. Withdraw\n3. Check Balance` ")
    choice=input("Enter your choice: ")
    while True:
        if choice=="1":
            b=deposit(n,p,b)
            break
        elif choice=="2":
            b=withdraw(n,p,b)
            break
        elif choice=="3":
            checkBalance(n, p, b)
            break
        else:
            print("Please enter a valid choice")


def accountLogin():
    fname=input("Enter your first name: ")
    password=input("Enter your password: ")
    stat=""
    with open(FILE,'r') as file:
        for line in file:
            n,p,b = line.strip().split(',')
            if n.lower() == fname.lower() and password == p:
                stat="Found"
                break
        if stat!="Found":
            print("Account not found. Please press enter to create an account")
            accountRegister()
        else:
            print(f"Login Successful.")
            homePage(n,p,b)
        

def main():
    print("Welcome to Bank!!")
    print("Enter S.No. to for following actions:")
    print("1. Account Register\n2. Account Login")
    action=input("choose an option: ")
    while True:
        if action=="1":
            accountRegister()
            break
        elif action=="2":
            accountLogin()
            break
        else:
            print("Please enter a valid option")
        
main()