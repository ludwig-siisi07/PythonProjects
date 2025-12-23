print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
#arithmetic
bill_per_person = (100*bill + bill*tip)/(100*people)
print(f"Each person should pay: {bill_per_person:.2f}")