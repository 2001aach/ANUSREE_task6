# Program to find the total number of characters in the a string

string =input('enter the word')
count = 0

for i in range(0, len(string)):
    if (string[i]!= ' '):
        count = count + 1

print("Total no.of characters:" + str(count))