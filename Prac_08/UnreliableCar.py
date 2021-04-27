"""Unreliable Car Class"""

from Prac_08.cars import Car
from random import randint


class UnreliableCar(Car):
    """Specialized version of car class that includes reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialize an unreliable car instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Print values of unreliable car"""
        return f"{self.name}, {self.fuel}, {self.reliability}"

    def drive(self, distance):
        drive_chance = randint(0,100)
        if drive_chance >= self.reliability
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
