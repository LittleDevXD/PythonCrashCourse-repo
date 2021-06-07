#Invitation Letter
def invitation(people, message):
	for i in range(len(people)):
		print(f"{people[i]}, {message}")

def number_of_people(people):
	return f"{len(people)} people are invited"

# People to invite
people = ["Elon Musk", "Steve Job", "MkBHD"]

# First Invitaion
invitation(people, "Let's have a dinner together.")

#Steve Job can't come to the party
print(f"\n{people.pop(1)} can't come to the party.\n")

people.append("Bill Gates")

# Second Invitation
invitation(people, "Come to my Party!!!")
print(number_of_people(people))

# Bought a bigger table
print("\nGood news! I bought a bigger table.\n")

people.insert(0, "Einstein")
people.insert(2, "Nicolas Tesla")
people.append("Zuckerberg")

# Third invitation
invitation(people, "Please come to my party.")
print(number_of_people(people))

# The table won't reach in time
print("\nSorry guys! The table won't reach in time: T_T\n")

people.remove("Einstein")
people.pop()
del people[-1]
people.pop()

# Fourth invitation
invitation(people, "You are still invited!")
print(number_of_people(people))


