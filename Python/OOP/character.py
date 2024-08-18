from weapons import fist

class character:
    def __init__(self, name:str, health:int) -> None:
        self.name=name
        self.health=health
        self.maxHealth=health

        self.weapon=fist

    def attack(self,target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)