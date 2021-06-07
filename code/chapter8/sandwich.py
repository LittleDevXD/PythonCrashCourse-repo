def make_sandwich(*sandwiches):
    print("The following sandwiches are being made: ")
    for sandwich in sandwiches:
        print(f"- {sandwich}")

make_sandwich("vegetable", "meat", "poop")