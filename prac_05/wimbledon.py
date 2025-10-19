from __future__ import annotations
import csv
from collections import OrderedDict
from pathlib import Path


def read_records(filename: str) -> list[dict]:

    records: list[dict] = []
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {filename}")

    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = [name.strip() if name is not None else "" for name in reader.fieldnames or []]
        norm_map = {name.lower(): name for name in fieldnames}
        champion_col = norm_map.get("champion", "Champion")
        country_candidate_cols = ["country.1", "champion country", "country"]
        champion_country_col = next((norm_map[c] for c in country_candidate_cols if c in norm_map), None)

        if champion_country_col is None:
            # If still not found, use the last column as a last resort
            champion_country_col = fieldnames[-1] if fieldnames else None

        for row in reader:
            if not row:
                continue
            champion = (row.get(champion_col, "") or "").strip()
            champ_country = (row.get(champion_country_col, "") or "").strip()
            if champion:
                records.append({"champion": champion, "country": champ_country})
    return records


def tally_wins(records: list[dict]) -> dict[str, int]:
    wins: "OrderedDict[str, int]" = OrderedDict()
    for rec in records:
        name = rec["champion"]
        wins[name] = wins.get(name, 0) + 1
    return wins


def extract_countries(records: list[dict]) -> set[str]:
    countries: set[str] = set()
    for rec in records:
        c = rec["country"].strip()
        if c:
            countries.add(c)
    return countries


def format_countries(countries: set[str]) -> str:
    return ", ".join(sorted(countries))


def display_results(win_counts: dict[str, int], countries_str: str) -> None:
    print("Wimbledon Champions:\n")
    for name, count in win_counts.items():
        print(f"{name} {count}")
    print("\nThese {} countries have won Wimbledon:\n{}".format(len(set(countries_str.split(', '))) if countries_str else 0, countries_str))


def main() -> None:
    filename = "wimbledon.csv"
    records = read_records(filename)
    win_counts = tally_wins(records)
    countries = extract_countries(records)
    countries_str = format_countries(countries)
    display_results(win_counts, countries_str)


if __name__ == "__main__":
    main()