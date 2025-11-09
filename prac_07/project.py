"""
# Estimated time - 1 hours
#Actual time taken - 1.5 hours

"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date

@dataclass(order=False)
class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percent."""
    name: str
    start_date: date
    priority: int
    cost_estimate: float
    completion: int  # 0..100

    def is_complete(self) -> bool:
        """Return True if the project is complete (100%)."""
        return self.completion >= 100

    def is_incomplete(self) -> bool:
        """Return True if the project is not yet complete."""
        return not self.is_complete()

    def starts_after(self, ref_date: date) -> bool:
        """Return True if the project starts after the given date."""
        return self.start_date > ref_date

    def __lt__(self, other: "Project") -> bool:
        """Define < comparison by priority (lower number = higher priority).

        This enables list.sort() / sorted() to order Projects by priority naturally.
        """
        if not isinstance(other, Project):
            return NotImplemented
        return self.priority < other.priority

    def __str__(self) -> str:
        """Return a human-friendly string for this project (matches sample style)."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion}%")
