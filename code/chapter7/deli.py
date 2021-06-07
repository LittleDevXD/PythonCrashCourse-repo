sandwiches = []
finished_sandwiches = []

print("Deli is out of pastrami.")

while True:
    sandwich = input("Order a sandwich: ")
    if sandwich.lower() == "pastrami":
        print("Out of pastrami.")
    else:
        repeat = input("Would you like to add more (Y/n): ")
        if repeat.lower() == 'n':
            sandwiches.append(sandwich)
            break
        else:
            sandwiches.append(sandwich)

print("\n~~~Finishing your order~~~")
while sandwiches:
    finished_sandwiches.append(sandwiches.pop())

for sandwich in finished_sandwiches:
    print(f"Made {sandwich} sandwich.")