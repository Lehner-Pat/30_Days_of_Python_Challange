# Day 5: Lists

empty_list = list()
print(empty_list)

list = []
print(list)

fruits = ['mango', 'banana', 'orange', 'apple']
print(fruits)
print(len(fruits))
print('Fruits:', fruits)

list_teacher = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]
print(list_teacher)

# Accessing items in list:

first_fruit = fruits[0]
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# Unpacking list items
lst = ['item1','item2','item3','item4','item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(rest)

number_list = [1,2,3,4,5,6,7,8,9,10]
print(number_list)
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(rest)
print(tenth)

# Slicing items from a list
print(fruits)
all_fruits = fruits[0:4]
print(all_fruits)
mango_banana = fruits[0:2]
print(mango_banana)
apple_orange = fruits[-1:-3:-1]
print(apple_orange)

# Inserting items to a list
print(fruits)
fruits.append('kiwi')
print(fruits)
fruits.insert(0,'lime')
print(fruits)

print(lst)
lst.remove('item5')
print(lst)

print(number_list)
number_list.pop()
print(number_list)
number_list.append(10)
print(number_list)
number_list.pop(0)
print(number_list)
number_list.insert(0,0)
print(number_list)
number_list.pop(0)
print(number_list)
number_list.insert(0,1)
print(number_list)

print(lst)
lst.sort(reverse=True)
print(lst)
lst.sort()
print(lst)

print(fruits)
print(sorted(fruits))
print(fruits)

# EXERCISES: DAY 5

# Level 1

# 1. Declare an empty list
empty_list = []
print(empty_list)


# 2. Declare a list with more than 5 items
list_with_7_items = [1,2,3,4,5,6,7]
print(list_with_7_items)


# 3. Find the length of your list
print(len(list_with_7_items))


# 4. Get the first item, the middle item and the last item of the list
selected_items_list = [list_with_7_items[0], list_with_7_items[len(list_with_7_items) // 2], list_with_7_items[-1]]
print(selected_items_list)
# One step approach


# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Pamtros Lehnertz','30','178','single','NonYoBizStr420']
print(mixed_data_types)


# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Fb','Gg','Ms','Ap','IBM','Oc','Am']


# 7. print(it_companies)
print(it_companies)


# 8. Print the number of companies in the list
print(len(it_companies))


# 9. Print the first, middle and last company
selected_comp_list = [it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1]]
print(selected_comp_list)


# 10. Print the list after modifying one of the companies
it_companies[6] = 'Amz'
print(it_companies)


# 11. Add an IT company to it_companies
it_companies.append('SAP')
print(it_companies)
it_companies.pop(7)
print(it_companies)
it_companies.insert(7,'SAP')
print(it_companies)


# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4,'NVD')
print(it_companies)


# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = [[it_companies[0].upper()] + [it_companies[1:7]]]
print(it_companies)
it_companies = it_companies[0]
print(it_companies)


# 14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print(joined_companies)
#dunno


# 15. Check if a certain company exists in the it_companies list.
print(it_companies)
does_exist = 'Ms' in it_companies
print(does_exist)



# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)


# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)


# 18. Slice out the first 3 companies from the list
print(it_companies)
Oc_NVD_Ms = it_companies[0:3]
print(Oc_NVD_Ms)

# 19. Slice out the last 3 companies from the list
print(it_companies)
Gg_FB_Ap = it_companies[-1:-4:-1]
print(Gg_FB_Ap)


# 20. Slice out the middle IT company or companies from the list
print(it_companies)
middle_it_comp = [it_companies[len(it_companies) // 2]]
print(middle_it_comp)


# 21. Remove the first IT company from the list
print(it_companies)
it_companies.pop(0)
print(it_companies)


# 22. Remove the middle IT company or companies from the list
print(it_companies)
del it_companies[2:3]
print(it_companies)
it_companies.insert(3, 'IBM')
print(it_companies)
del it_companies[2:4]
print(it_companies)


# 23. Remove the last IT company from the list
print(it_companies)
del it_companies[-1]
print(it_companies)


# 24. Remove all IT companies from the list
del it_companies[0:3]
print(it_companies)


# 25. Destroy the IT companies list
del it_companies
print(it_companies)
# done


# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print(front_end)
print(back_end)

# 27. After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


# Level 2

# 1. List of student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
min_max_age = [19, 26]

# Add the min age and the max age again to the list
ages.append(19)
ages.append(26)
print(ages)
ages.sort()
print(ages)


# Find the median age (one middle item or two middle items divided by two)
import math
median_age = [ages[len(ages) // 2]]
print(median_age)


# Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print(average_age)

# Find the range of the ages (max minus min)
range_of_ages = ages[-1] - ages[1]
print('The range of ages is:',range_of_ages)

# Compare the value of (min - average) and (max - average), use abs() method
abs((ages[0] - average_age))
abs((ages[-1] - average_age))

import matplotlib.pyplot as plt

# Plotting the ages as a histogram
plt.hist(ages, bins=range(min(ages), max(ages) + 1, 1), edgecolor='black')  # Adjust bins as per your preference
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')
plt.grid(True)
plt.show()


# Find the middle country(ies) in the countries list:

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

print(countries)
middle_country = countries[len(countries) // 2]
print('The middle country in the countries list is:', middle_country)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# All the way to Lesotho
print(len(countries) // 2)
half_of_the_countries = countries[0:97]
print('All the way to Lesotho:', half_of_the_countries)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as nordic countries.
old_friends = ['China', 'Russia', 'USA']
nordic_countries = ['Finland', 'Sweden', 'Norway', 'Denmark']
print(old_friends, nordic_countries)






