from time import sleep

num = int(input("Enter the number: "))

flag = 1
while flag != 11:
    print("{} * {} = {}".format(num, flag, num*flag))
    flag+=1
    sleep(1)









