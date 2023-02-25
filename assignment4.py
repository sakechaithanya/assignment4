#1q Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument
x=int(input('enter the number :'))
a = lambda i : i+25
print(a(x))

# 2q Write a Python program to triple all numbers of a given list of integers. Use Python map.
lis=[]
n=int(input('enter the number:'))
for i in range(1,n):
    lis.append(i)
def triple(y):
    return 3*y
result=list(map(triple,lis))
print(result)
