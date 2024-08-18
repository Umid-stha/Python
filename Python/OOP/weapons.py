class weapons:
    def __init__(self, name:str, type:str, damage:int, value:int) -> None:
        self.name=name
        self.type=type
        self.damage=damage
        self.value=value

sword=weapons('ironSword', 'sharp', 10, 15)
bow=weapons('bow', 'ranged', 13, 19)
fist= weapons('fist', 'melee', 3, 0)