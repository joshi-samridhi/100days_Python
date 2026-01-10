student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


# way one of doing sum
# total_sum = sum(student_scores)
# print(total_sum)

# Doing sum with for

''' 
sum = 0
for i in student_scores:
    sum +=i
print(sum)
'''

#  Maximum
# total_sum = max(student_scores)
# print(total_sum)

Max =0
for i in student_scores:
    if i> Max:
       Max= i
print(Max)