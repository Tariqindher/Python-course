
#Basic Try_Except
try:
                    result=10/0
except ZeroDivisionError:
        print("Cannot divide by zero!")


#Catching Multiple Exception
try: 
        number=int("abc")
        numbers=10/0
except (ValueError, ZeroDivisionError) as e:
        print(f"An error occurred: {e}")


#Using else  with Try Except
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")

#Finally
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This block always runs.")

#Catching All Exception
try:
    x = 10 / 0
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#Raising Exception Manually
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print(e)

#Custom Exception
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)


#Nested Try_Except
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner exception: division by zero.")
        raise  # Re-raise the exception to outer block
except Exception as e:
    print(f"Outer exception caught: {e}")