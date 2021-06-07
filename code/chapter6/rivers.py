rivers = ["areawady", "niles", "thanlwin", "amazon", "bago"]

rivers_dict = {
    "areawady" : "Myanmar",
    "niles" : "Egypt",
    "thanlwin" : "China",
    "amazon" : "Amazon",
    "bago" : "Bago"
}

for key, value in rivers_dict.items():
    if key in rivers:
        print(f"{key.title()} flows through {value}")