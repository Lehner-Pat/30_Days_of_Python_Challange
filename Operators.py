print(True)
print(False)

# There are assignment operators
# We can use the Addition Assignment Operator += and loops to define the fibonacci sequence:

# Number of steps in our Fibonacci series
n_steps = 10

# Initialize the first three numbers in the series
a, b = 0, 1

# Print the first two numbers
print(a)
print(b)

# Generate the Fibonacci series for n_steps
for _ in range(n_steps - 2):  # We already have the first two numbers
    a += b  # This is equivalent to a = a + b
    a, b = b, a  # Swap a and b
    print(b)

print(int(8/2))
print(8/2)

# Floating numbers
print('Floating Point Number, PI:', 3.14)
print('Floating Point Number, gravity:', 9.81)

print('Complex Number:', 1 + 1j)
print('Multiplying Complex Numbers:', (1+1j)**2, (1-1j)**2, (1+1j)*(1-1j))

print('Addition: ', 1 + 2) 
print('Subtraction: ', 3 - 1)
print('Multiplication: ', 2 * 3)  
print ('Division: ', 4 / 2)       # Division in Python gives floating numbers
print('Division: ', 6 / 2)                 
print('Division: ', 7 / 2)        
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3)


# Declaring the variable at the top first

a, b = 3, 2


# Arithmetic operations and assigning the result to a variable

add = a + b
diff = a - b
prod = a * b
div = a / b
remain = a % b
floor_div = a//b
expon = a ** b

# If you do not label your print with some string, you never know where the result is coming from.

print('a + b = ', add)
print('a - b = ', diff)
print('a * b = ', prod)
print('a / b = ', div)
print('a % b = ', remain)
print('a // b = ', floor_div)
print('a ** b = ', expon)


# Calculating area of a circle
import math

radius = 10
area_circle = math.pi * radius ** 2
print('Area of circle:', area_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_rectancle = length * width
print('Area of rectangle:', area_rectancle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight_obj = mass * gravity
print('Weight of object:', weight_obj)

# Calculate the density of a liquid
mass = 75
volume = 0.075
density_liq = mass / volume
print('Density of liquid:', density_liq)


# Comparison Operators

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Is, Is not, In, Not In
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Logical Operators
x = 5
print(x > 3 and x < 7)  # Returns: True
print(x > 3 and x < 5)  # Returns: False
print(x > 3 or x < 7)   # Returns: True
print(x > 3 or x < 5)   # Returns: True
print(x > 6 or x < 4)   # Returns: False


# Exercises Day 3:

# 1. Declare your age as integer variable
my_age = 30
print('My age in 2024:', int(my_age))

# 2. Declare your height as a float variable
my_height = 178
print('My height in cm in 2024:', float(my_height))

# 3. Declare a variable that stores a complex number
num_compl = (1+1j)
print('Complex diagonal:', num_compl)

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# Enter base: 20
# Enter height: 10
# The area of the triangle is 100

base_triangle = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area_triangle = 0.5 * base_triangle * height_triangle
print('The area of the triangle is:', int(area_triangle))

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

a_triangle = float(input("Enter side a: "))
b_triangle = float(input("Enter side b: "))
c_triangle = float(input("Enter side c: "))
perimeter_triangle = a_triangle + b_triangle + c_triangle
print('The perimeter of the triangle is:', perimeter_triangle)

# 6. Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length_rect = float(input("Enter length of rectangle: "))
width_rect = float(input("Enter width of rectangle: "))
exerc_area_rect = length_rect * width_rect
print('The area of the exercise rectangle is:', exerc_area_rect)
exerc_perimeter_rect = 2 * (length_rect + width_rect)
print('The perimeter of the exercise rectangle is:', exerc_perimeter_rect)

# 7. Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math

exerc_radius = float(input("Enter radius of circle: "))
exerc_area_circle = exerc_radius**2 * math.pi
print('The area of the exercise circle is:', exerc_area_circle)
exerc_circumf = exerc_radius*2 * math.pi
print('The circumference of the exercise circle is:', exerc_circumf)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

y = 2*x - 2
slope_exerc_8 = int((2-0) / (1-0))
print('The slope of the function is:', slope_exerc_8)

def calculate_intercepts():
    # Calculate y-intercept (when x = 0)
    x = 0
    y_intercept = 2*x-2
# Calculate x-intercept
    y = 0
    x_intercept = (y+2)/2
    return x_intercept, y_intercept
x_intercept, y_intercept = calculate_intercepts()

print(f"The x-intercept is at x = {x_intercept}")
print(f"The y-intercept is at y = {y_intercept}")

# 9. Find the slope and Euclidean distance between point (2, 2) and point (6,10).
x_1, x_2, y_1, y_2 = 2, 6, 2, 10
import math
# Squareroot of (x_2 - x_1)^2 + (y_2 - y_1)^2 is Eucl_dist
exerc_eucl_dist = math.sqrt((6-2)**2 + (10-2)**2)
print('The Euclidean distance between (2,2) and (6,10) is:', exerc_eucl_dist)
# Slope of a linear function is (y_2 - y_1)/(x_2 - x_1)
slope_exerc_9 = int((y_2 - y_1)/(x_2 - x_1))
print('The slope of the line is:', slope_exerc_9)

# 10. Compare the slopes in tasks 8 and 9.
slope_equality = slope_exerc_8 == slope_exerc_9
print('The slopes of the two exercises are the same:', slope_exerc_8 == slope_exerc_9)

# 11. Calculate the value of y for (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.

import math

def calculate_x_intercepts(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two real roots
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # One real root
        x = -b / (2*a)
        return x,
    else:
        # No real roots
        return None

# Coefficients for the quadratic equation y = x^2 + 6x + 9
a = 1
b = 6
c = 9

# Calculate the x-intercepts
x_intercepts = calculate_x_intercepts(a, b, c)

# Display the results
if x_intercepts:
    if len(x_intercepts) == 1:
        print(f"The quadratic equation has one x-intercept: x = {x_intercepts[0]}")
    else:
        print(f"The quadratic equation has two x-intercepts: x1 = {x_intercepts[0]}, x2 = {x_intercepts[1]}")
else:
    print("The quadratic equation has no real x-intercepts.")


# PLOTTING

import matplotlib.pyplot as plt
import numpy as np

# Define the quadratic function
def quadratic_function(x):
    return x**2 + 6*x + 9

# Generate x values
x_values = np.linspace(-23, 17, 400)  # generates 400 points from -10 to 0

# Calculate y values
y_values = quadratic_function(x_values)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='y = x^2 + 6x + 9')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Graph of the Quadratic Function y = x^2 + 6x + 9')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("Python"))
print(len("Dragon"))
print('The length of "Python" is shorter than of "Dragon":', len("Python"), len("Dragon"))

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'.
str1, str2 = "python", "dragon"
result = "on" in str1 and "on" in str2
print(result)

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
str_1, sentence = "jargon", "I hope this course is not full of jargon"
result = "jargon" in sentence
print(result)

# 15. There is no 'on' in both dragon and python.
str15a, str15b = "python", "dragon"
result = "on" not in str15a and "on" in str15b
print(result)

# 16. Find the length of the text python and convert the value to float and convert it to string.
print(float(len("python")))
print(str(len("python")))

# 17. Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?

num17 = 4
result = num17/2 and num17%2 == 0
print(result)

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div18, integ_val18 = 7//3, int(2.7)
result = floor_div18 == integ_val18
print (result, floor_div18, integ_val18)

# 19. Check if type of '10' is equal to type of 10
equality_19 = type('10') == type(10)
print("Is type of '10' is equal to type of 10?", equality_19)

# 20. Check if int('9.8') is equal to 10.
int('9.8') # invalid literal for int() with base 10: '9.8
int(9.8) == 10
# False

# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
work_hours = input('Enter your working hours:', )
rate_per_h = input('Enter your rate per hour:', )
pay_per_week = float(work_hours) * float(rate_per_h)
pay_per_month = pay_per_week * 4
pay_per_year = pay_per_week * 52
print(pay_per_week, pay_per_month, pay_per_year)

# 22. Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
num_years = int(input('Enter number of years: '))

sec_in_min = 60
min_in_h = 60
h_in_day = 24
day_in_year = 365
num_sec_in_100_years = sec_in_min * min_in_h * h_in_day * day_in_year * num_years
# Use 'f' to evaluate expression in the {} and include their values in the string.
print(f"There are {num_sec_in_100_years} seconds to live in 100 years.")

# 23. Write a Python script that displays the following table:
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# Attempt 1:
n_1 = 1
n_2 = 2
n_3 = 3
n_4 = 4
n_5 = 5
print(n_1, n_1, n_1, n_1, n_1)
print(n_2, n_1, n_2, n_2**2, n_2**3)
print(n_3, n_1, n_3, n_3**2, n_3**3)
print(n_4, n_1, n_4, n_4**2, n_4**3)
print(n_5, n_1, n_5, n_5**2, n_5**3)

# Nested list:
matrix_23 = [
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125]
]

print(matrix_23)


# Define the values of n_1, n_2, n_3, n_4, n_5
n_values = [1, 2, 3, 4, 5]

# Initialize a 5x5 matrix with zeros
matrix = [[0]*5 for _ in range(5)]

# Fill the matrix according to the specified pattern
for i in range(5):
    for j in range(5):
        if j == 0:
            matrix[i][j] = n_values[i]  # n_1, n_2, n_3, n_4, n_5
        elif j == 1:
            matrix[i][j] = n_values[0]  # n_1 for all rows
        elif j == 2:
            matrix[i][j] = n_values[i]  # n_1, n_2, n_3, n_4, n_5
        elif j == 3:
            matrix[i][j] = n_values[i] ** 2  # n_1^2, n_2^2, n_3^2, n_4^2, n_5^2
        elif j == 4:
            matrix[i][j] = n_values[i] ** 3  # n_1^3, n_2^3, n_3^3, n_4^3, n_5^3

# Print the matrix row by row
for row in matrix:
    print(row)
