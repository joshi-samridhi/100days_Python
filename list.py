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