
# This is a program about printing fibonacci numbers of certain length
num = int(input("Enter the last number: "))
print("Here's your first {} fibonacci numbers".format(num))
a = 0
b = 1
print(a)
print(b)
i = 0
while i <= num:
    x = a + b
    a = b
    b = x
    i += 1
    print(x)




