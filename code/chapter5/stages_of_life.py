person_age = int(input("Your age: "))

if person_age < 2:
    print("Baby")
elif person_age < 4:
    print("Toddler")
elif person_age < 13:
    print("Kid")  
elif person_age < 20:
    print("Teenager")  
elif person_age < 65:
    print("Adult")
else:
    print("Elder")

