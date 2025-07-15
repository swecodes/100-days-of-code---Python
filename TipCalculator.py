print("Welcome to the tip calculator")
total_bill = float(input("Enter your total bill amount $"))
tip =int(input("How much tip would you like to give? 10 15 20 "))
tip_as_percent = tip/100
total_tip_amount = total_bill * tip_as_percent
total_bill += total_tip_amount
split = int(input("How many people to split the bill? "))
split_per_person = total_bill/split
final_amount = round(split_per_person,2)
#each_pay =round(((total_bill + tip) /split),2)

print(f"Each person should pay ${final_amount}")
