import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Setting up the class to save lines of codes in test func"""
        self.employee = Employee("Simon", "Henry", 200_000)

    def test_ordinary_value(self):
        """Not Passing the amount argument"""
        self.employee.get_raise()
        self.assertEqual(self.employee.annual_salary, 205_000)
    
    def test_custom_value(self):
        """Passing the amount argument"""
        self.employee.get_raise(100_000)
        self.assertEqual(self.employee.annual_salary, 300_000)
        print(self.employee.annual_salary)

if __name__ == "__main__":
    unittest.main()