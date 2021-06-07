pet_1 = {"name" : "Bob", "owner" : "Grandma"}
pet_2 = {"name" : "Milo", "owner" : "GumGum"}
pet_3 = {"name" : "Sky", "owner" : "Phil"}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Name : {pet['name']}")
    print(f"Owner: {pet['owner']}")