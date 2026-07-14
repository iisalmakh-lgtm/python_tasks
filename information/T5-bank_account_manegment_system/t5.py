users = {}
current_user = None
def register() :
    username=input("Enter username : ").strip()
    password=input("Enter Your Password Of 6 characters :").strip()

    if not username:
        print("Username cannot be empty.") 
        return   
    if not password:
        print("Password cannot be empty.")
        return      
    if username in users:
        print("Username already exists. Please choose a different username.")
        return    
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return
    
     
    users[username] = {
    "password": password,
    "balance": 0
}
    print("Registration successful! You can now log in.")
    

def login():
    username=input("Enter username : ").strip()
    password=input("Enter Your Password : ").strip()

    if username not in users :
        print("Username does not exist. Please register first.")
        return
    
        
    if users[username]["password"] != password:
        print("Incorrect password. Please try again.")
        return
    
    global current_user
    current_user = username
    
    print(f"Welcome {username}")
    print(f"Current Balance: {users[current_user]['balance']} EGP")
    bank_menu()

def bank_menu():
    while True:
        print("========== Bank Menu ==========")
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Change Password\n6. Logout")
        choice=int(input("Enter Your Choise As A Number :"))
        if choice == 1 :
            check_balance()
        elif choice == 2 :
            deposit()       
        elif choice == 3 :
            withdraw()
        elif choice == 4 :
            transfer()
        elif choice == 5 :
            change_password()
        elif choice == 6 :
            return
        else :
            print("Invalid Choise")
    

def check_balance():
    if current_user:
        balance = users[current_user]["balance"]
        print(f"Current Balance: {balance} EGP")
    else:
        print("No user is currently logged in.")
    
    

def deposit():
    amount=float(input(" Enter Amount : "))
    if amount <= 0 :
        print(" invalid amount ")
        return
    else:
        users[current_user]["balance"]+=amount
        print(f"Your Balance Become {users[current_user]['balance']} EGP")


def withdraw():
    amount=float(input(" Enter Amount : "))
    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > users[current_user]["balance"]:
        print("Insufficient balance.")
        return
    
    users[current_user]["balance"]-=amount
    print(f"Your Balance Become {users[current_user]['balance']} EGP")

def transfer():
    reci_username =input(" Enter The recipient's Username : ")
    amount=float(input(" Enter Amount : "))
    if reci_username not in users :
        print("  The other user must exist. ")
        return
    if reci_username == current_user :
        print(" A transfer to the same account is not allowed. ")
        return
    if amount <= 0:
        print("Invalid amount")
        return
    if amount > users[current_user]["balance"]:
        print("Insufficient balance")
        return
            
    users[current_user]["balance"]-=amount
    users[reci_username]["balance"]+=amount
    print("Transfer completed successfully!")
    print(f"User New Balance = {users[current_user]['balance']} EGP")
    print(f"recipient User New Balance = {users[reci_username]['balance']} EGP")

def change_password():
    current_password = input(" Enter Your Password : ")
    new_password = input(" Enter Your New Password : ")
    if current_password != users[current_user]["password"] :
        print(" Sorry Your Password Is Incorrect ! ")
        return
    if len(new_password) < 6 :
        print(" Your Password Must Be Contained With 6-Charcater Or More ")
        return
    users[current_user]["password"]=new_password
    print(" Password changed successfully! ")
    

def main():
    while True :

        print("========== Welcome To Python Bank ==========")
        print("1. Register\n2. Login\n3. Exit")

        choice=int(input("Enter Your Choise As A Number :"))
        if choice == 1 :
            
            register()
        elif choice == 2 :
            login()
                    
        elif choice == 3 :
            break
        else :
            print("Invalid Choise")



main()





















