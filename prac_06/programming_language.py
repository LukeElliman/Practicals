

class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection="", year=0):
        """Represent information about a programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage"""
        return"{}, Typing {}, Reflection {}, Year {}".format(self.name, self.typing,
                                                             self.reflection,
                                                             self.year)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        return False
