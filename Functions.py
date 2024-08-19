# Day 11: Functions
# A function is a reusable block of code or programming statements designed to perform a certain task.

def add_two_numbers ():
    num_one = 3
    num_two = 5
    total = num_one + num_two
    print(total)
add_two_numbers()

# Function Returning a Value - Part 1

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())


# Function with Parameters

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Patrick'))


def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))


def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area
print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range (n+1):
        total += i
    print(total)
print(sum_of_numbers(10))
print(sum_of_numbers(100))


def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers:', sum_two_numbers(11, 24))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('The age is:', calculate_age(2024, 1993))


def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + 'N'
    return weight
print('The weight of the object in Newtons is:', weight_of_object(100, 9.81))


def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Hosen', lastname = 'Berger'))


# Function Returning a Value - Part 2
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False
print(is_even(10)) 
print(is_even(9))


def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(20))
results_even_numbers = find_even_numbers(20)
print(results_even_numbers)


# Function with Default Parameters:
def greetings(name = 'Peter'):
    message = name + ', welcome to Python!'
    return message
print(greetings())
print(greetings('Pamtrix'))


def generate_fullname(first_name = 'Pamtrix', last_name = 'Lehmertz'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Welcome,', generate_fullname(), '.')
print('Welcome,', generate_fullname('John', 'Smith'), '.')


# Arbitrary Number of Arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2, 3, 5, 8))


# Function as a Parameter of Another Function
def square_number(n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))



# Exercises: Day 11

# Exercises: Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_1, num_2):
    sum = num_1 + num_2
    return sum
print(add_two_numbers(23, 34))


# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.1415
    area = pi * r ** 2
    return area
print('The area of the circle in square meters is:', area_of_circle(100))


# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(add_all_numbers(1, 2, 3, 4, 5, 6))


# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celcius_to_fahrenheit(C):
    temp_in_fahrenheit = (C * 9/5) + 32
    return temp_in_fahrenheit
print(convert_celcius_to_fahrenheit(40))


# 5. Write a function called check_season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['March', 'April', 'May']:
        print('Spring')
    elif month in ['June', 'July', 'August']:
        print('Summer')
    elif month in ['September', 'October', 'November']:
        print('Autumn')
    else:
        return 'Winter'
print(check_season('July'))
print(check_season('February'))


# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(m):
    return m
print("A linear function's slope (y=mx+t) is its m value:", calculate_slope(3))

# or
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("The x-values are the same; the line is vertical and slope is undefined.")
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(1, 3, 5, 8))


# 7. Quadratic equations are calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates a solution set of a quadratic equation, solve_quadratic_eqn.
import math
def solve_quadratic_eqn(a, b, c):
    discriminant = ((b ** 2) - (4 * a * c))
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return(root,)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, imaginary_part)
        return(root1, root2)
print(solve_quadratic_eqn(3, 9, 6))


# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for element in list:
        print(element)
my_list = [1, 2, 3, 4, 5]
print(print_list(my_list))

# extra exerc
def squaring(number):
    result = number ** 2
    return result
print(squaring(4))
# extra exerc
def squaring_list(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares
print(squaring_list([1, 2, 3, 4]))

# extra exerc 
# Here's a function that checks if numbers in a list are even and returns a new list of even numbers:
def filter_even_numbers(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens
print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# extra exerc
# Write a function that takes a list of integers and returns a list of integers that are divisible by a given divisor.
def divisible_by(numbers, divisor):
    # initialise an empty list to store the results
    result = []
    # Loop through each number in the provided list
    for number in numbers:
        # Check if the current number is divisible by the divisor
        if number % divisor == 0:
            # If it is, append the number to the result list
            result.append(number)
    # Return the list of numbers that are divisible by the divisor
    return result
print(divisible_by([1, 2, 3, 4, 5, 6, 7, 8], 2))


# 9. Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_list = []
    for i in range(len(arr) -1, -1, -1):
        reversed_list.append(arr[i])
    return reversed_list
print(reverse_list([12, 13, 15, 16]))
# repeat:
def reverse_list(arr):
    reversed_list = []
    for i in range(len(arr)-1, -1, -1):
        reversed_list.append(arr[i])
    return reversed_list
print(reverse_list([1, 2, 3, 4]))


# 10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalise_list_items(arr):
    post_capitalisation = []
    for item in arr:
        post_capitalisation.append(item.capitalize())
    return post_capitalisation
print(capitalise_list_items(['car', 'hat', 'boy']))


# 11. Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(arr, item):
    arr.append(item)
    return arr
print(add_item([], 'hat'))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))


# 12. Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.
def remove_item(arr, item):
    arr.remove(item)
    return arr
print(remove_item(food_staff, 'Meat'))
# noice


# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    total_sum = 0
    for i in range(0, num):
        total_sum += i
    return total_sum
print(sum_of_numbers(5))


# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    total_sum = 0
    for i in range(1, num, 2):
        total_sum += i
    return total_sum
print(sum_of_odds(8))
# lit


# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    total_sum = 0
    for i in range(0, num, 2):
        total_sum += i
    return total_sum
print(sum_of_even(7))


# Exercises: Level 2

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    nr_evens = 0
    nr_odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            nr_evens += 1
        else:
            nr_odds += 1
    return nr_evens, nr_odds
print("Amount of evens and odds in input number:", evens_and_odds(100))


# 2. Call your function factorial, it takes a whole number as a parameter and it returns a factorial of the number
def factorial(num):
    all_i_multipl = 1
    for i in range(1, num + 1):
        all_i_multipl *= i
    return all_i_multipl
print(factorial(4))


# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not

# nice clarity:

def is_empty(arr):
    if arr == []:
        print('Array is empty.')
    else:
        print('Array is full.')
print(is_empty([]))        # Output: Array is empty.
print(is_empty([2, 7]))    # Output: Array is full.

# improved functionality:

def is_empty(arr):
    if not arr:
        return True
    else:
        return False
print(is_empty([]))       # Output: True
print(is_empty([2, 3]))   # Output: False  

# combined for optimal use:

def is_empty(arr):
    if not arr:
        print('Array is empty.')
        return True
    else:
        print('Array is full.')
        return False

# Testing the function
print(is_empty([]))       
# Output: Array is empty.
#         True
print(is_empty([2, 3]))   
# Output: Array is full.
#         False


# 4. Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# calculate_mean:
def calculate_mean(lst):
    numerator = sum(lst)
    denominator = len(lst)
    mean = numerator / denominator
    return mean
print(calculate_mean([2, 3, 4]))
print("The arithmetic mean of this list is: ", calculate_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]))
# Sauber Pate


# calculate_median:
def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    middle_value = n // 2
    if n % 2 == 1:
        return sorted_lst[middle_value]
    else:
        return (sorted_lst[middle_value - 1] + sorted_lst[middle_value]) / 2

print(calculate_median([2, 3, 4, 5, 6, 7, 8]))
print(calculate_median([2, 3, 4, 5, 6, 7, 8, 9]))
print(calculate_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]))


# calculate_mode:
def calculate_mode(lst):
    most_common_value = max(lst, key=lst.count)

    return most_common_value
print(calculate_mode([1, 2, 3, 4, 4, 4, 5, 6, 7]))


# calculate_range:
def calculate_range(lst):
    first_value = min(lst)
    last_value = max(lst)
    return last_value - first_value
print(calculate_range([1, 2, 3, 4, 5, 6, 7, 8, 19]))


# calculate_variance:
import statistics
def calculate_variance(lst):
    mean_value = statistics.mean(lst)
    variance = sum((i - statistics.mean(lst)) ** 2 for i in lst) / len(lst)
    return variance
print(calculate_variance([1, 5, 6, 7]))

statistics.mean([1, 5, 6, 7]) # sum of the squared differences of the list items minus the arithmetic mean. 4.75

def calculate_variance(lst):
    mean_value = statistics.mean(lst)
    variance = sum((i - statistics.mean(lst)) ** 2 for i in lst) / len(lst)
    return variance
print(calculate_variance([1, 10, 100])) # 1998


# calculate_std:
import math
def calculate_std(lst):
    variance = statistics.variance(lst)
    stand_dev = math.sqrt(variance)
    return stand_dev
print(calculate_std([1, 5, 6, 7])) 
# standard deviation derived from sample variance, hence 1/(n-1) * sum of the squared differences of the list items minus the arithmetic mean
# I.e. not 20.75 / 4, but 20.75 / (4-1) -> sqrt(ans)


# Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        print(f"{num} is not a prime number.")
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return False

    else:
        print(f"{num} is a prime number.")
        return True

print(is_prime(15))
print(is_prime(17))


# 2. Write a functions which checks if all items are unique in the list.
def list_is_set(lst):
    if len(lst) == len(set(lst)):
        print("The list items are unique.")
        return True
    else:
        return False
        print("The list items appear more than once.")
print(list_is_set([2, 4, 6, 8]))


# 3. Write a function which checks if all the items of the list are of the same data type.
def is_same_type(lst):    
    first_type = type(lst[0])

    for item in lst:
        if type(item) != first_type:
            print("The list items are not of the same data type.")
            return False
         
    print("The list items are all of the same type.")
    return True

print(is_same_type([2, 4, 6]))


# 4. Write a function which checks if provided variable is a valid python variable
def is_valid_pyth_var(var):


def sum_all_nums(*numbs):
    total = 0
    for num in numbs:
        total += num
    return total
print(sum_all_nums(3, 5))














