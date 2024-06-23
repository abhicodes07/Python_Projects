"""
This is a program or a project for a food app in which you can order and make payment for food
It has some cool features like wallet and cash withdrawl
It starts by asking users for the username and password
since some users doesn't have an account it will ask them to create one first
"""

# First of all i am creating a function for asking username and password

def log(username, password):
    """
    This function allows the user to create a login username and 
    password if it's incorrect then it asks them to fill in the correct
    username and password.
    """
    user = input("\t-> Enter The username: ")
    # print(f"Confirming username: {user}")
    passw = input("\t-> Enter the password: ")
    # print(f"Confirming password: {passw}")

    if user == username and passw == password:
        print(f"\n\t---\t\t🍀 Welcome!, {username} 🍀")
        print(f"\n\t---\t🍀 {username}! Choose an option from below ->  🍀")
        print()
        options()
    while user != username or passw != password:
        print("-- WRONG USERNAME AND PASSWORD, PLEASE TRY AGAIN!! -- ")
        print()
        
        user = input("\t-> Enter the correct username: ")
        passw = input("\t-> Enter the correct password: ")

    # uncomment if you want to understand the working of the function 
    doc1 = log.__doc__
    # print(doc1)

def wallet():
    balance = 10
    print(f"\t🍀 Your Wallet Balance is: $ {balance}")
    q1 = input("\t🍀 Would ou like to add more money to your wallet: ")
    if q1 == 'yes':
        q2 = int(input("\t🍀 Enter The Amount You Want To Add: "))
        balance += q2
        print(f"\t🍀 Now Your Wallet Balance Is: $ {balance}")
        print("\t 🍀 You Can Make A Choice again. 🍀")
        print()
        options()
    elif q1 == 'no':
        print("\t🍀 Ok No problem!, You May Proceed To Make a Choice Again: ")
        print()
        options()
        
def options():
    print("\t\t🪻 1. Wallet")
    print("\t\t🪻 2. Menu")
    print("\t\t🪻 4. Account")
    print("\t\t🪻 5. Exit")
    
    choice = int(input("🍀 Enter Your Choice: "))
    if choice == 1:
        wallet()

def menu():
    pass

def kill():
    pass

# Main
print("\t\t--- 🌟 WELCOME TO THE EPHIMORE FOOD ORDERING APP 🌟 ---")
print()
print()
# setting up login id
username = input("\t-> Please Set the username: ")
password = input("\t-> Please Set the password: ")
print()
print()

# confirming the username and password from the user
print("-- 🍀 PLEASE CONFIRM USERNAME AND PASSWORD TO CONTINUE! --🍀")
log(username, password)

# making choice out of options





