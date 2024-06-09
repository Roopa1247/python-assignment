"""
WAP to assign 75 and 3.14 values to the variable and constant.
Check the values and type of those after the assignment.
"""
import sys

a=75
NUM=3.14
print(a,type(a))
print(NUM,type(NUM))



'''
WAP to define one complex number with lower case 'j' and
another one with the upper case 'J'.
Check the values and type of the variables after the assignment.
'''
a=7+3j
b=5+8J
print(a,type(a))
print(b,type(b))
'''
WAP to assign 99 digits integer number to a variable.
Check the value, size and type of the variable after the assignment.
'''
num=98765432234567899898765432198765432198765432123456789098765422345678905432123456789098769876543234567753234565423456789532345678754345678764
print(num)
print(sys.getsizeof(num))
print(type(num))