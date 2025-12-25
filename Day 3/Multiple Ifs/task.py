print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill += 5
    elif age <= 18:
        print("Please pay $7.")
        bill += 7
    else:
        print("Please pay $12.")
        bill += 12
    take_photo = input("Do you want to take photographs? 'Y for yes and N for no?' ")
    if take_photo == "Y" or take_photo == "y":
        print("Please pay $3.")
        bill += 9
        print(f"The total bill is ${bill}")
    else:
        print(f"The total bill is ${bill}")


else:
    print("Sorry you have to grow taller before you can ride.")



