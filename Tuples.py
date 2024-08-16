# Tuples and Tuplerones

# Exercises: Level 1

# 1. Create an empty tuple.
empty_tuple = ()
print(empty_tuple)
nill_tuple = tuple()
print(nill_tuple)


# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
imag_sibl_bros = ('Roggls', 'Hosenberger', 'Wastlcito')
print(imag_sibl_bros)

imag_sibl_siss = ('Sarah', 'Sophie', 'Géraldine')
print(imag_sibl_siss)


# 3. Join brothers and sisters tuples and assign it to siblings
all_sibl = imag_sibl_siss + imag_sibl_bros
print(all_sibl)


# 4. How many siblings do you have?
nr_all_sibl = len(all_sibl)
print(nr_all_sibl)
# Answer: 6.


# 5. Modify the siblings tuple and 
# add the name of your father and mother and assign it to family_members
all_sibl_list = list(all_sibl)
print(all_sibl_list)

all_sibl_list.extend(['Papa', 'Mama'])
family_members = tuple(all_sibl_list)
print(family_members)


# Exercises: Level 2

fruits = ('banana', 'orange', 'mango', 'lemon')
some_fruits = fruits[0:3]
print(some_fruits)


# 1. Unpack siblings and parents from family_members
print(len(family_members))
sibl = family_members[0:6]
print(sibl)
parents = family_members[6:8]
print(parents)

# 2. Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
some_fruits = fruits[0:3]
print(some_fruits)
print(fruits)

vegetables = ('cucumber', 'carrot', 'bellpepper')
print(vegetables)

animal_prod = ('cheese', 'meat', 'eggs')
print(animal_prod)

foods_tp = fruits + vegetables + animal_prod
print(foods_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
foods_list = list(foods_tp)
print(foods_list)


# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
len(foods_list)
foods_list[4:6]


# 5. Slice out the first three items and the last three items from food_staff_lt list
foods_list[0:3]
foods_list[7:10]


# 6. Delete the food_staff_tp tuple completely
del foods_tp
print(foods_tp)


# 7.     Check if an item exists in tuple:

# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
# Given: 
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'Estonia' in nordic_countries
'Iceland' in nordic_countries

# Done.









