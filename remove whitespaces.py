# Program to remove all the white spaces of from string

def remove(string):
    return "".join(string.split())

string = 'remove white spa ce '
print(remove(string))
