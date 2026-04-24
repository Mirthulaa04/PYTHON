'''
#1)Chect whether a number is even or odd
s=int(input("Enter your no:"))
def num(s):
    if s%2==0:
        print("Even no")
    else:
        print("Odd no")
num(s)
'''
'''
#2)Find the maximum of two numbers
a=int(input("Enter your first no:"))
b=int(input("Enter your second no:"))
def no(a,b):
    if a>b:
        print("a is max")
    else:
        print("b is max")
no(a,b)
'''
'''
#3)Calculate the factorial number
n=int(input("Enter your number"))
def fac(n):
    m=1
    for i in range(1,n+1):
        m*=i
    print(m)
fac(n)
'''
'''
#4)Sum of element in a list
def sum():
    sum=0
    for i in range(11):
        sum+=i
    print("the sum=",sum)
sum()
'''
'''
#6)Reverse string
n=("Malayalam")
def reverse(n):
    print(n[::-1])
reverse(n)
'''
'''
#7)Check whether a number is prime
n=int(input("Enter your no:"))
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("Not a prime no")
            break
        else:
            print("Prime no")
prime(n)
'''

      

