# Input and Output

# Variables
# Python is a language that does not require explicit declaration of variable types. However, it is good practice to assign values consistent with the expected type.
# Example:
age = 26  # Here, age is a variable of type integer
name = "Maria"  # Here, name is a variable of type string

# Mathematical Operations (Arithmetic)
# Python supports all basic mathematical operations.
# Example:
sum = 10 + 5
subtraction = 20 - 8
multiplication = 3 * 7
division = 15 / 3
power = 2 ** 3
remainder = 20 % 3

# Type Conversion
# It is possible to convert between data types using conversion functions.
# Example:
age_text = '26'
age_integer = int(age_text)  # Converting string to integer
print(age_integer)  # Output: 26

# Conditional Statements and Best Practices
# Python supports conditional statements like if, elif, and else.
# Example:
age = 17
if age >= 18:
    print("You are of legal age.")
else:
    print("You are a minor.")

# Loops ("While") and Best Practices, when to use while
# The 'while' loop is useful when the number of iterations is not known in advance.
# Example:
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Loops (For) and Best Practices, when to use it and examples of range
# The 'for' loop is useful for iterating over a sequence (like lists, tuples, strings, etc.).
# Example:
for i in range(5):
    print(i)

# The range object can be used to generate a sequence of numbers.
# Example:
even_numbers = list(range(0, 10, 2))  # Creates a list of even numbers from 0 to 8 (exclusive), incrementing by 2.
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# Lists
# Lists in Python can contain elements of different types and are mutable.
# Example:
number_list = [1, 2, 3, 4, 5]
string_list = ['a', 'b', 'c']
mixed_list = [1, 'a', True]

# List Methods and Functions
# Python provides a variety of built-in methods for manipulating lists.
# Example:
my_list = [3, 1, 2, 4, 5]
my_list.sort()  # Sorts the list
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Adding elements to a list:
my_list.append(6)  # Adds the number 6 to the list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Removing elements from a list:
my_list.remove(3)  # Removes the number 3 from the list
print(my_list)  # Output: [1, 2, 4, 5, 6]

# Function Examples
# In Python, functions are defined using the 'def' keyword.
# Example:
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# Dictionaries
# Dictionaries in Python are unordered collections of key-value pairs.
# While they can be used to model objects and their properties, dictionaries do not have methods or behaviors associated like objects in object-oriented languages.
# Example:
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person['name'])  # Output: John

# Adding new items to the dictionary:
person['profession'] = 'Engineer'
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'profession': 'Engineer'}

# Iterating over dictionary keys and values:
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary:
if 'age' in person:
    print("Age is present.")

# Getting only the keys of the dictionary:
keys = person.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city', 'profession'])

# Getting only the values of the dictionary:
values = person.values()
print(values)  # Output: dict_values(['John', 30, 'New York', 'Engineer'])
