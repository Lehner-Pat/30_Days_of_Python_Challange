# Dictionaries
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

dictionary = {'key1':'value1', 'key2':'value2', 'key3': 'value3', 'key4': 'value4'}
print(dictionary)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space Street',
        'zipcode': '02210'
    }
}
print(person)

print(len(dictionary))
print(len(person))
print(person['is_married'])
print(person.get('first_name'))

print(person.get('city')) # none instead of error


# Adding another pair:

print(dictionary)
dictionary['key5'] = 'value5'
print(dictionary)

person['job_title'] = 'instructor'
person['skills'].append('HTML')

print(person)


# We can modify items in a dictionary

# Syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

# Check "in":
print('key4' in dictionary)
print('key5' in dictionary)
print('key6' in dictionary)


# Turns into a list of (tuple?) items:
print(dictionary.items())
print(dictionary)


# Deleting specifically or entirely:
del person['address']  # removes key
del dictionary # deletes entire dictionary

dictionary_copy = dictionary.copy()
print(dictionary_copy)


# All the keys of a dict as a list:
keys = dictionary.keys()
print(keys)


# All the values of a dict as a list:
values = dictionary.values()
print(values)


# Exercises: Day 8

# 1. Create an empty dictionary called dog
dog = {}
print(dog)


# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Doggo'
dog['colour'] = 'black and white'
dog['legs'] = '4'
dog['age'] = '0'
print(dog)


# 3. Create a student dictionary and add first_name, last_name, gender, age, 
# marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Horst',
    'last_name':'Seehofer',
    'gender':'male',
    'age':'oid',
    'marital_status':'married',
    'skills':['political discours', 'modelling'],
    'country':'Bayern',
    'city':'Minga',
    'address':'dort, wo er wohnt zefix'
}
print(student)


# 4. Get the length of the student dictionary
print(len(student))


# 5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type('skills'))
# Its type is string, not list. 


# 6. Modify the skills values by adding one or two skills
student['skills'].append('Bier sauffa')
student['skills'].append('Wiaschd essn')
print(student)


# 7. Get the dictionary keys as a list
student_keys_list = student.keys()
print(student_keys_list)


# 8. Get the dictionary values as a list
student_values_list = student.values()
print(student_values_list)


# 9. Change the dictionary to a list of tuples using items() method
print(student.items())


# 10. Delete one of the items in the dictionary
del student['marital_status']
print(student)


# 11. Delete one of the dictionaries
print(dictionary_copy)
del dictionary_copy
print(dictionary_copy)
# Done.








