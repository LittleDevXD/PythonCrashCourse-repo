class Employee:
    def __init__(self, f_name, l_name, annual_salary):
        self.f_name = f_name
        self.l_name = l_name
        self.annual_salary = int(annual_salary)

    def get_raise(self, amount=5000):
        self.annual_salary += amount