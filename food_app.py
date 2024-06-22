"""This is a program or a project for a food app in which you can order and make payment for food
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
        print(f"\n\t---\t🍀 Please {username}! Choose an option from below ->  🍀")

    while user != username or passw != password:
        print("-- WRONG USERNAME AND PASSWORD, PLEASE TRY AGAIN!! -- ")
        print()
        
        user = input("\t-> Enter the correct username: ")
        passw = input("\t-> Enter the correct password: ")

    # uncomment if you want to understand the working of the function 
    # print(log.__doc__)

# Main
print("\t\t---\t 🌟 WELCOME TO THE EPHIMORE FOOD ORDERING APP 🌟 \t --")

print("-- 🍀 PLEASE CONFIRM USERNAME AND PASSWORD TO CONTINUE! --🍀")

username = input("\t-> Please Set the username: ")
password = input("\t-> Please Set the password: ")
print()
print()
log(username, password)


