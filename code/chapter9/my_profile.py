from user import User
from admin import Admin

my_profile = User("Simon", "Henry", 16, "Male", "Bago, Myanmar")

my_profile.describe_user()

my_admin = Admin("Simon", "Henry", 16, "Male", "Bago, Myanmar")

my_admin.describe_user()
my_admin.privileges.show_privileges()