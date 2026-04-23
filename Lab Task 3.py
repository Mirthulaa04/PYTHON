'''
#1) Find the sum of first N natural no

sum=0
for i in range (1,10):
    sum+=i
print("sum=",sum)
'''
'''
#2) Check whether a no is palindrome

n=int(input("Enter your no:"))
t=n
r=0
while t>0:
    d=t%10
    r=r*10+d
    t//=10
if r==n:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
'''
#3) Print multiplication table of a no

t=int(input("Enter your no:"))
for i in range(1,11):
    print(i,"*",t,"=",i*t)
'''
'''
#4) Count digits in a no

n=int(input("Enter your digits:"))
count=0
t=n
while t>0:
    d=t%10
    count+=1
    t//=10
print(count)
'''
'''
#5) Find factorial of a no

mul=1
for i in range (1,10):
    mul*=i
print("mul=",mul)
'''
'''
#6) Check whether a no is prime

n=int(input("Enter your no:"))
if n<0:
    print("not a prime no")
else:
    for i in range(2,n):
        if n%i==0:
            print("not a prime no")
            break
    else:
        print("prime no")
'''
'''
#7) Check whether a word is a palindrome

word=input("Enter your word:")
reversed == word[: :-1]
if reversed == word:
    print("It is a palindrome")
else:
    print("Not a palindrome")
'''
