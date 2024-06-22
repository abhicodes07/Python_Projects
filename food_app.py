# This is a program or a project for a food app in which you can order and make payment for food
# It has some cool features like wallet and cash withdrawl
# It starts by asking users for the username and password
# since some users doesn't have an account it will ask them to create one first

# First of all i am creating a function for asking username and password

def log(username, password):
    print("-- 🍀 PLEASE CONFIRM USERNAME AND PASSWORD TO CONTINUE! --🍀")
    user = input("\t\t-> Enter The username: ")
    # print(f"Confirming username: {user}")
    passw = input("\t\t-> Enter the password: ")
    # print(f"Confirming password: {passw}")

    if user == username and passw == password:
        print(f"\n\t---\t\t🍀 Welcome!, {username} 🍀")
        print(f"\n\t---\t🍀 Please {username}! Choose an option from below ->  🍀")

    while user != username and passw != password:
        print("WRONG USERNAME AND PASSWORD, PLEASE TRY AGAIN!! ")
        print()
        return log(username, password)
         

print("\t\t---\t 🌟 WELCOME TO THE EPHIMORE FOOD ORDERING APP 🌟 \t --")

username = input("\t\t-> Please Set the username: ")
# print(f"Username: {username}")
password = input("\t\t-> Please Set the password: ")
# print(f"Password: {password}")
print()
print()
log(username, password)

        # if user_cnfrm == user_name and pass_cnfrm == user_pass:
        #     print(f"\n\t\t---\t\t🍀 Welcome!, {user_cnfrm} 🍀")
        #     break




