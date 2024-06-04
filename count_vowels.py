# Demonstrating program of finding vowels in string
import string
str1 = input("Enter the string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in range(0, len(str1)):
    for j in range(0, len(vowels)):
        if str1[i] == vowels[j]:
            count += 1

print(count)




