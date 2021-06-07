import json

try:
    with open('favourite_number.json') as f:
        num = json.load(f)
except:
    num = int(input("What is your favourite number? "))
    with open('favourite_number.json', 'w') as f:
        json.dump(num, f)
        print(f"We will remember your favourite number, {num}")
else: 
    print(f"Your favourite number is {num}.")