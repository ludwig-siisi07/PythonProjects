#BMI CALCULATOR
print("Welcome to the BMI Calculator!")
#USER INPUTS
weight = float(input("What is your weight ? "))
height = float(input("What is your height ? "))
bmi = round((weight / (height**2)), 2)
print(f"Your BMI is: {bmi:.2f}kg/m^2")
