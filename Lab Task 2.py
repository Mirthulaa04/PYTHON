'''
#1) check wheather a positive

a=int(input("Enter a no:"))
if a>0:
    print("positive no")
else:
    print("negative no")
'''
'''
#2) check whether a no divisible by 5

a=int(input("Enter a no:"))
if a%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")
'''
'''
#3) check whether a person eligible to vote

age=int(input("Enter your age:"))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
'''
'''
#4) check whether a no is even or odd

a=int(input("Enter a no:"))
if a%2==0:
    print("even no")
else:
    print("odd no")
'''
'''
#5) find the largest of two no

a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))
if a>b:
    print("a is largest no")
else:
    print("b is largest no")
'''
'''
#6) check whether a year is leap year or not

year=int(input("Enter the year:"))
if year%4==0:
    print("leap year")
else:
    print("non leap year")
'''
'''
#7) find the largest of three no

a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))
c=int(input("Enter the third no:"))
if a>b and a<c:
    print("a is the largest no")
elif b>a and b<c:
    print("b is the largest no")
else:
    print("c is the largest no")
'''
'''
#8) assign grades based on marks

mark=int(input("Enter your mark:"))
if mark>=35 and mark<=50:
    print("Grade:C")
elif mark>=51 and mark<=80:
    print("Grade:B")
elif mark>=81 and mark<=90:
    print("Grade:A")
elif mark>=91 and mark<=100:
    print("Grade:A+")
else:
    print("Fail!")
'''
'''
#9) check whether a character is vowel oe consonant

b=input("Enter a character")
if b in 'aeiou':
    print("b is a vowel")
else:
    print("b is a consonant")
'''
'''
#10) create a simple calculator

a=int(input("Enter a no:"))
operator=input("Enter your operator:")
b=int(input("Enter a no:"))
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
else:
    print("invalid error")
'''
'''
#11) check if a number is positive then check it is odd or even

a=int(input("Enter a no:"))
if a>0:
    print("positive no")
    if a%2==0:
        print("even no")
    else:
        print("odd no")
else:
    print("negative no")
'''
'''
#12) check login credentials

u=input("Enter username:")
p=int(input("Enter password:"))
if u=="Elsa":
    if p=="0405":
        print("Login")
    else:
        print("Incorrect password")
else:
    print("Invalid username")
'''
'''
#13) check whether a no divisible by both 3 and 7

a=int(input("Enter a no:"))
if a%3==0 and a%7==0:
    print("divisible by both 3 and 7")
else:
    print("not divisible by both 3 and 7")
'''
'''
#14) determine the type of triangle

a=int(input("Enter the side1 of triangle:"))
b=int(input("Enter the side2 of triangle:"))
c=int(input("Enter the side3 of triangle:"))
if a==b==c:
    print("Equilateral triangle")
elif a==b!=c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
'''
'''
#15) check whether a student passed all subjects and determine

a=int(input("Enter mark 1:"))
b=int(input("Enter mark 2:"))
c=int(input("Enter mark 3:"))
d=int(input("Enter mark 4:"))
if a>=35 and b>=35 and c>=35 and d>=35:
    print("Passed all subjects")

    avg = (a+b+c+d)/4

    if avg>=75:
        print("Distinction")
    else:
        print("No Distinction")
else:
    print("Fail")
'''



    

