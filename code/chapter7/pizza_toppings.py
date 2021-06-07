print("Enter the toppings you would like to add.")
print("(If you are finished just enter 'quit')")

available_topping = ["cheese", "extra cheese", "spice", "tomato", "pepper", "sea food"]
topping_list = []

while True:
    topping = input("Your topping: ")

    if topping.lower() == "quit":
        print(f"Here are your toppings \n{topping_list}.")
        break
    else:
        if topping.lower() in available_topping:
            print(f"{topping} is added.")
            topping_list.append(topping)
        else:
            print(f"{topping} is not available")