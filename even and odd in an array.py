# Print even and odd numbers in an array

array = [1,2,3,4,5,6,7,8,9,10]
evennum = []
oddnum = []
for i in range(len(array)):
  if(array[i]%2 == 0):
    evennum.append(array[i])
  else:
    oddnum.append(array[i])
print("Even Numbers:", evennum)
print("Odd Numbers:", oddnum)