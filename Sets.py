# Sets

init_set = {'item1', 'item2', 'item3'}
print(init_set)

len(init_set)
print("The length of the initial set is:", len(init_set))

print("Does init_set contain 'item4':", 'item4' in init_set)

init_set.add('item_a, item_b')
print(init_set)

init_set.remove('item_a, item_b')
print(init_set)


# Join OR Union
breddas = {'Sepp', 'Wast', 'Nick'}
sistas = {'Gerry', 'Srizzle', 'Souphl'}
siblinhos = breddas.union(sistas)
print(siblinhos)


# Intersection AND 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
inters1and2 = st1.intersection(st2)
print(inters1and2)


# Symmetric Difference
# (A\B) ∪ (B\A)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print("The symmetric difference is:", whole_numbers.symmetric_difference(some_numbers)) 
# {0, 6, 7, 8, 9, 10}


# Checking disjoints sets
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)
# TRUE


# EXERCISES: Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# 1. Find the length of the set it_companies
print("Number of companies in set is:", len(it_companies))


# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)


# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['SAP', 'Secunet'])
print(it_companies)


# 4. Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print(it_companies)


# 5. What is the difference between remove and discard?
# Answer: We can remove an item from a set using the remove() method. If the item is not found remove() method will raise errors, 
# so it is good to check if the item exist in the given set. However, the discard() method doesn't raise any errors.


# Exercises: Level 2

# 1. Join A and B.
C = A.union(B)
print(C)


# 2. Find A intersection B.
A_intersect_B = A.intersection(B)
print(A_intersect_B)
# All of A is the intersection of the two sets.


# 3. Is A subset of B?
print(A.issubset(B))
# Yes.


# 4. Are A and B disjoint sets?
print(A.isdisjoint(B))
# False.


# 5. Join A with B and B with A.
print(C) # A.union(B)
C1 = B.union(A)
print(C1)


# 6. What is the symmetric difference between A and B?
# (A\B) ∪ (B\A)
print(A)
print(B)
print("The symmetric difference is:", A.symmetric_difference(B)) 


# 7. Delete the sets completely.
del A
print(A)
del B
print(B)


# Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24] # = List
age_set = set(age)
print(age_set)


# 2. Explain the difference between the following data types: string, list, tuple and set.
# string: 'string', list: list['list', '2'], tuple: tuple()-unalterable, set: set{}-no order-multiple elements count only once
# - String: Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings.
# - List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# - Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# - Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.


# 3. "I am a teacher and I love to inspire and teach people." How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.

# Manual attempt:
sentence = {'I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people'}
print(len(sentence))
# Answer: 10


# Split method attempt:
sentence_2 = "I am a teacher and I love to inspire and teach people."
words = sentence_2.split()
print(words)
indiv_words_SET = set(words)
print(indiv_words_SET)
len(indiv_words_SET)
# Answer: 10





