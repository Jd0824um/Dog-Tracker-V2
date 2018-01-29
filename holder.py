class Holder:
    CATCHES = 0

    # Constructor for creating a record holder
    def __init__(self, name, country, catches=CATCHES):
        self.name = name
        self.country = country
        self.catches = catches

    # To string method to formats and prints out the holders information
    def __str__(self):
        template = 'Name: {} Country: {} Number of Catches: {}'
        return template.format(self.name, self.country, self.catches)
