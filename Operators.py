#Types of Operator
#An Operator is a symbol that performs a certain operation between operands
#Arithmetic (+,-,*,/,%, **)
#Relation/ Comparision  (==, !=, >, <, >=,<=)
#Assignment  (=, +=,-=, *=, /=, %=, **=)
# Logical (not, and , or)

#Arithmetic Operator
a=7; b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #Remainder
print(a**b) # a ^ b
# Realtional Operator
print(a==b)# false
print(a!=b)# True
print(a>b)# True
print(a<b)# false
print(a>=b)# True
print(a<=b)# false
#Assignment
a+=6
print(a)
a-=6
print(a)
a*=6
print(a)
a/=6
print(a)
a%=6
print(a)
a**=6
print(a)

#Logical
print(not False)
print(not (a>b))
print(not(not (a>b)))
Pakistan=True
Sindh=False
China=True
print("ans , Both are Countries  ", Pakistan and Sindh)# False
print("ans , Both are Countries  ", Pakistan and China)# True