# ------------------------------- append() -------------------------------------

# Adding one element to list
currencies = ['Dollar', 'Euro', 'Pound']
# append 'Rupee' to the list
currencies.append('Rupee')
print(currencies)

# Adding a list to the list

# animals list
animals = ['cat', 'dog', 'rabbit']
# list of wild animals
wild_animals = ['tiger', 'fox']
# appending wild_animals list to animals
animals.append(wild_animals)
print('Updated animals list: ', animals)
# o/p : Updated animals list:  ['cat', 'dog', 'rabbit', ['tiger', 'fox']]


# ------------------------------- extend() -------------------------------------

# create a list
prime_numbers = [2, 3, 5]
# create another list
numbers = [1, 4]
# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)
print('List after extend():', numbers)
# o/p : List after extend(): [1, 4, 2, 3, 5]

# Adding elements of tuple and set to the list
# languages list
languages = ['French']
# languages tuple
languages_tuple = ('Spanish', 'Portuguese')
# languages set
languages_set = {'Chinese', 'Japanese'}
# appending language_tuple elements to language
languages.extend(languages_tuple)
print('New Language List:', languages)
# appending language_set elements to language
languages.extend(languages_set)
print('Newer Languages List:', languages)

# Using + operator
a = [1, 2]
b = [3, 4]
a += b    # a = a + b
print('a =', a)
# Output: [1, 2, 3, 4]

# Using list slicing
a = [1, 2]
b = [3, 4]
a[len(a):] = b
print('a =', a)
# Output: [1, 2, 3, 4]


# ------------------------------- insert() -------------------------------------


# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
# insert 11 at index 4
prime_numbers.insert(4, 11)
print('List:', prime_numbers)


mixed_list = [{1, 2}, [5, 6, 7]]
# number tuple
number_tuple = (3, 4)
# inserting a tuple to the list
mixed_list.insert(1, number_tuple)
print('Updated List:', mixed_list)
# o/p: Updated List: [{1, 2}, (3, 4), [5, 6, 7]]


# ------------------------------- remove() -------------------------------------

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# 'rabbit' is removed
animals.remove('rabbit')
# Updated animals List
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['cat', 'dog', 'guinea pig']


# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
# 'dog' is removed
animals.remove('dog')
# Updated animals list
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['cat', 'dog', 'guinea pig', 'dog']


# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# Deleting 'fish' element
animals.remove('fish')
# Updated animals List
print('Updated animals list: ', animals)


# ------------------------------- count() -------------------------------------

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count)
# o/p: The count of i is: 2
# count element 'p'
count = vowels.count('p')
# print count
print('The count of p is:', count)
# o/p: The count of i is: 0


# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
# count element ('a', 'b')
count = random.count(('a', 'b'))
# print count
print("The count of ('a', 'b') is:", count)
# o/p: The count of ('a', 'b') is: 2
# count element [3, 4]
count = random.count([3, 4])
# print count
print("The count of [3, 4] is:", count)
# o/p: The count of [3, 4] is: 1


# ------------------------------- pop() -------------------------------------


# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']
# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)
# o/p: Return Value: French
# Updated List
print('Updated List:', languages)
# o/p: Updated List: ['Python', 'Java', 'C++', 'C']


# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
# remove and return the last item
print('When index is not passed:') 
print('Return Value:', languages.pop())
print('Updated List:', languages)
# o/p: When index is not passed:
#      Return Value: C
#      Updated List: ['Python', 'Java', 'C++', 'Ruby']
# remove and return the last item
print('\nWhen -1 is passed:') 
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)
# o/p: When -1 is passed:
#      Return Value: Ruby
#      Updated List: ['Python', 'Java', 'C++']
# remove and return the third last item
print('\nWhen -3 is passed:') 
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)
# o/p: When -3 is passed:
#      Return Value: Python
#      Updated List: ['Java', 'C++']


