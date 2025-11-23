class Band:
    """The class Band has a list of Musicians."""
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def add(self, musician):
        """Musician added to the band."""
        self.musicians.append(musician)

    def play(self):
        """ musician to play their instrument."""
        for musician in self.musicians:
            result = musician.play()
            print(result)
