alien = "red"
point = 0

if alien == "green":    
    point += 5
    print(f"You just earned {point} points.")
elif alien == "yellow":
    point += 10
    print(f"\nYou just earned {point} points.")
elif alien == "red":
    point += 15
    print(f"\nYou just earned {point} points.")

print(f"\nYour total point: {point}")