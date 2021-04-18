"""Guitar class"""


class Guitar:
    """Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a car instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Print parameters of guitar"""
        return"{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of guitar"""
        return 2021 - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= 50