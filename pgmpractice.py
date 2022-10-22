# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
# a=645
# b=89
# c= a*b
# if c<=1000:
#     print(c)
# else:
#     c=a+b
#     print(c)
# to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number
# for i in range(0,10):
#     i=i+(i-1)
#     print(i)
# to accept a string from the user and display characters that are present at an even index number.
# str="pynative"
# c=len(str)
# for i in range(0,c,2):
#     print(str[i])              #1st
# print(str[0:8:2])               #2nd
# c=list(str)
# print(c)
# for i in c[0::2]:
#     print(i)
# to remove characters from a string starting from zero up to n and return a new string.
# c="i love yellow colour"
# x=c[4:]
# print(x)
# Check if the first and last number of a list is the same
# def numbercheck():
#     n1=l1[0]
#     n2=l1[-1]
#     if n1==n2:
#         print("true")
#     else:
#         print("false")
# l1=[10,20,30,40,50,10]
# numbercheck()
# iterate the given list of numbers and print only those numbers which are divisible by 5
# l1=[10, 20, 33, 46, 55]
# for i in l1:
#     if i%5==0:
#         print(i)
# to find how many times substring “Emma” appears in the given string
# st = "Emma is good developer. Emma is a writer"
# print(st.count("Emma"))
# Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for i in range(0,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
#  program to check if the given number is a palindrome number.
# a = "121"
# if a == a[::-1]:
#     print("palin")
# else:
#     print("not palin")   #1st method
# Given a two list of numbers, write a program to create a new list such that
# the new list should contain odd numbers from the first list and even numbers from the second list
# l1 = [10, 20, 25, 30, 35]
# l2 = [40, 45, 60, 75, 90]
# for i,j in l1,l2:
#     if (l1[i]%2==1):
#         l3.append(i)
# def TowerOfHanoi(n, source, destination, auxiliary):
#     if n == 1:
#         print("Move disk 1 from source", source, "to destination", destination)
#         return
#     TowerOfHanoi(n - 1, source, auxiliary, destination)
#     print("Move disk", n, "from source", source, "to destination", destination)
#     TowerOfHanoi(n - 1, auxiliary, destination, source)
# n = 4
# TowerOfHanoi(n, 'A', 'B', 'C')
# Print First 10 natural numbers using while loop
# i=1
# while i<11:
#     print(i)
#     i+=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# a = int(input("enter the number to find sum:"))
# b=0
# for i in range(1,a+1):
#      i = b+a           # printing tables
#      b=i
#      print(i)
# for i in range(1,a+1):
#     c=b+i
#     b=c
# print(c)
# x=sum(range(1,a+1))          #inbuilt fn
# print(x)
#print multiplication table of given number
# a = int(input("enter the number to find sum:"))
# b=0
# for i in range(1,10):
#      i = b+a           # printing tables
#      b=i
#      print(i)
# Count the total number of digits in a number
# num=12846566565456484563456
# x=0
# while num!=0:
#     num=num//10
#     x=x+1
#     print(x)
# pattern printing
# for i in range(1,6):
#     for j in range(6-i,0,-1):
#         print(j,end=" ")
#     print()
# l1=[10,20,30,40,50]
# a=len(l1)-1
# for i in range(a,-1,-1):
#     print(l1[i])
# Display numbers from -10 to -1 using for loop
# for i in range(-10,0,1):
#     print(i)
# Use else block to display a message “Done” after successful execution of for loop
# for i in range(1,5):
#     print(i)
# if i==0:
#     pass
# else:
#     print("Done")
# Write a program to display all prime numbers within a range
# a=int(input("enter starting number:"))
# b=int(input("enter ending number:"))
# for i in range(a,b+1):
#     if i>1:
#        for num in range(2,i):
#           if (i%num)==0:
#              print("not")
#           else:
#               print(i)
# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")
#
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#     else:
#         print(num)

# Fibbonacci series
# x=8
# a=0
# b=1
# for i in range(1,x+1):
#     print(a)
#     c = a + b
#     a=b
#     b=c
#
# factorial
# x=15
# a=1
# for i in range(1,x+1):
#     i=i*a
#     a=i
# print(i)

# class Nobel:



# for i in range(0,7):
     # if i!=3 and i!=6:
     #     print(i,end=" ")
     # if i==3 or i==6:
     #     continue
     # print(i)
# x=76542
# b=0
# while (x>1):
#     a=x%10
#     b=(b*10)+a
#     x = x//10
# print(b)

# datalist = [1452, 11.23, 1+2j, True, 'Python 3', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# for i in datalist:
#     print(i,type(i))
# for i in range(0,9):
#     for j in range(0,i+1):
#         if j>5:
#             for i in range(4,0,-1):
#                 print("*",end=" ")
#         else:
#            print("*",end=" ")
#     # for i in range(4,0,-1):
#     #     print("*", end=" ")
#     print()
# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(0,i-1):
#         print("*",end=" ")
#     print()
# l1=[]
# def square(n):
#     for i in range(1,n):
#           n= i**2
#           l1.append(n)
# square(10)
# print(l1)
# def calculation(a, b):
#     add=a+b
#     sub=a-b
#     return (add,sub)
# res = calculation(40,10)
# print(res)
# def show_employee(name,salary=9000):
#     print("Name:",name,"Salary:",salary)
# show_employee("Ben", 12000)
# show_employee("Jessa")

# def func1(*args):
#     for i in args:
#         print(i)
# func1(20,30,40)
# func1(80,100)
# TOWERS OF HANOI------------
# def tower(n,A,B,C):
#     if n==1:
#         print("moved %d from %s to %s"%(n,A,C))
#     else:
#         tower(n-1,A,B,C)
#         print("move %d from %s to %s"%(n,A,C))
#         tower(n-1,B,C,A)
# n=int(input("enter no of disc:"))
# tower(n,"A","B","C")
# print(dir(n))
# def fun():
#     return("hi")
# d=fun()
# print(d)
# def of():
#     task="de"
#     def ifu():
#         print(task)
#     return ifu()
# h=of()
# print(h)
# def rem(n):
# def div(a,b):
#     # if a<b:
#     #     a,b=b,a
#     print(a/b)
#     # return a/b
# def mydiv(func):
# class shape():
#     @abstract
#     def area(self):
#         pass
# obj=shape()
#     def infn():
#         if a<b:
#             a,b = b,a
#         return func()
#     return infn()
# # div(10,50)
# obj=mydiv(div(a,b))
# obj(4,8)
# print(obj)
# print(dir())


# create password
# a=0
# x = [4, 6, 8, 24, 12, 2]
# for i in x:
#     if i>a:
#         a=i
# print(a)

# for i in range(4,31,2):
#     print(i,end=" ")
# print()
# print(list(range(4,31,2)))
def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)