class Ml_hero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.name} is a/an {self.role} hero."

    def __str__(self):
        return f"{self.name} is a/an {self.role} hero."
mm = Ml_hero("Layla", "Marksman")
assassin = Ml_hero("Hayabusa", "Assassin")

print(mm.name)
print(mm.role)
print(mm)
print(assassin.name)
print(assassin.role)
print(assassin)
