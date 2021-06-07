people = [
    {"Henry" : {
        "name" : "Sitt Lin Htet",
        "age" : 17,
        "address" : "Bago"}
    },
    {"Harry" : {
        "name" : "Thet Paing Zaw",
        "age" : 17,
        "address" : "Bago"}
    },
    {"Shin Wai" : {
        "name" : "Soe Wai Yan Lin",
        "age" : 13,
        "address" : "Yangon"}
    }
]

for person in people:
    for name, info in person.items():
        print(f"{name}'s Informations: ")
        print(f"\tName : {info['name']}")
        print(f"\tAge : {info['age']}")
        print(f"\tAddress : {info['address']}")


dict = {"person" : "wtf", "etaf" : "ifur"}

print(dict['person'])