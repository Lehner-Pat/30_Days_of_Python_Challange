# Day 10: Loops

# In order to handle repetitive tasks, programming languages use loops.
# Python programming language also provides the following types of two loops:
# while loop
# for loop

# While Loop

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)


count = 0
while count <= 10:
    print(count)
    count = count + 2


count = 0
while count <= 10:
    if count == 6:
        count = count + 2
        continue
    print(count)
    count = count + 2


# For Loop
# Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)


language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])


zero_to_four = []
for i in range(5):
    zero_to_four.append(i)
print(zero_to_four)


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)


for key, value in person.items():
    print(key, value)


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
for company in it_companies:
    print(len(company))


numberones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numberones:
    print(number)
    if number == 4:
        break


# cool

numberones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numberones:
    print(number)
    if number == 5:
        continue
    print('The next number should be ', number + 1) if number != 9 else print("loop's end")


numberones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0

while index < len(numberones):
    number = numberones[index]
    print(number)
    if number <= 7:
        print('These are the numbers from 0 to 7:', number)
    if number == 9:
        print("End while")
    index += 1


numberones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number = 0

while number in numberones:
    print(number)
    if number <= 7:
        print('These are the numbers from 0 to 7:', number)
    if number == 9:
        print("End while")
    number += 1


number_list = list(range(0, 12, 2))
print(number_list)


for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)



# Exercises: Day 10

# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number)   
else: # not obligatory
    print('The for-loop stops at', number)


count_to_ten = 0
while count_to_ten <= 10:
    print(count_to_ten)
    count_to_ten = count_to_ten + 1
    if count_to_ten == 11:
        break

# even more simplistic:
count_to_ten = 0
while count_to_ten <= 10:
    print(count_to_ten)
    count_to_ten += 1



# 2. Iterate 10 to 0 using for loop, do the same using while loop.
list_11_0 = []
for number in range (10, -1, -1):
    print(number)
    list_11_0.append(number)
print(list_11_0)

countdown_to_zero = 10
countdown = []
while countdown_to_zero >= 0:
    print(countdown_to_zero)
    countdown.append(countdown_to_zero)
    countdown_to_zero -= 1
print(countdown)


# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
n = 7
for i in range(1, n + 1):
    print('#' * i)


# 4. Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
n = 8
for _ in range(n):
    print('#' * 8)


# 5. Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
n = 10
for i in range(0, n + 1):
    print(f'{i} * {i} = {i * i}')

# noiccce


# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
exerc_6_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in exerc_6_list:
    print(item)


# 7. Use for loop to iterate from 0 to 100 and print only even numbers
even_number_list = []
for number in range(0, 101, 2):
    even_number_list.append(number)
print(even_number_list) # Print outside the loop


# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
odd_number_list = []
for number in range (1, 100, 2):
    odd_number_list.append(number)
print(odd_number_list)


# Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_of_numbs = []
for number in range(0, 101, 1):
    sum_of_numbs.append(number)
print("The sum of all numbers is:", sum(sum_of_numbs))
# 5050. Worked like a charm.


# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print(sum(odd_number_list)) # 2500
print(sum(even_number_list)) # 2550
sum_of_all = sum(odd_number_list) + sum(even_number_list)
print(sum_of_all) # 5050


# Exercises: Level 3

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

country_list = [line.strip() for line in countries]
print(country_list)


with open('/Users/mac/Downloads/countries.py', 'r') as file:
    vertical_list = file.readlines()
horizontal_list = [line.strip() for line in vertical_list]
print(horizontal_list)
country_list = horizontal_list


# 1. Loop through the countries and extract all the countries containing the word land.

for country in country_list:
    if 'land' in country:
        print(country)

# 'Finland', 'Iceland', 'Ireland', 'Marshall Islands', 'Netherlands', 'New Zealand', 'Poland', 'Solomon Islands', 'Swaziland', 'Switzerland', 'Thailand'


# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
reversed_fruit_list = []
for i in range(len(fruit_list)-1, -1, -1):
    reversed_fruit_list.append(fruit_list[i])
print('The fruit list in reversed order: ', reversed_fruit_list)


# 3. Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world

file_path = '/Users/mac/Downloads/countries-data.py'
with open(file_path, 'r') as file:
    country_data = file.read()
print(country_data)
print('languages' in country_data)

list_of_languages = []

# Iterate over each country in the country_data list
for country in country_data:
    # Check if the 'languages' key exists in the dictionary
    if 'languages' in country:
        # Extend the list_of_languages with the languages from the current country
        list_of_languages.extend(country['languages'])

# Print the flattened list of languages
print("List of languages:", list_of_languages)

# Get unique languages
unique_languages = set(list_of_languages)
print("Number of unique languages:", len(unique_languages))


# 3.1 What are the total number of languages in the data?

list_of_languages = []
for dictionary in country_data:
    print(dictionary['languages'])
    list_of_languages.extend(dictionary['languages'])
print("All languages:", list_of_languages)
print(len(list_of_languages))
# total 368 values for languages-key

unique_languages = set(list_of_languages)
print(unique_languages)
print(len(unique_languages))
# 112 unique languages


# 3.2 Find the ten most spoken languages from the data
list_of_languages = []
for dictionary in country_data:
    print(dictionary['languages'])
    list_of_languages.extend(dictionary['languages'])
print("All languages:", list_of_languages)
print(len(list_of_languages))

unique_languages = set(list_of_languages)
print(unique_languages)
print(len(unique_languages))


# Plotting approach:
import matplotlib.pyplot as plt
from collections import Counter
list_of_languages
language_counts = Counter(list_of_languages)
print(language_counts)

languages_name_list = list(language_counts.keys())
print(languages_name_list)
counts_list = list(language_counts.values())
print(counts_list)

plt.figure(figsize=(10, 6))  # Set the size of the plot
plt.bar(languages_name_list, counts_list, color='skyblue')

plt.title('Absolute Language Prevalence')
plt.xlabel('Languages')
plt.ylabel('Count')

plt.xticks(rotation=45)

plt.tight_layout()  
plt.show()


# Second approach:
import heapq
counts_list
languages_name_list
counts_and_languages_list = list(zip(counts_list, languages_name_list))
print(counts_and_languages_list)

ten_most_spoken_lang = heapq.nlargest(10, counts_and_languages_list, key=lambda x: x[0])
print(ten_most_spoken_lang)

print("The ten most spoken languages are:")
for value, name in ten_most_spoken_lang:
    print(f"Language: {name}, Value: {value}")


# 3.3 Find the 10 most populated countries in the world
pop_of_countries = []
for dictionary in country_data:
    print(dictionary['population'])
    pop_of_countries.append(dictionary['population'])
print("All country populations:", pop_of_countries)

country_names = []
for dictionary in country_data:
    print(dictionary['name'])
    country_names.append(dictionary['name'])
print("All country names:", country_names)

import heapq
population_and_country_names = list(zip(pop_of_countries, country_names))
print(population_and_country_names)

ten_largest_populations = heapq.nlargest(10, population_and_country_names, key=lambda x: x[0])
print(ten_largest_populations)

# DONE




