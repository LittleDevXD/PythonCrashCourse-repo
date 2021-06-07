class Car:
    def __init__(self, model, manufacturer, time):
        self.model = model.title()
        self.manufacturer = manufacturer.title()
        self.time = time

    def describe_car(self):
        print(f"{self.manufacturer} {self.model} {self.time}")
    
    def show_gas_tank(self):
        print("Gas Tank")

class ElectricCar(Car):
    def __init__(self, model, manufacturer, time):
        super().__init__(model, manufacturer, time)
        self.battery = Battery()

    def show_gas_tank(self):
        print("Are you stupid? (Yes or No)")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        self.range = 216

    def show_battery(self):
        print(f"This car has {self.battery_size}-kwh battery.")

    def get_range(self):
        print(f"This car can go {self.range} miles on full charge.")

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            self.range = 350
        else:
            print("Battery is already upgraded.")

my_tesla = ElectricCar("model y", "tesla", "2020")

my_tesla.describe_car()
my_tesla.battery.show_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

my_tesla.battery.show_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()


