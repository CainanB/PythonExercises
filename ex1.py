# Python Exercise 1

name = input("What is your name? ")
print(f"Hello, {name}")

# Exercise 2 
name = input("What is your name? ")
name_length = len(name)
greeting = f"Hello, {name}! your name has {name_length} letters in it! awesome!"
print(greeting.upper())

# Exercise 3

name = input("Insert a Name >> ")
num = input("Insert a number")
greeting = f"""{name} is an amazing developer,
he has {num} projects in his portfolio.
"""
print(greeting)

# Exercise 4

day = int(input("Day (0-6)? "))
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednsday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")

# Exercise 5

day = int(input("Day (0-6)? "))
if day > 0 and day < 6:
    print("Go to work")
else:
    print("Sleep in")

# Exercise 6

deg_cels = int(input("Please enter a degree in Celsius >> "))
deg_fah = deg_cels * 1.8 + 32
print(deg_fah)

# Exercise 7

total_bill = float(input("Please enter your total bill"))
level_of_service = input("Please rate your level of service as, good, fair, or bad")

if level_of_service.lower() == "good":
    tip_amount = .20
    total = total_bill * tip_amount + total_bill
    print("{:.2f}".format(total))
elif level_of_service.lower() == "fair":
    tip_amount = .15
    total = total_bill * tip_amount + total_bill
    print("{:.2f}".format(total))
elif level_of_service.lower() == "bad":
    tip_amount = .10
    total = total_bill * tip_amount + total_bill
    print("{:.2f}".format(total))
else:
    print("Please enter an appropriate answer")

# Exercise 8

total_bill = float(input("Please enter your total bill"))
level_of_service = input("Please rate your level of service as, good, fair, or bad")
split_ways = int(input("How many ways would you like the bill split? "))
if level_of_service.lower() == "good":
    tip_amount = .20
    total = total_bill * tip_amount + total_bill
    amount_per_person = total / split_ways
    print("{:.2f}".format(total), "{:.2f}".format(amount_per_person))
elif level_of_service.lower() == "fair":
    tip_amount = .15
    total = total_bill * tip_amount + total_bill
    amount_per_person = total / split_ways
    print("{:.2f}".format(total), "{:.2f}".format(amount_per_person))
elif level_of_service.lower() == "bad":
    tip_amount = .10
    total = total_bill * tip_amount + total_bill
    amount_per_person = total / split_ways
    print("{:.2f}".format(total), "{:.2f}".format(amount_per_person))
else:
    print("Please enter an appropriate answer")

# Exercise 9

num = 1

while(num <= 10):
    print(num)
    num += 1

# Exercise 10
num_coins = 0
ques = input("do you want a coin? ")
while ques == "yes":
    print(f"You have {num_coins} coins.")
    num_coins += 1
    ques = input("do you want a coin? ")
