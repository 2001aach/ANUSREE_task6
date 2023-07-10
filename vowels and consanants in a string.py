# Program to count the total no.of vowels and constant in a string


string=input("enter word")
vowels=["a","e","i","o","u"]
count = 0
for i in vowels:
    count=count+string.count(i)
print(count)