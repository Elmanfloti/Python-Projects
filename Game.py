class Player:
    def __init__(self, name, health, score, damage):
        self.name = name
        self.health = health
        self.score = score
        self.damage = damage
    def take_damage(self, amount):
        self.health -= amount
    def heal(self, amount):
        self.health += amount
    def dmg(self, enemy, damage):
        enemy.health -= damage
    def status(self):
        print(f"{self.name} has {self.health} health and {self.score} score.")
    def save(self):
        with open("save.txt", "w") as file:
            file.write(f"{self.name} / {self.health} / {self.score}")

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def attack(self, player):
        player.health -= self.damage

player = Player(input("Enter your name: "), 100, 0, 20)

def kill(player, enemy):
    if player.health <= 0:
        player.health = 0
        print("GAME OVER!")
    elif enemy.health <= 0:
        enemy.health = 0
        player.score += 50
        player.health += 20
        print(f"{player.name} killed {enemy.name}! +50 score!")

def fight(player, enemy):
    while enemy.health > 0 and player.health > 0:
        player.dmg(enemy, 30)
        enemy.attack(player)
    kill(player, enemy)
    if player.health > 0:
        player.status()

enemy1 = Enemy("Goblin", 90, 20)
enemy2 = Enemy("Orc", 80, 30)
enemy3 = Enemy("Dragon", 120, 50)

fight(player, enemy1)
if player.health > 0:
    fight(player, enemy2)
if player.health > 0:
    fight(player, enemy3)
player.save()