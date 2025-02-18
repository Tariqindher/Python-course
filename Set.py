
# A dictionary is a data structure that stores key-value pairs, where each key is unique.
# Using curly braces {}
my_set = {1, 2, 3, 4, 5}

# Using set() function
my_set2 = set([5, 6, 7, 8])  # Converts list to set

# Creating an empty set (Note: {} creates an empty dictionary)
empty_set = set()

print(my_set)
print(my_set2)
print(empty_set)


#Accessing element
for item in my_set:
    print(item)

my_set.add(6)  # Adds a single element
print(my_set)

#Removing element 
my_set.remove(2)  # Removes 2 (Raises error if not found)
my_set.discard(3)  # Removes 3 (No error if not found)
popped_item = my_set.pop()  # Removes a random item
print(my_set, popped_item)

my_set.clear()  # Removes all elements
print(my_set)   # Output: set()

#Set Operation

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Output: {1, 2, 3, 4, 5}
print(A.union(B))  # Same as A | B

print(A & B)  # Output: {3}
print(A.intersection(B))  # Same as A & B

print(A - B)  # Output: {1, 2}
print(A.difference(B))  # Same as A - B

print(A ^ B)  # Output: {1, 2, 4, 5}
print(A.symmetric_difference(B))  # Same as A ^ B


A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))  # True (A is a subset of B)
print(B.issuperset(A))  # True (B is a superset of A)

squared_numbers = {x**2 for x in range(1, 6)}
print(squared_numbers)  # Output: {1, 4, 9, 16, 25}
