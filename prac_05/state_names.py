CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

for code in ["NSW", "QLD", "NT", "WA", "ACT", "VIC", "TAS", "SA", "XYZ"]:
    try:
        # Try to get the state name
        name = CODE_TO_NAME[code]
        print(f"{code:<3} is {name}")
    except KeyError:
        # Handle missing key
        print(f"{code:<3} is Unknown")

