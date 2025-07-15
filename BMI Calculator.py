#bmi = weight/(height)**2
def bmi_calculator(weight,height):
    bmi = weight/(height ** 2)
    return bmi

weight = float (input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters:"))

result= bmi_calculator(weight,height)
print("Your BMI is",result)

if result < 18.5:
    print("you are underweight")
elif 18.5 <= result >= 24.9:
    print("you have a normal weight")
elif 25<= result >=29.9:
    print("you are overweight")
else:
    print("you are obese")
