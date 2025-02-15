fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1]) # Output: cherry (negative index starts from the end)
#modify List
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

numbers = [5, 2, 8, 1]

numbers.append(10)  # [5, 2, 8, 1, 10]
#append(item): Adds an item to the end of the list

#insert(index, item): Inserts an item at a specific index
numbers.insert(1, 15)  # [5, 15, 2, 8, 1, 10]
#remove(item) :Removes the first occurrence of the item
numbers.remove(2)  # [5, 15, 8, 1, 10]

#pop(index):Removes and returns an item at the given index (default: last item)
numbers.pop()  # Removes last element: [5, 15, 8, 1]
#sort(): Sorts the list in ascending order
numbers.sort()  # [1, 5, 8, 15]

#reverse(): Reverses the order of elements in the list
numbers.reverse()  # [15, 8, 5, 1]


print(numbers)  # Output: [15, 8, 5, 1]


#Using for loop  list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


#List Comparision
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

#Copy List
list1 = [1, 2, 3]
list2 = list1.copy()  # or list1[:]

#MultiDimensional list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6

