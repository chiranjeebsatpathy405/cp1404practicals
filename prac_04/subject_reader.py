FILENAME = "subject_data.txt"


def main():
    data = load_subject_details(FILENAME)
    display_subject_details(data)


def load_subject_details(filename):
    """Read data from file and return a list of [subject, lecturer, number_of_students]."""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            parts = line.strip().split(',')   # ['CP1401', 'Ada Lovelace', '192']
            parts[2] = int(parts[2])          # convert the number of students to int
            subjects.append(parts)
    return subjects


def display_subject_details(subjects):
    """Display subject details neatly."""
    for subject in subjects:
        code = subject[0]
        lecturer = subject[1]
        students = subject[2]
        print(f"{code} is taught by {lecturer} and has {students} students")


main()