"""Guitar class testing"""

from prac_06.guitar import Guitar


def run_tests():
    """Run test on guitar class"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another guitar", 2013, 0)
    print(gibson)
    print(another_guitar)
    print("Gibson L-5 CES get_age() - Expected 99. Got {}"
          .format(gibson.get_age()))
    print("Another Guitar get_age() - Expected 8. Got {}"
          .format(another_guitar.get_age()))
    print("Gibson L-5 CES is_vintage() - Expected True. Got {}"
          .format(gibson.is_vintage()))
    print("Another Guitar is_vintage() - Expected False. Got {}"
          .format(another_guitar.is_vintage()))


if __name__ == '__main__':
    run_tests()