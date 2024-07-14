
#* print your name after storing it in a varaible "name"

#! string : "", '', f''
word = "anubhav"
print(word)
print('name = ', word)
print(f"name = {word}")

#! print the sum of two numbers after taking input from user

#! default input : string

s = 0
a = int(input("Enter a num:"))
b = int(input("Enter a num:"))
# a, b = map(int, input().split())
s = a + b
print(f"Sum = {s}")

#! Data Type
# 1. int
# 2. float
# 3. string
# 4. bool 

#! Basic Operators

# :- +, -, *, /, %


num1 = 7
num2 = 2

#! / for simple division
#! "//" for value to its floor (used as math.floor)
print(num1//num2)


#? % operator is used to find the remainder
num1 = 5
num2 = 2

print(num1%num2)

#! "str" function 

num = 4.3
word = str(num)
print(word)
print(type(word))




#! Test  

#! print multiplication of two no., take input from users
#! use f string and also add a message in input and ouput

s = 1
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
s = a * b
print(f"Result : {s} ")

#! print your name, by taking two input from user(first name, last name and print them all at once)

name1 = input("Enter your first name:")
name2 = input("Enter your last name:")
#! s = name1 + " " + name2
#! print(f"Full name: {s}")

print(f"Full name : {name1} {name2}")


#! In f string we dont use any operation we just write a variable in it 
#name all the data type
"""int,float,str,bool"""

#Take all the data type input from user and print the, with proper message
n= int(input("Enter a NO ="))
print(f"result ={n}")

n= float(input("Enter a NO ="))
print(f"RESULT = {n}")

word= str(input("Enter a Name= "))
print(f"name = {word}")

s= True
print(f"{s}")