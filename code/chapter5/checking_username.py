current_users = ["elon", "einstein", "newton", "bill", "tesla", "gumgum"]
new_users = ["eren", "henry", "harry", "bill", "gumgum"]

for user in new_users:
    if user.lower() in current_users:
        print(f"Username {user.title()} is in use. Choose another one.")
    else:
        print(f"Username {user.title()} is available.")