animals = ["Dog", "Cat", "Parrot"]

for animal in animals:
    print(animal)

print("\n")

for i in range(len(animals)):
    if i == 0:
        print(f"{animals[i]} would guard your house.")
    elif i == 1:
        print(f"{animals[i]} would bring lucks.")
    else:
        print(f"{animals[i]} would give you pleasure.")

print("\nAll these animals would make a great pet.")