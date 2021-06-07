def user_profile(f_name, l_name, **user_info):
    user_info["first name"] = f_name
    user_info["last name"] = l_name

    return user_info

my_profile = user_profile("Simon", "Henry", age="16", location="Myanmar")

print(my_profile)