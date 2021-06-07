people = ["khant", "henry", "peter", "harry", "strinky", "elon"]

favourite_languages = {
    "khant" : "Java",
    "henry" : "Python",
    "peter" : "C",
    "elon" : "BrainSuck"
}

for person in people:
    if person in favourite_languages.keys():
        print(f"{person.title()}, Thank you for taking the poll.")
    else:
        print(f"{person.title()}, Please take the poll.")