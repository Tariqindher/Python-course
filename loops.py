#Loop
# It executes a block of code multiple times.


#Types of loop
#For Loop
#A for loop is used when we know the number of iterations in advance. 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#While Loop
#A while loop runs as long as a condition is True.
num = 1
while num <= 5:
    print(num)
    num += 1


#Range() function:generates a sequence of numbers and is commonly used in loops.
#Syntax
#range(start, stop, step)

#using range in for
for i in range(1, 6):  # Numbers from 1 to 5
    print(i)

#Statement

#Break: break statement exits the loop immediately when a condition is met.
for i in range(1, 6):
    if i == 3:
        break
    print(i)

#Continue:  The continue statement skips the current iteration and moves to the next one.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#Pass Statement: The pass statement is a placeholder when a block of code is required but not yet implemented.
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder, does nothing
    print(i)