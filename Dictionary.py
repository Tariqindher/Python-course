
# A dictionary in Python is a collection of key-value pairs where each key is unique,  
# and it allows fast data retrieval, modification, and deletion.

# Using curly braces {}
student = {
    "name": "Tariq",
    "age": 22,
    "course": "Computer Science"
}

# Using the dict() function
student2 = dict(name="Zaheer", age=21, course="Mathematics")

print(student)
print(student2)
#Accesing Value
print(student["name"])   # Output: Tariq
print(student.get("age"))  # Output: 22

#Difference between [] and get()
#[] raises an error if the key does not exist.
#get() returns None if the key is missing

#Adding and Updating
student["university"] = "IBA"  # Adding a new key-value pair
student["age"] = 23            # Updating an existing key
print(student)

#Removing
del student["age"]  # Removes a specific key
print(student)

age = student.pop("age", "Not Found")  # Removes key and returns value (default: "Not Found")
print(age)


#Loop through Dictionary
for key in student:
    print(key, ":", student[key])

# Using items() to get both key and value
for key, value in student.items():
    print(key, "->", value)

#Dictionary Method

                    #Methods
                    #keys():Returns a list of all keys
                    #values():Returns a list of all values
                    #items():Returns a list of key-value pairs
                    #update():Merges another dictionary
                    #clear():Removes all items

print(student.keys())     
print(student.values())   
print(student.items())    # Output: dict_items([('name', 'Tariq'), ('course', 'Computer Science')])


#Nested Dictionary

students = {
    1: {"name": "Tariq", "age": 22},
    2: {"name": "Zaheer", "age": 21}
}

print(students[1]["name"])  # Output: Tariq

#Dictionary Comphrension
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
