"""
operands
'+' --> add/concatenate
'-' --> sub/remove
'*' --> multiply
'**' --> raise to the power of
'==' --> comparison
'!' --> not equal to
'and' --> will return false when any of them is false
'or' --> will return true when any of them is true
"""

# add
num1 = input("first: ")
num2 = input("second: ")

add = int(num1) + int(num2)
print(add)

# subtract
num1 = input("first: ")
num2 = input("second: ")

sub = int(num1) - int(num2)
print(sub)

# multiply
num1 = input("first: ")
num2 = input("second: ")

mul = int(num1) * int(num2)
print(mul)

# division
num1 = input("first: ")
num2 = input("second: ")

div = int(num1) / int(num2)
print(div)

"""conversion of data types

strings"""

no = 1
str(no)  # converts the value of "no" to string

yes = 2
int(yes)  # converts the value of "yes" to string
