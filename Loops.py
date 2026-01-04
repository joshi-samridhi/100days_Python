# Program 1, for while loop (increment)
'''
x=1
while x<=10:      MULTI LINE COMMENT
 print(x)
 x=x+1
'''

# Program 2, for while loop (decrement) 

'''
x=10
while x>=1:
    print(x)
    x=x-1
'''

# Program 3, WAP to print even numbers rang from 1-50
'''
x= 1
while x<=50:
    if(x%2==0):
        print(x)
    x=x+1          # Take care of the indentation
'''

    # For LOOP

# for i in range(3, 10,2):         #range(starting value, stopping value, stepping value)
#    print(i)                    # i is automatically assign to 0

'''   
country = "India"    
print(country)

for i in country:  # in range() will not come
   print(i)

'''
'''
for i in range(6):             #break Statment
  if i==3:              # if postion i ==3, then it will STOP the loop
   break
  print(i)
'''

for i in range(10):
    if i==6:            # Except 6 all will be printed
        continue
    print(i)