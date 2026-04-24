'''
#1)chect whether a number is even or odd
s=int(input("Enter your no:"))
def num(s):
    if s%2==0:
        print("even no")
    else:
        print("odd no")
num(s)
'''
'''
#2)find the maximum of two numbers
a=int(input("enter your first no:"))
b=int(input("enter your second no:"))
def no(a,b):
    if a>b:
        print("a is max")
    else:
        print("b is max")
no(a,b)
'''
'''
#3)calculate the factorial number
n=int(input("Enter your number"))
def fac(n):
    m=1
    for i in range(1,n+1):
        m*=i
    print(m)
fac(n)
'''
'''
#4)sum of element in a list

for i in range(1,10):
    def num(i):
        sum=0
        sum+=i
print("sum=",sum)
num(i)
'''

'''
#6)reverse string
n=("harini suresh")
def reverse(n):
    print(n[::-1])
reverse(n)
'''
'''

#7)check whether a number is prime
n=int(input("enter your no:"))
def prime(n):
    if n<0:
        print("not a prime no")
    
    else:
        for i in range(2,n):
            if n%i==0:
                print("not a prime no")
                break
            else:
                print("prime no")
prime(n)
'''


      

