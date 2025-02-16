 #Tuples are used to store multiple items in a single variable. 
 # They are similar to lists but immutable, meaning their values cannot be changed after creation.
# Creating a tuple
my_tuple = (1, 2, 3, "Hello", 3.14)
print(my_tuple)

#Accesing Element
# Indexing
print(my_tuple[1])  # Output: 2

# Negative Indexing
print(my_tuple[-1])  # Output: 3.14

# Slicing
print(my_tuple[1:4])  # Output: (2, 3, 'Hello')

#Touple Operation
# Length of Tuple
print(len(my_tuple))  # Output: 5

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
print(tuple1 * 2)  # Output: (1, 2, 3, 1, 2, 3)

#touple Method

# Count occurrences
t = (1, 2, 2, 3, 4, 2)
print(t.count(2))  # Output: 3

# Find index of an element
print(t.index(3))  # Output: 3

#Tuple Packing and Unpacking:
# Packing
my_tuple = ("Apple", "Banana", "Cherry")

# Unpacking
fruit1, fruit2, fruit3 = my_tuple
print(fruit1)  # Output: Apple
print(fruit2)  # Output: Banana
print(fruit3)  # Output: Cherry

