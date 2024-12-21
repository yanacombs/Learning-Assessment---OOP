class Ml_hero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        print(f"{self.name} is a/an {self.role} hero.")

mm = Ml_hero("Judea", "Marksman")
assassin = Ml_hero("Haya", "Assassin")

mm.describe()
assassin.describe()
