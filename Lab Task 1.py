'''
#1)Arithmetic Operations:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)
'''
'''
#2)Area & Perimeter:

# Rectangle
a = int(input("Enter length:"))
b = int(input("Enter width:"))
print("Rectangle Area:", a * b)
print("Rectangle Perimeter:", 2 * (a + b))

# Square
a = int(input("Enter side:"))
print("Square Area:", a * a)
print("Square Perimeter:", 4 * a)

# Circle
pi=3.14
a = int(input("Enter radius:"))
print("Circle Area:",  pi * a * a)
print("Circle Perimeter:", 2 * pi * a)
'''
'''
#3)Average of Three Numbers:

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

avg = (a + b + c) / 3
print("Average: ", avg)
'''
'''
#4)Comparison Program :

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

# Equal
if a == b:
    print("Both numbers are equal")

# Greater
if a > b:
    print("a is greater than b")

# Less or equal
if a <= b:
    print("a is less than or equal to b")
'''
'''
#5)Square root:

import math
num = int(input("Enter number: "))
print("Square root:", math.sqrt(num))
'''
'''
#6)Simple Interest & Compound Interest:

p = int(input("Enter principal:"))
r = int(input("Enter rate:"))
t = int(input("Enter time:"))

# Simple Interest
s = (p * r * t) / 100
print("Simple Interest:",s)

# Compound Interest
c = p * (1 + r/100) ** t - p
print("Compound Interest:",c)
'''
'''
#7)Assignment Operators:

x = 10

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 4
print("x /= 4:", x)

x %= 2
print("x %= 2:", x)

x **= 3
print("x **= 3:", x)
'''
'''
#8)Swapping Arithmetic Operator:

a = int(input("Enter a:"))
b = int(input("Enter b:"))
a = a+b
b = a-b
a = a-b
print("After swapping:")
print("a =",a)
print("b =",b)
'''
'''
#9)Username & Password Check:

user =  input("Enter a username:" )
passw = input("Enter a password:")

if user =="Mirthu" and passw =='1234':
    print("Login Successfully")
else:
    print("Incorrect")
'''
'''
#10)Cube Root:
    
num = int(input("Enter number: "))
cube_root = num ** (1/3)
print(cube_root)
'''
