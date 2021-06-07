cities = {
    "Bago" : {
        "country" : "Myanmar",
        "population" : "2M",
        "fact" : "This cities produced a lot of heroes who gave their lives for Democracy in Spring Revolution"
    },
    "New York" : {
        "country" : "United States",
        "population": "5M",
        "fact" : "A well developed city with lots of high tech things."
    }, 
    "Heroshima" : {
        "country" : "Japan",
        "population" : "1k",
        "fact" : "One of the two cities where American denoded the Nuclear Bomb in WWII"
    }
}

for city, infos in cities.items():
    print(f"The information of {city}: ")
    for key, value in infos.items():
        print(f"\t{key.title()} : {value}")