
from time import sleep

# This is program about printing a star pattern using a for loop

# First we need to ask the user how many rows needs to be printed
rows = int(input("Enter the number: "))

for i in range(rows):
    print()
    sleep(0.5)
    for j in range(i+1):
        print('*', end=' ')
        

print()

