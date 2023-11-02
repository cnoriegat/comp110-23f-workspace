"""Defining a class, defining the pizzas."""

#Think of a class definition as a roadmap for objects that belong to the class. 
# You are defining the underlying structre every instance of this class will have.

class Pizza:
    """This is my class to represent pizza!"""

    # attributes
    # syntax <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
    """Constructor."""
    self.size = inp_size
    self.toppings = inp_toppings
    self.gluten_free = inp_gf
    # returns self for you

def price(self) -> float:
    """Method to compute price of pizza."""
    if self.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
        cost += .75 * self.toppings
    if self.gluten_free:
        cost += 1.00
    return cost
    
def add_topping(self, num_toppings: int):
    """Update existing pizza order with num_toppings."""
    self.toppings += num_toppings

def add_topping_new_order(self, num_toppings: int) -> Pizza:
    """"""
    
