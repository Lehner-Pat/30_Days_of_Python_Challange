# Conditionals

# In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. 
# Remember the indentation after the colon.

# if
a = 3
if a > 0:
    print('a is a positive number')


# if - else
a = 3
if a < 0:
    print('a is a negative number')
else:
    print('a is a positive number')


# if - elif - else
a = 0
if a < 0:
    print('a is a negative number')
elif a > 0:
    print('a is a positive number')
else:
    print('a is equal to zero')


# shorter:
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
b = -3
print('b is positive') if b > 0 else print('b is negative')
c = 0
print ('c is an integer and even') if c % 2 == 0 else print('c is sth else')


# Nested Conditions
d = 0
if d > 0:
    if d % 2 == 0:
        print(('d is a positive integer and even'))
    else:
        print('d is a positive number')
elif d == 0:
    print('d is zero')
else:
    print('d is a negative number')
# d is zero


# AND-operator to avoid nesting
d = 0
if d > 0 and d % 2 == 0:
    print('d is a positive integer and even')
elif d > 0 and d % 2 != 0:
    print('d is a positive integer')
elif d == 0:
    print('d is equal to zero')
else:
    print('d is a negative number')


# OR-operator
user = 'Pamtso'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted.')
else:
    print('Access denied.')


# Exercises: Day 9

# Exercises: Level 1


# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.


# Run input scripts in interactive window

age_learner = int(input("Enter your age: "))
years_to_wait = 18 - age_learner
if age_learner >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {years_to_wait} more years to learn to drive.")


# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
# Output:
# Enter your age: 30
# You are 5 years older than me.

my_age = int(input("Enter your age: "))
your_age = int(input("Enter your age: "))
age_difference = my_age - your_age

if age_difference == 0:
    print(f"We are of the same age.")
elif abs(age_difference) == 1:
    print(f"We are {abs(age_difference)} year apart.")
else: 
    print(f"We are {abs(age_difference)} years apart.")




# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

number_a = int(input("Enter a number: "))
number_b = int(input("Enter a number: "))
if number_a > number_b:
    print("a is greater than b")
elif number_a < number_b:
    print("b is greater than a")
else:
    print("The two numbers are equal.")



# Nested approach:
number_a = int(input("Enter a number: "))
number_b = int(input("Enter a number: "))

if number_a > number_b:
    print("a is greater than b")
else:
    if number_a < number_b:
        print("b is greater than a")
    else:
        print("The two numbers are equal.")



# Exercise: Level 2

# 1. Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-79, B
# 60-69, C
# 50-59, D
# 0-49, F

import random

test_score = int(input("What is the test score? "))

if test_score < 0 or test_score > 100:
    test_score = random.randint(0, 100)
    print(f"Invalid score. A random score of {test_score} will be used.")

if test_score >= 80 and test_score <= 100:
    print(("Your grade is A"))
elif test_score >= 70 and test_score < 80:
    print(("Your grade is B"))
elif test_score >= 60 and test_score < 70:
    print(("Your grade is C"))
elif test_score >= 50 and test_score < 60:
    print(("Your grade is D"))
else:
    print(("Your grade is F"))

# Edel.



# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
all_months = Spring + Summer + Autumn + Winter
print(all_months)

chosen_month = input("Choose a month: ")
if chosen_month in Spring:
    print(f"{chosen_month} is in Spring.")
elif chosen_month in Summer:
    print(f"{chosen_month} is in Summer.")
elif chosen_month in Autumn:
    print(f"{chosen_month} is in Autumn.")
else:
    print(f"{chosen_month} is in Winter.")

# Top.


# 3. The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['Banana', 'Orange', 'Mango', 'Lemon']
chosen_fruit = input("Name a fruit: ")
if chosen_fruit in fruits:
    print(f"'{chosen_fruit}' already is in 'Fruits'")
else:
    fruits.append(chosen_fruit) 

print(fruits)


# Exercises: Level 3

# 1. Here we have a person dictionary. Feel free to modify it!


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


# 1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# 2. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# 3. If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, # Python, MongoDB, print('He is a backend developer'), 
# 4. If the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
# 5. - for more accurate results more conditions can be nested!
# 6. If the person is married and if he lives in Finland, print the information in the following format:

# Asabeneh Yetayeh lives in Finland. He is married.

# 1. 
print(len(person['skills']))
if 'skills' in person:
    print(person['skills'][2])
# Node


# 2. 
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python')
    else:
        print("Python not in skills")
else:
    print("Skills key not in person.")


# 3. 
if 'JavaScript' and 'React' in person['skills']:
    print("He is a front end developer.")
if 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print("He is a back end developer.")
if 'React' and 'Node' and 'MongoDB' in person['skills']:
    print("He is a fullstack developer")
else:
    print("unkown title")


# 4. 
if 'is_married' in person and person['is_married'] == True:
    if 'country' in person and person['country'] == 'Finland':
        print("Asabeneh Yetayeh lives in Finland. He is married.")



