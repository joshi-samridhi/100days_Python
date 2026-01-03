# Assign grade based on score >80 A grade, 60 and <80 B grade 50 > and than 60 C grade 

a= int(input("Enter your marks : "))
print("Your marks is : ", a)

if(a>=80):
    print("Congratulation your grade is A ")

elif(a<80 and a>=60):
    print("Good,your grade is B" )

elif(a<60 and a>=40):
    print("Ok, Your grade is C ")

elif(a<40 and a>=33):
    print("Bad, your grade is D ")

else:
    print("FAIL, your grade is F")


