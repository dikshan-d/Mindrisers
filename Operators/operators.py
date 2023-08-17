# Arithmetic operators
# Addition operators
a = 'Hello'
b = 'World'

c = [2,3]
d = [2.3,2]

print(a + b)

print(c + d)

# Subtraction operator
a = 21.2
b = 21

print(a - b)

# Multiply operator
a = 23
b = 2

print(a * b)

# Division operator
a = 20
b = 2

c = a / b

print(c)

# Floor operator
a = 20
b = 3

print(a // b)

#floor Operators 
# a = 20
# b = 3
# print(a//b) #gives output above point 20/3 3*6 18 it gives 6

# Exponential operator
a = 3
b = 2

print(a ** b)

# Modulus operator
a = 20
b = 2

print(a % b)

# Assignment Operator
# save operator in new variable and print
 #Addition Assignment Operator
# a = 2
# b =  2
# a +=2
# print(a)

a = 'Hello'

print(a)

# Add assignment operator
a = 2
b = 3

a += b
print(a)

# Subtract assingment operator
a = 2
b = 3
a -= b

print(a)

# Multiply assignment operator

a = 20
b = 2

a *= b

print(a)

# Division assignment operator
a = 30
b = 3

a /= b

print(a)

# Floor assignment operator
a = 20 
b = 2

a //= b

print(a)

# Exponential assignment operator
a = 2
b = 3

a **= b

print(a)

# Modulus assignment operator
a = 20
b = 2

a %= b
print(a)

#Comparision Operators
#Greater Than
a = 2
b = 5
print(a>b)

 # Less Than
a = 3
b = 4
print(a<b)

#Greater Than
a = 5
b = 5
print(a==b)

#Not is Equal to
a = 5
b = 6
print(a!=b)

#Greater than or Equal to
a = 5
b = 4
print(a>=b)
 
#Less than or Equal tp
a = 6
b = 4
print(a<=b)

#Logical Operator

#And Logical Operator
a = 2
b = 3
c = 4
d = 5

e= (a>b) and (c<d)
print(e)

#OR Logical Operator
a = 2
b = 3
c = 4
d = 5

e= (a>b) or (c<d)
print(e)

# Not operator

a = 2
b = 3
c = 4
d = 5

e= not(a<b or c<d)
print(e)

# Membership operator
# In Operator
a = "Hello"
b = "Hello World"
c = b in a
print(c)

# Not in Operator
a = "Hello"
b = "Hello World"
c = b not in a
print(c)

#Identity Operator
#Is Operator
a = 'Hello'
b = 'Hello'
c = a is b
print(c)

#Is Not Operator
a = 'Hello'
b = 'Hello'
c = a is not b
print(c)

#Bitwise Operator
#And Bit Wise Operator
a = 2
b = 4
c = a & b
print(c)

#OR Bitwise Operator
a = 2
b = 4
c = a | b
print(c)

#Invert Bitwise Operator
a = 2
b = ~a
print(b)

#Shift right bitwise operator
a = 2
b = a >> 2
print(b)

#Shiftleft bitwise operator
a = 2
b = a << 2
print(b)

#XOR bitwise operator
a = 3
b = 2
c = a ^ b
print(c)