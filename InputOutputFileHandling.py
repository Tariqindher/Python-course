print("Hello Tariq")

name='Tariq'
print("My Name is ",name)

#Use F-String Modern and clean
age=22
print(f"My age is {age}")

name=input("Enter Ur Name")
print(f"Hello,{name}!")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum is:", num1 + num2)


#Create or write to a file (w mode)
file = open("example.txt", "w")  # 'w' means write mode
file.write("This is Tariq's first file.\n")
file.write("Welcome to file handling!")
file.close()

#Read from a file Mood
file = open("example.txt", "r")  # 'r' means read mode
content = file.read()
print(content)
file.close()


#Append to file mode
file = open("example.txt", "a")  # 'a' means append mode
file.write("\nThis line is added later.")
file.close()


#Use with statement (auto-closes file)
with open("example.txt", "r") as file:
    print(file.read())






