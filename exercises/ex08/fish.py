"""File to define Fish class."""


class Fish:
    """Class to represent Fish in the river."""
    
    age: int

    def __init__(self):
        """Fish constructor."""
        self.age = 0
        return None
    
    def one_day(self) -> None:
        """Increase age by 1."""
        self.age += 1
        return None