def ispalindrom(string):
    reversed_string = string[::-1]
    return string == reversed_string
print(ispalindrom('laal'))
print(ispalindrom('lbll'))