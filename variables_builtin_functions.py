# Day 2: Variables in Python

# 'Day 2: 30 Days of python programming' or:
print('Day 2: 30 Days of python programming')


first_name = 'Patrick'
last_name = 'Lehner'
country = 'Deutschland'
city = 'Dorfen'
age = 30
is_married = False
skills = ['R', 'Python', 'Excel']
person_info = {
    'firstname':'Patrick',
    'lastname':'Lehner',
    'country':'Deutschland',
    'city':'Dorfen',
    'number':13
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', person_info)


# Declaring Multiple Variables in a Line:

first_name, last_name, country, age, is_married = 'Patrick', 'Lehner', 'Deutschland', 30, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age', age)
print('Married:', is_married)


# input()-built-in function:

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
print(person_info)


# Different python data types
# Let's declare variables with various data types

print(type('Patrick'))
print(type(first_name))
print(type(10))
print(type(3.14))
print(type(1 + 1j))
print(type(False))
print(type([1, 2, 3, 4]))
print(type(person_info))
print(type((1, 2)))
print(type(zip([1,2], [3,4])))


# Casting: Converting one data type to another data type.

# integer to float
num_int = 10
print('Num_Int:', num_int)
num_float = float(num_int)
print('Num_Float:', num_float)

# float to integer (sad example)
gravity = 9.81
print(int(gravity))

# integer to string
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# DIDN'T WORK: string to integer or float
num_str = '10.6'
print(num_str)
print('num_int:', int(num_str))
print('num_float:', float(num_str))

# str to list
first_name = 'Patrick'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)


# Exercises - Day 2

# Level 1:

# 1.: done
# 2.: see start
# 3.:
first_name_exerc1 = 'Lara'
print(first_name_exerc1)

# 4.:
last_name_exerc1 = 'Gibbs'
print(last_name_exerc1)

# 5.:
full_name_exerc1 = 'Lara Gibbs'
print(full_name_exerc1)

# 6.:
country_exerc1 = 'Puerto Rico'
print(country_exerc1)

# 7.:
city_exerc1 = 'San Juan'
print(city_exerc1)

# 8.:
age_exerc1 = 27
print(age_exerc1)

# 9.:
year_exerc1 = 2024
print(year_exerc1)

# 10.:
is_married_exerc1 = False
print(is_married_exerc1)

# 11.:
is_true = True
print(is_true)

# 12.:
is_light_on = True
print(is_light_on)

# 13.:
is_fun, studied, interest = True, 'Psycology', 'Rugby'
print(is_fun, studied, interest)


# Level 2:

# 1.:
print(type(is_fun))
print(type(full_name_exerc1))
print(type(city_exerc1))
print(type(year_exerc1))
print(type(studied))
print(type(interest))

# 2.:
print(first_name, len(first_name))

# 3.:
print(first_name, last_name, len(first_name), len(last_name), len(first_name) > len(last_name))

# 4.:
num_one, num_two = 5, 4
print(num_one, num_two)
# i.:
num_add = num_one + num_two
print(num_add)
# ii.:
num_diff = num_one - num_two
print(num_diff)
# iii.:
num_prod = num_one * num_two
print(num_prod)
# iv.:
num_div = num_one / num_two
print(num_div)
# v.:
num_remain = num_one % num_two
print(num_remain)
# vi.:
num_exp = num_one ** num_two
print(num_exp)
# vii.:
floor_division = num_one // num_two
print(floor_division)

# 5.:
# rad_circle = 30 m
# i.:
import math
circle_area = 30**2 * 3.1415
print(circle_area)
# ii.:
circle_circum = 2*30 * 3.1415
print(circle_circum)
# iii.:
circle_rad = float(input('Radius of circle: 30'))
circle_area_v2 = math.pi * circle_rad**2
print(circle_area_v2)

# 6. Input Exercises: 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "Invalid operation"

print("The result is:", result)


first_name_input_exerc = input('Your first name: ')
print("Hello, " + first_name_input_exerc + "!")
last_name_input_exerc = input('Your last name: ')
print("Hello, " + last_name_input_exerc + "!")
country_input_exerc = input('You reside in: ')
print("I'm from " + country_input_exerc + ".")
age_input_exerc = input('Your age: ')
print("I'm currently " + age_input_exerc + ".")

# Again the calculator:

num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second numer: '))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "/":
    result = num_1 / num_2
else:
    result = "Invalid Operation"

print("The result is:", result)


# 7.:
# cmd and space -> terminal -> python3 ->
# -> help('input')

