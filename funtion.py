# import math
'''
print("ceil value :", math.ceil(15.23))  # always give high range
# print("ceil value :", math.floor(15.23))  always give low range
print("ceil value :", round(15.23))     # It will compare whether its graeter than 5 or nor 

'''

'''
# Cube of number
print(9**3)      # ** is is to

# Square root
print("Square root : ", math.sqrt(64))
'''
# print("   INDIA   ")                         # Remove unwanted space
# print(str.strip("   INDIA   "))


# Making your own functions
# def fun_name(parameters):


#   !!!!!   This will not give any result as we have just defined it, you can run and check  !!!!!
# created function without giving parameters
'''
def add_num():
    a=12
    b=14
    c=a+b
    print("sum of 2 numbers is :", c)    
  
# Now to check the scope of the function we can CALL/INVOKE our function anywhere in code

print("sum:", add_num())     # !!! No Need To Give Any Value here, Just The Function
'''


# created function with parameters
'''
def add_num_par(x,y):
    z=x+y
    print("Parameter Sum ", z)

# Calling Function
add_num_par(15,16)            # You don't have to type print, it will automatically give you the result 31

'''


'''Write a Python program to create a calculator that can perform at least five
different mathematical operations such as addition, subtraction, multiplication,
division and average. Ensure that the program is user-friendly, prompting for input
and displaying the results clearly. '''

'''

def addtion(a,b):
    return a+b
    

def Subtraction(a,b):
    return a-b
      


num1 =int(input("Enter your First number "))    # if you will not convert this to int you will not get any answer as its a string
                                    #   TypeError: unsupported operand type(s) for -: 'str' and 'str'

num2 = int(input("Enter your Second number "))
output=int(input("Enter what function you want to perform\n 1.ADD\n 2.Subtraction\n 3.Multiplication\n 4.Division\n"))

'''
# Input type	Compare with
# int	1, 2, 3
# str	'1', '2' 

'''   # Therefore if(output=='1'): its worng as '1' it becomes string


if output==1:
   print(addtion(num1,num2))           #  DON'T WRITE PRINT STATMENT AS IN ABOVE DEF FUNCTION ALREADY WRITTEN

elif output==2:
   print(Subtraction(num1,num2))       #  DON'T WRITE PRINT STATMENT AS IN ABOVE DEF FUNCTION ALREADY WRITTEN

else:
    print("Invalid option")
'''

import pandas as pd
print(pd.__version__)