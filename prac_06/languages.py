
from programming_language import ProgrammingLanguage
""" Estimate: 3 hours
    Actual: 2 hours """
def main():

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the object to validate the __str__ method
    print(python)

    # Add python, ruby, visual_basic languages in a list
    languages = [python, ruby, visual_basic]

    # Display  dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()