#1q Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument
x=int(input('enter the number :'))
a = lambda i : i+25
print(a(x))

# 2q Write a Python program to triple all numbers of a given list of integers. Use Python map.
lis=[]
n=int(input('enter the number:'))
for i in range(0,n):
    value1=int(input('enter the value:'))
    lis.append(value1)
def triple(y):
    return 3*y
result=list(map(triple,lis))
print(result)

#3q Write a Python program to square the elements of a list using map() function.

def square(z):
    return z*z
lis1=[]
num=int(input('enter the number:'))
for i in range(0,num):
    value=int(input('enter the value:'))
    lis1.append(value)
output=list(map(square,lis1))    
print(output)
