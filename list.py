'''list_name= ["Name", 1, 4, 18.5, "True"]
print(list_name)                            # Sting should be in double qoutes
print(list_name[3]) '''                 # Print perticular number

"""
list_name[start:stop:step]
list_name[start:stop] [:3] n-1
"""

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Slice from index 1 to 3 20,30,40
print(numbers)
# print(numbers[1:4])

# print(numbers[:3])   # 10, 20, 30 will be printed. As starting is not given it will start from 0, stop is 3 means n-1=2

# print(numbers[:: 3])    # stating will be from 0, then STOP not given then STEP 3 therefore, [10,40] will be printed.

# print(numbers[2::1])    #Staring from 30, 40,50,60

# print(numbers[2::3])    # Output [30, 60, 90]   3rd element will be printed

# print(numbers[:-1])   # Removed last elemt from the list

# print(numbers[::-1])   # REverse the list
# print(numbers[-1:-6:-1])   starting -1 is 100, stop -6 is 50("WHICH IS NOT INCLUDED") and step -1
                        #    Therefore output will be 100,90,80,70,60


# print(numbers[-1:-4])   # This will give you empty list as -1 is graeter than -4
print(numbers[-1:-6:-1])                        # print(numbers[-4:-1])   # This will give you 70,80,90


"""
Method	       Description                                         	Example
append(x)	    Adds item x to the end of the list	                   list.append(10)
insert(i, x) 	Inserts item x at position i	                         list.insert(1, 20)
remove(x)    	Removes the first occurrence of x	                     list.remove(3)
pop([i])    	Removes and returns item at index i,
              or last item if i not given	                           list.pop() or list.pop(2)
clear()	       Removes all items from the list	                     list.clear()
index(x)	     Returns the index of the first occurrence of x	       list.index(5)
count(x)	    Returns number of times x appears in the list	         list.count(2)
sort()	      Sorts the list in ascending order (modifies in place)	 list.sort()
sort(reverse=True)	Sorts the list in descending order	             list.sort(reverse=True)
sorted(list)	  Returns a new sorted list                            sorted(list)
reverse()	     Reverses the list in-place	                           list.reverse()


"""


'''
list1= [10, 20, 30, 40, 50]
list2= [60, 70, 80, 90, 100]

list1.append(60)                  # append will add 60 at the end of list1
# print("After append :", list1) 

print(list1 + list2)          # Concatenate two lists

list1.extend(list2)           # extend will add list2 elements to list1
'''

# create a list consisting of numbers between range 1 to 10
# list3= list(range(1,11))
# print("Original list :", list3)

'''
list1=[]
for i in range(1,11):
     list1.append(i)
print(list1)
'''


# create a list consisting of even 1 to 10
'''
list1=[]
for i in range(1,11):
    if i%2==0:
        list1.append(i)
print(list1)        
'''

# create a list consisting of ODD 1 to 10
'''
list1=[]
for i in range(1,11,2):
 list1.append(i)
print(list1) '''

# Just by a single line of code we can make a list

# Starting i is initializing the vale

# k = [i for i in range (1,11)]   # Focus on code i for i in range is written
# print(k)
'''
k = [i*i for i in range (1,11,2)]   # Square of even numbers  [1, 9, 25, 49, 81]
print(k)

k = [i+1 for i in range (1,11)]   # Square of even numbers  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(k)

k = [i for i in range (1,11) if i%2==0]   # Square of even numbers  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(k)
'''


'''


#         TUPLES
# Uppercase the element of list str.upper

country ="india"  # single quotes or double quotes doesn't matter
Upper_list= [str.upper(i) for i in country]
print(Upper_list)


# 1.	Using Parentheses ()
colors = ("red", "green", "blue")
print("colors=",colors)
numbers = (1, 2, 3, 4, 5)
print("numbers=",numbers)
mixed = (1, "hello", 3.14, True)
print("mixed list items=",mixed)
nested = (1, [2, 3], (4, 5, 6))
print("nested list =",nested)
# 2.	Without Parentheses (Comma-Separated) also_
numbers = 1, 2, 3, 4, 5
print(numbers)
# 3.	 Using the tuple() Constructor
new_tuple = tuple(("apple", "banana", "cherry"))
print(new_tuple)
 # use double brackets
list_items = ["x", "y", "z"]
# Creating a tuple from a list
tuple_items = tuple(list_items) # convert list to tuple
print(tuple_items)
# ('x', 'y', 'z’)
# 4.	Single-Item Tuple tuple
'''


# tuple1 = 7,        # Imporatnt!! In interview they will ask give a single value and show that its type is tuple
# print(type(tuple1))


# Add elemet in tuple using LIST
# tuple has (), List has []
# fiest make changes in list

'''
x = (1, 2, 3, 4)
t1 = list(x)    # Make it to list 
print(type(t1))

t1.append(5)
print(t1)
  # covert list to tuple
x=tuple(t1)
print(x)
'''

emp_details={
    'EmployeeId':[150,151,152],
    'EmployeeName':['Prakash','Atul','Rohan'],
    'Designation':['Sr.Sales Mgr','Lead Auditor','Server Admin']
    }
import pandas as pd

emp_df=pd.DataFrame(emp_details)
emp_df
