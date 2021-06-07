price = 0
print("Welcome to Dota Cinema!")
print("(If you are finished just enter 'quit')")
while True:
    tickets = int(input("How many tickets do you want? "))
    zero = 0
    while zero < tickets:
        age = int(input("Please tell me the ages: "))
        

        if age <= 3:
            price += 0
        elif age <= 12:
            price += 10
        else:
            price += 15


        zero += 1

    print(f"Here is your total price: {price}")
    break