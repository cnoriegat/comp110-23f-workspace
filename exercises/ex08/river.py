"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


__author__ = "730621572"


class River:
    """Class to represent River."""
    
    day: int
    bear: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove Fish with age > 3 and Bears with age > 5 from the River."""
        # Remove old Fish
        new_fish_list = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish_list.append(fish)
        self.fish = new_fish_list

        # Remove old Bears
        new_bears_list = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears_list.append(bear)
        self.bears = new_bears_list

        return None

    def bears_eating(self) -> None:
        """Bears eat 3 Fish each if at least 5 Fish are present in the River."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)

        return None
    
    def check_hunger(self) -> None:
        """If hunger_score < 0, then remove the Bear from the river."""
        hunger_list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                hunger_list.append(bear)
        self.bears = hunger_list
            
        return None
        
    def repopulate_fish(self) -> None:
        """Repopulate Fish in the River."""
        num_new_fish = (len(self.fish) // 2) * 4

        for fish in range(num_new_fish):
            new_fish = Fish()
            self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self) -> None:
        """Repopulate Bears in the River."""
        num_new_bears = len(self.bears) // 2

        for bear in range(num_new_bears):
            new_bear = Bear()
            self.bears.append(new_bear)

        return None
    
    def view_river(self) -> None:
        """Print the river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self) -> None:
        """Calls one_river_day 7 times."""
        for idx in range(7):
            self.one_river_day()
        return None
    
    def remove_fish(self, amount: int) -> None:
        """Remove amount many Fish from the River."""
        for fish in range(amount):
            self.fish.pop(0)
