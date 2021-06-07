# Parent Class
class User:
    def __init__(self, f_name, l_name, age, gender, address):
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.age = age
        self.address = address
        self.gender = gender
        self.full_name = self.f_name + " " + self.l_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full Name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.address}")

    def greet_user(self):
        print(f"Hello, welcome back {self.f_name}")

    def login(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Admin class inheritted from User class
# Using a separate class for admin privileges

