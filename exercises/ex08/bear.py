"""File to define Bear class."""


class Bear:
    """Class to represent Bears in the river."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Bear constructor."""
        self.age = 0
        self.hunger_score = 0

        return None
    
    def one_day(self) -> None:
        """Increase age and decrease hunger by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None: 
        """Update Bear hunger_score so that it increases by num_fish."""
        self.hunger_score += num_fish
        return None