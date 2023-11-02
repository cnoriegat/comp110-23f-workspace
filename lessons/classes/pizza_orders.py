"""We actually make the pizzas."""


# This is where we instantiate the class we defined in classes.py. //
# In other words, we're creating objects that belong to that class.

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # Constructor

# print("Size: ")
# print(my_Pizza.size)

# print("my_pizza: ")
# print(my_Pizza)

# print("Pizza class: ")
# print(Pizza)

# Make sals_pizza size medium, five toppings, not gluten free

sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """Compute the price of a Pizza."""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings

    if input_pizza.gluten_free:
        cost += 1.00
    
    return cost

# Calling function
print(price(my_pizza))
print(price(sals_pizza))

# Calling method
print(my_pizza.price())
