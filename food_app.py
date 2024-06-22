# This is a program or a project for a food app in which you can order and make payment for food
# It has some cool features like wallet and cash withdrawl
# It starts by asking users for the username and password
# since some users doesn't have an account it will ask them to create one first

# First of all i am creating a function for asking username and password

def log(username, password):
    user = input("\t\t-> Enter The username: ").lower
    passw = input("\t\t-> Enter the password: ") .lower

    while user != username and passw != password:
        if user != username:
            print("Wrong Username, Please Enter The Correct Username!")
        elif passw != password:
            print("Wrong password, Please enter correct password!")
        else: 
            print("WRONG USERNAME AND PASSWORD, PLEASE TRY AGAIN!! ")
            # log(user_name, user_pass)
        return log(username, password)

        print()

print("\t\t---\t 🌟 WELCOME TO THE EPHIMORE FOOD ORDERING APP 🌟 \t --")

username = input("\t\t-> Please Set the username: ").lower
password = input("\t\t-> Please Set the password: ").lower

log(username, password)

        # if user_cnfrm == user_name and pass_cnfrm == user_pass:
        #     print(f"\n\t\t---\t\t🍀 Welcome!, {user_cnfrm} 🍀")
        #     break




