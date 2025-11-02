class ProgrammingLanguage:
    """ Class ProgrammingLanguage provides information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """ This returns name of ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"