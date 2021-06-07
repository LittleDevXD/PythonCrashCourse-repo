import json

file = "username.json"

def get_username(file_name):
    username = input("Enter your username: ")
    with open(file_name, 'w') as f:
        json.dump(username, f)
        print(f"We will remember you as {username} when your come back!")

try:
    with open('username.json') as f:
        name = json.load(f)
except:
    get_username(file)
else:
    yours = input(f"Is your username {name}? ")
    if yours.lower() == 'y':
        print(f"Welcome back, {name}!")
    else: 
        get_username(file)




        