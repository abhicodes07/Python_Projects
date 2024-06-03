# Demonstrating table with for loop

from time import sleep

num = int(input("Enter the number: "))

for i in range(1, 11):
    print("{} * {} = {}".format(num, i, num*i))
    sleep(1)

