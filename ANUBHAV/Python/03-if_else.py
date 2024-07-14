word1 = "Anubhav"
word2 = "Mishra"

#! Syntax 
'''
if condition:
    print("For true")
elif condition:
    print("For tre condition)
else:
    print("For false") '''

#? print "Yes" if word1 is equal to word2 or print "No"

if word1 == word2:
    print("Yes")
else:
    print("No")
    
#? print "No. is even " if given no. is even or print "No. is odd also check whehter the given num is 1 or not"

n = 1

if n % 2 == 0:
    print("No. is even ")
elif n == 1:
    print("Num is 1")
else:
    print("No. is odd")
    
    
#! Test 


#? print whether the given no. is odd or not 
# also take input from user add a msg
# Use != operator
n = int(input("Enter a num: "))
if n % 2 != 0:
    print("Num is odd")
else:
    print("Num is even")
    

#? print whether the string input from user is same or not 
#? print "Yes" if true and print "No" if false

name1 = input("Enter a name : ")
name2 = input("Enter a name2 :")

if name1 == name2:
    print("Yes")
else:
    print("No")
    print("Noob")

