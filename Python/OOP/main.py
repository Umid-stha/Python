from character import character

hero=character(name='hero', health=100)
enemy=character(name='enemy', health=100)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f'Health of {hero.name}:{hero.health}')
    print(f'Health of {enemy.name}:{enemy.health}')

    input()