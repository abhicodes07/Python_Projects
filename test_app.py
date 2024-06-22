user = input("Enter the username: ").lower
passw = input("Enter the username: ").lower


print(user)
print(passw)

username = input("Enter the username again: ").lower
password = input("Enter the password again: ").lower
print(username)
print(password)

while username != user and password != passw:
    username = input("Enter the correrct username: ")
    password = input("Enter the correct password: ")


