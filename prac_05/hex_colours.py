# Dictionary of 10 sample colours and their hex codes
COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

print("Available colours:", ", ".join(COLOUR_TO_HEX.keys()))

# Loop until the user enters a blank line
colour_name = input("Enter a colour name (or press Enter to quit): ").strip().title()
while colour_name != "":
    try:
        hex_code = COLOUR_TO_HEX[colour_name]
        print(f"{colour_name} has hex code {hex_code}")
    except KeyError:
        print("Invalid colour name")
    # Prompt again
    colour_name = input("Enter a colour name (or press Enter to quit): ").strip()
    # Have run the code for Black and Bisque