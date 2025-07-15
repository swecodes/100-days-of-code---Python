# pizza
print("welcome to pizza deliveries")
size = input("what pizza size do you want? S, M OR L?")
pepperoni = input("Do you want pepperoni on your piza? Y or N?")
extra_cheese = input("Do you want extra cheese Y or N")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("wrong size entered!")

if pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3

if extra_cheese == "Y":
    bill += 1


print(f"your final bill is ${bill}")
