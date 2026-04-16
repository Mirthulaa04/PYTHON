'''
#1)Check whether a list is palindrome

word=input("Enter your word:")
s=""
for i in word:
    s=i+s
print(s)
if s==word:
    print("It is a palindrome")
else:
    print("Not a palindrome")
'''
'''
#2)Split a list into even and odd

l=[0,1,2,3,4,5,6,7,8,9,10]
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd,even)
'''
'''
#3)Merge two lists and remove duplicate

l=[90,91,92,93,94,95,99]
l.extend([96,97,98,99,100])
print(l)
l.remove(99)
print(l)
'''
