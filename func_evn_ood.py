def __evnodd__(num):
    if num < 0:
        print("Entered number is negative.")
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
num = int(input("Enter the number: "))
__evnodd__(num)


