import json

with open('favourite_number.json') as f:
    print(f"Your favourite number is {json.load(f)}")