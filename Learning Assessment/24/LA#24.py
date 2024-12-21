from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass
   
class Warrior(GameCharacter):
    def attack(self):
        print("Swing sword")

class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball")

class Archer(GameCharacter):
    def attack(self):
        print("Shoot an arrow")

class Healer(GameCharacter):
    def attack(self):
        print("Casts healing spell on ally!")


josua = Warrior()
reinalyn = Mage()
omi = Archer()
gia = Healer()
josua.attack()
reinalyn.attack()
omi.attack()
gia.attack()
