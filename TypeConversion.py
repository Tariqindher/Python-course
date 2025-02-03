# Type Conversion
#There are 2 type Conversion
#1. Conversion (Automatically)  easily 
#2. Casting (Manually) Not Easily

#Casting
a,b=1,2.0
sum=a+b

#Error
a,b=1,"2.0"
sum=a+b

#Type Casting
a,b=1,"2"
c=int(b)
sum=a+c

print(type(sum))