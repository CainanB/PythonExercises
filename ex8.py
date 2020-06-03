# Exercise 8

total_bill = float(input("Please enter your total bill >> "))
level_of_service = input("Please rate your level of service as, good, fair, or bad >> ")
split_ways = int(input("How many ways would you like the bill split? "))
if level_of_service.lower() == "good":
    tip_amount = .20
    total = total_bill * tip_amount + total_bill
    amount_per_person = total / split_ways
    print("Your total is " + "${:.2f}".format(total), " and the amount per person is " + "${:.2f}".format(amount_per_person))
elif level_of_service.lower() == "fair":
    tip_amount = .15
    total = total_bill * tip_amount + total_bill
    amount_per_person = total / split_ways
    print("Your total is " + "${:.2f}".format(total), " and the amount per person is " + "${:.2f}".format(amount_per_person))
elif level_of_service.lower() == "bad":
    tip_amount = .10
    total = total_bill * tip_amount + total_bill
    amount_per_person = total / split_ways
    print("Your total is " + "${:.2f}".format(total), " and the amount per person is " + "${:.2f}".format(amount_per_person))
else:
    print("Please enter an appropriate answer")
