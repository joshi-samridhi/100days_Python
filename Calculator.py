# This program helps to do Maths Calculation

a= float(input("Enter your First Number "))
b = float(input("Enter your Second Number "))

print("First Number = " ,  a)
print("Second Number = ",  b)

c= str(input("Enter Operant: + , - , *, / , % "))
print("You want to perform",  c)

if(c=='+'):
    print("Sum of your selected number is ", a+b)
elif(c=='-'):
    print("Subtraction of your selected number is ", a-b)
elif(c=='*'):
    print("Multiplication of your selected number is ", a*b)
elif(c=='%'):
    print("Modulus of your selected number is ", a%b)
elif(c=='/'):
    print("Division of your selected number is ", a/b)

else:
    print("You have selected worng operant among the given")