pizzas = ["Hawaii", "Double cheese", "Sea food"]

for pizza in pizzas:
    print(pizza)
    print(f"I love {pizza}")

print("\nI really love pizza.")

#Copying the list
my_pizza = pizzas[:]

pizzas.append("Vegetable")
my_pizza.append("Spicy")

print(f"My friend's favourite pizza: {pizzas}")
print(f"My favourite pizzas: {my_pizza}")
