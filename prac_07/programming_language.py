"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
Estimated time - 1 hour
"""
#Downloaded the programming_language.py file as per instruction in https://github.com/CP1404/Practicals/tree/master/prac_07
#template
class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int, pointer_arithmetic: bool):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def is_dynamic(self) -> bool:
        """Return True if the language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def has_pointer_arithmetic(self) -> bool:
        """Return True if the language supports pointer arithmetic."""
        return bool(self.pointer_arithmetic)

    def __str__(self) -> str:
        """Return a readable string for this language."""
        reflection_str = "Yes" if self.reflection else "No"
        ptr_str = "Yes" if self.pointer_arithmetic else "No"
        return (f"{self.name}, {self.typing} Typing, Reflection: {reflection_str}, "
                f"Pointer Arithmetic: {ptr_str}, First appeared: {self.year}")


def run_tests():
    """Basic sanity checks for ProgrammingLanguage."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    cplusplus = ProgrammingLanguage("C++", "Static", False, 1983, True)
    DotNet= ProgrammingLanguage(".NET", "Static", False, 2003, True)

    languages = [ruby, python, visual_basic, cplusplus,DotNet]
    # __str__ check
    print(python)
    # is_dynamic check
    dynamic_names = [lang.name for lang in languages if lang.is_dynamic()]
    print("Dynamically typed:", ", ".join(dynamic_names))
    # pointer arithmetic check
    ptr_langs = [lang.name for lang in languages if lang.has_pointer_arithmetic()]
    print("Pointer arithmetic:", ", ".join(ptr_langs))


if __name__ == "__main__":
    run_tests()