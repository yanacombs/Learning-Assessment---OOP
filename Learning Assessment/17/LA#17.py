class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
   
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name}!")
        print(f"{self.name} deals {self.attack_power} damage")
        print(f"{target.name} now has only {target.health}")
       
    def heal(self, amount):
        heal.health += amount
       
   
judea = Player("Judea", 100, 20)
angel = Player("Angel", 100, 10)


while judea.health > 0 and angel.health > 0:
   
    judea.attack(angel)
    if angel.health <= 0:
        print(f"====={judea.name.upper()} won the game!=====")
        break
    angel.attack(judea)
    if judea.health <= 0:
        print(f"====={angel.name.upper()} won the game!=====")
        break
