class Privileges:
    def __init__(self):
        self.privileges = ["can kick members", "can ban members", 
                           "can do anouncements", "can change rules"]
                    
    def show_privileges(self):
        print("~~~Here are an Admin authorithy~~~")
        for privilege in self.privileges:
            print(f"- {privilege}")
