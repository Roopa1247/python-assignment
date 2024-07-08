
# Assignment-1: if condition
------------------------------

# Check if a person is eligible to vote based on their age

# Input: Age of the person

# Check if the person is eligible to vote

age=int(input("enter a Age of the person: "))
if age>=18:
    print("The person is eligible for vote")
#print("The person is Not eligible for vote")
    


# Assignment-2: if else condition
----------------------------------

# WAP that checks whether a number is positive or negative
num=int(input("enter a Number: "))
if num>=0:
    print("the number is positive")
else:
    print("the number is negative")

    

# Assignment-3: if else condition
-----------------------------------------

# WAP that Checks if a given number is even or odd
num=int(input("enter a Number: "))
if num%2==0:
    print("the given number is even")
else:
    print("the given number is odd")


# Assignment-4: nested if condition
-----------------------------------

# WAP to find the greatest of 3 numbers
num1=int(input("enter a Num1: "))
num2=int(input("enter a Num2: "))
num3=int(input("enter a Num3: "))
if num1>num2:
    if num1>num3:
        print("num1 is greater")
if num2>num1:
    if num2>num3:
        print("num2 is greater")
if num3>num2:
    if num3>num1:
        print("num3 is greater")



# Assignment-5: nested if else condition
---------------------------------------------

num1=int(input("enter a Num1: "))
num2=int(input("enter a Num2: "))
num3=int(input("enter a Num3: "))
if num1>num2:
    if num1>num3:
        print("num1 is greater")
    else:
        print("num3 is greater")
else:
    if num2>num3:
        print("num2 is greater")
    else:
        print("num3 is greater")
"""

Movie Ticket Pricing


Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""
"""Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""
time=int(input("enter a time"))
person_age=int(input("enter a age"))
price=10
if person_age<=12 or person_age>=65:
    print(f"the price is {price*(1-0.5)}")
else:
    if time<17:
        print(f"the ticket price before 5pm is {price*(1-0.25)}")
    else:
        print(f"the ticket price is {price}")
        


# Assignment-6: nested if else condition
-----------------------------------------

# WAP to find the biggest country among 3 based on the population
country_1=int(input("enter a country_1 population: "))
country_2=int(input("enter a country_2 population: "))
country_3=int(input("enter a country_3 population: "))
if country_1>country_2:
    if country_1>country_3:
        print("country_1 population is more")
    else:
        print("country_3 population is more")
else:
    if country_2>country_3:
        print("country_2 population is more")
    else:
        print("country_3 population is more")
    











