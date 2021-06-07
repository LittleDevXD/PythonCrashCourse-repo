from time import time


class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} provides the best {self.cuisine} dishes.")

    def open_restaurant(self):
        print(f"{self.name} always opens.")

    def update_number_served(self, number_served):
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("You can't reduce the number.")

    def increase_number_served(self, increment):
        if increment >= 0:
            self.number_served += increment
        else:
            print("You can't reduce the number.")

class IceCreamStand(Restaurant):
    def __init__(self,name, cuisine):
        super().__init__(name, cuisine)
        self.flavour = ["Strawberry", "Blueberry", "Chocolate", "Milk", "Tea"]

    def show_flavour(self):
        print("~~~These favours are avaiable at IceCream Stand~~~")
        for flavour in self.flavour:
            print(f"- {flavour}")

