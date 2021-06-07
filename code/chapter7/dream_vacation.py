poll = {}
print("Help me filling the poll!")
print("If you could visit one place in the world, what would it be?")
while True:
    name = input("\nWhat is your name? ")
    vacation = input("Where would you like to go? ")
    more = input("Would you like to add more people in the poll? (Y/n) ")

    poll[name] = vacation
    if more.lower() == 'n':
        break

print("\n~~~Here is the poll result~~~")
for name, place in poll.items():
    print(f"{name} would like to go {place}.")
