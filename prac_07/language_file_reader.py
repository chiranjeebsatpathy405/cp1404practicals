"""
CP1404/CP5632 Practical
# Estimated time - 1 hour
# Actual time taken - 2 hours
"""

import csv
from programming_language import ProgrammingLanguage
def read_languages(csv_path: str):
    """Read languages from CSV and return a list of ProgrammingLanguage objects."""
    languages = []
    #print("I am here")
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Language'].strip()
            #print(name)
            typing = row['Typing'].strip()
           # print(typing)
            # Allow 'Yes'/'No' or 'True'/'False'
            reflection = row['Reflection'].strip().lower() in ("yes", "true", "1")
           # print(reflection)
            year = int(row['Year'])
            pointer_arithmetic = row['PointerArithmetic'].strip().lower() in ("yes", "true", "1")
            languages.append(ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic))
        return languages

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


def main():
    """Client code to demonstrate reading and simple queries."""
    csv_path = 'languages.csv'
    languages = read_languages(csv_path)
    print("In Main")
    print(languages)
    print("All languages:")
    for lang in languages:
        print(" -", lang)

    print("\nDynamically typed languages:")
    for lang in languages:
        if lang.is_dynamic():
            print(" -", lang.name)

    print("\nLanguages with pointer arithmetic:")
    for lang in languages:
        if lang.has_pointer_arithmetic():
            print(" -", lang.name)


if __name__ == '__main__':
    main()
