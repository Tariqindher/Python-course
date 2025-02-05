x=27
# if
if x>=18:
    print("You are adult")
print("You are not adult")

#if else
marks=80
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
else:
    print("Try Again")


#Nested If
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")


# For Loop
print()
print()
# print number 1 to 5
for i in range(1,6): #6 is not include
    print(i)

#Loop through the list
Fruits=["Apple", "Banana","Orange"]

for fruit in Fruits:
    print(fruit)

#Using for Loop with else
for i in range(1,5):
    print(i)
else:
    print("Loop Finished")

#Nested Loop

for i in range(1,3):
    print("Outer loop ")
    for j in range(1,3):
        print(i,"  ",j)