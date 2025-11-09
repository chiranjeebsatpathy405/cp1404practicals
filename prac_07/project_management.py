import csv
from datetime import datetime, date
from pathlib import Path
from typing import List
from project import Project
# Estimated time - 4 hours
#Actual time taken - 5 hours

DEFAULT_FILE = "projects.txt"  # tab-delimited

MENU = (
    "(L)oad projects\n"
    "(S)ave projects\n"
    "(D)isplay projects\n"
    "(F)ilter projects by date\n"
    "(A)dd new project\n"
    "(U)pdate project\n"
    "(Q)uit"
)

# ------------- File I/O (SRP: one loader, one saver) -------------
def load_projects(path: str | Path) -> List[Project]:
    """Load projects from a tab-delimited file with header; return list of Project."""
    projects: List[Project] = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            project_name = row['Name'].strip()
            project_start_date = datetime.strptime(row['Start Date'].strip(), "%d/%m/%Y").date()
            project_priority = int(row['Priority'])
            project_cost_estimate = float(row['Cost Estimate'])
            project_completion = int(row['Completion Percentage'])
            projects.append(Project(project_name, project_start_date, project_priority, project_cost_estimate, project_completion))
    return projects


def save_projects(path: str | Path, projects: List[Project]) -> None:
    """Save projects to a tab-delimited file with header (overwrite)."""
    header = ['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage']
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header, delimiter='\t')
        writer.writeheader()
        for p in projects:
            writer.writerow({
                'Name': p.name,
                'Start Date': p.start_date.strftime('%d/%m/%Y'),
                'Priority': p.priority,
                'Cost Estimate': f"{p.cost_estimate}",
                'Completion Percentage': p.completion,
            })


# ------------- Display helpers -------------
def display_projects(projects: List[Project]) -> None:
    """Display incomplete and then completed projects"""
    incomplete = sorted([p for p in projects if p.is_incomplete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects: List[Project]) -> None:
    """Prompt user for a date; display projects starting after that date, sorted by start date."""
    project_date_str = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        project_ref_date = datetime.strptime(project_date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy.")
        return
    filtered = sorted([p for p in projects if p.starts_after(project_ref_date)], key=lambda p: p.start_date)
    for p in filtered:
        print(p)


def add_new_project(projects: List[Project]) -> None:
    """Prompt for fields and add a new project to the list."""
    print("Let's add a new project")
    project_name = input("Name: ").strip()
    project_start_str = input("Start date (dd/mm/yyyy): ").strip()
    try:
        project_start_date = datetime.strptime(project_start_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date; cancelling add.")
        return
    try:
        project_priority = int(input("Priority: ").strip())
        project_cost_estimate = float(input("Cost estimate: $ ").strip())
        project_completion = int(input("Percent complete: ").strip())
    except ValueError:
        print("Invalid number; cancelling add.")
        return
    projects.append(Project(project_name, project_start_date, project_priority, project_cost_estimate, project_completion))


def update_project(projects: List[Project]) -> None:
    """Choose a project by index; update completion and/or priority (blank to keep)."""
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        index = int(input("Project choice: ").strip())
        project = projects[index]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    print(project)
    percentage_str = input("New Percentage: ").strip()
    priority_str = input("New Priority: ").strip()
    if percentage_str:
        try:
            project.completion = int(percentage_str)
        except ValueError:
            print("Ignored invalid completion value.")
    if priority_str:
        try:
            project.priority = int(priority_str)
        except ValueError:
            print("Ignored invalid priority value.")


def prompt_load_existing(projects: List[Project]) -> List[Project]:
    """Prompt for a filename and return loaded projects from it."""
    filename = input("Filename to load from: ").strip()
    try:
        loaded = load_projects(filename)
        print(f"Loaded {len(loaded)} projects from {filename}")
        return loaded
    except FileNotFoundError:
        print("Project File not found.")
        return projects


def prompt_save(projects: List[Project]) -> None:
    """Prompt for a filename and save current projects to it."""
    filename = input("Filename to save to: ").strip()
    save_projects(filename, projects)
    print(f"Saved {len(projects)} projects to {filename}")


# ------------- Main menu loop -------------
def main():
    print("Welcome to Pythonic Project Management")
    # Load default file on start
    try:
        projects = load_projects(DEFAULT_FILE)
        print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    except FileNotFoundError:
        projects = []
        print("No default file found; starting with empty project list.")

    while True:
        print(MENU)
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            projects = prompt_load_existing(projects)
        elif choice == 's':
            prompt_save(projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            ans = input(f"Would you like to save to {DEFAULT_FILE}? (y/n): ").strip().lower()
            if ans.startswith('y'):
                save_projects(DEFAULT_FILE, projects)
                print(f"Saved {len(projects)} projects to {DEFAULT_FILE}")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
