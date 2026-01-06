weight = float(input("Enter your weight : "))
height = float(input("Enter your height :"))

bmi = weight/(height**2)
# print("your BMI is ", bmi)     
# print(f"Your BMI is {bmi}")

print(f"Your BMI is {bmi:.2f}")   # best way to write.


if bmi < 18.5:
    print("underweight")

elif bmi>=18.5 and bmi<25 :
   print("normal weight")

else:
    print("overweight")
