# Exercise 10
num_coins = 0
ques = input("do you want a coin? ")
while ques == "yes":
    print(f"You have {num_coins} coins.")
    num_coins += 1
    ques = input("do you want a coin? ")
