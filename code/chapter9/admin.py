from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, f_name, l_name, age, gender, address):
        super().__init__(f_name, l_name, age, gender, address)
        self.privileges = Privileges()
