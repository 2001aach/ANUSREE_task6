# Program to sort the element of an array in descending order

arr = [ '5', '6', '7', '4', '8']


for i in range(0, len(arr)) :
	arr[i] = int(arr[i])
arr.sort(reverse = True)
print (str(arr))
