# Exercise 7

total_bill = float(input("Please enter your total bill >> "))
level_of_service = input("Please rate your level of service as, good, fair, or bad >> ")

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