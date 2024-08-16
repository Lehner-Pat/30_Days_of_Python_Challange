# Strings

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name) > len(last_name))

print('Days\tTopics\tExercises')
print('1\t5\t5')
print('2\t6\t20')
print('3\t5\t23')
print('4\t1\t35')

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s.' %(first_name, last_name, language)
print(formated_string)

import math
radius = 10
pi = math.pi
area = pi * radius**2
formated_string_2 = 'The area of a circle with radius %d is %.2f.' %(radius, area) #
print(formated_string_2)
print(f'The area of a circle with radius 10 is {area}.') #

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}.'.format(first_name, last_name, language)
print(formated_string)

first_name = 'Patrick'
last_name = 'Lehner'
language = 'Python'
formated_string = 'I am {} {}. I am studying {}.'.format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))

import math
radius = 10
area = math.pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.10f}.'.format(radius, area)
print(formated_string)

language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

greeting = 'Hello, World!'
print(greeting[::-1])

first_name = 'Patrick'
last_name = 'Lehner'
age = 30
job = 'analyst'
country = 'Germany'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence)

# Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(words)
print(result)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
words = ['Coding', 'For', 'All']
result = ' '.join(words)
print(result)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company) 

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.swapcase())
print(company.capitalize())
print(company.title())

# 9. Cut(slice) out the first word of Coding For All string.
company = "Coding For All"
first_word = company [0:6]
print(first_word)


# 10. Check if "Coding For All" string contains the word 'Coding' using the method index, find or other methods.
company = "Coding For All"
sub_string = "Coding"
print(company.index(sub_string))
print(company.find('Coding'))
print(company.find('For'))


# 11. Replace the word coding in the string 'Coding For All' to Python.
company = "Coding For All"
print(company.replace('Coding', 'Python'))


# 12. Change Python for Everyone to Python for All using the replace method or other methods.
motto_v1 = 'Python for Everyone'
print(motto_v1.replace('Everyone', 'All'))


# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.replace('Python', 'Coding'))
print(company.split(' '))


# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_comps = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_comps.split(','))


# 15. What is the character at index 0 in the string Coding For All.
print(company)
print(company[0])


# 16. What is the last index of the string Coding For All.
print(company[-1])


# 17. What character is at index 10 in "Coding For All" string.
print(company)
print(company[10])
# space


# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(company)
company = company.replace('Coding', 'Python')
company = company.replace('All', 'Everyone')
print(company)
acronym_comp = 'PFE'


# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
motto_v1 = 'Python For Everyone'
print(motto_v1)
motto_v1 = motto_v1.replace('Python', 'Coding')
motto_v1 = motto_v1.replace('Everyone', 'All')
print(motto_v1)
acronym_motto = 'CFA'


# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(motto_v1)
print(motto_v1.find('C'))
# Index 0


# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(motto_v1)
print(motto_v1.find('F'))
# Index 7


# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
cfap = 'Coding for all people'
print(cfap.rfind('l'))
# Index 19


# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because 'because' is a conjunction'
sentence_23 = 'You cannot end a sentence with because "because" is a conjunction'
print(sentence_23.find('because'))
# Index 31


# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence_23.rfind('because'))
# Index 40


# 25. Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
weird_sentence = 'You cannot end a sentence with because because because is a conjunction'
because_triple = weird_sentence[31:54]
print(because_triple)


# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
# SEE 23


# 27. Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
# SEE 25


# 28. Does 'Coding For All' start with a substring Coding?
print(motto_v1)
print(motto_v1.find('Coding'))
# Yes


# 29. Does 'Coding For All' end with a substring coding?
print(motto_v1)
ends_with_coding = motto_v1.endswith('coding')
print(ends_with_coding)


# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
motto_with_spaces = '   Coding For All      '
print(motto_with_spaces)
motto_without_spaces = motto_with_spaces.strip(' ')
print(motto_without_spaces)


# 31. Which one of the following variables return True when we use the method isidentifier():
# - 30DaysOfPython
# - thirty_days_of_python

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
# The second one does.


# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_separator = ' # '
result = join_separator.join(python_libraries)
print(result)


# 33. Use the new line escape sequence to separate the following sentences. 
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')


# 34. Use a tab escape sequence to write the following lines. 
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tExercises\nAsabeneh\t250\tFinland\tHelsinki')

# 35. Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
formated_string_exerc = 'The area of a circle with a radius %d is %.f.' %(radius, area)
print(formated_string_exerc)


# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a, b = 8, 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a **b))

