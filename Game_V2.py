import random
import json


#player abilities

class Player :
    def __init__(self,name, attack, health, level):
        self.name=name
        self.attack=attack
        self.health=health
        self.level= 1
        self.gold=0
        self.potions = 3
        self.inventory = []


    def attacks(self, attack, enemy):
        user_attack=input("what type of attack you want : [normal attack : 1 ] or [power attack : 2  ]\n").lower()
        if user_attack == "1":
            enemy.health -= self.attack
        elif user_attack == "2":
             enemy.health-= 2*self.attack
        else :
            print("sorry but you have just two abilities")


    def heal(self):
        if self.potions > 0:
            if self.health <= 50:
                user_heal=input(" do you want to use potion of heal")
                if user_heal == "yes":
                    self.health += 30
                    self.potions -= 1
                    print(f"you have {self.potions} potions left")
                if self.health > 100:
                    self.health = 100


    def kill(self, enemy, level):
        if enemy.health <= 0:
            enemy.health = 0
            self.level += 1
            number = random.randint(50, 100)
            self.gold += number
            self.attack += 10
            self.health = 100
            print(f"_________________________________________\n{self.name} has killed {enemy.name} and gain level up\n_________________________________________")


    def shop(self):
        items = {
            "1": ("Heal Potion Refill", 20),
            "2": ("Power Potion", 50),
            "3": ("Defense Potion", 50),
            "4": ("Leave", 0)
        }

        while True:
            print(f"you got {self.gold} gold")
            for key, (name, cost) in items.items():
                print(f"{key}. {name} - {cost} gold")

            user_buy = input("What do you want to buy from the shop? ")

            if user_buy in items:
                name, cost = items[user_buy]

                if user_buy == "4":
                    print("Leaving the shop.")
                    break

                if self.gold >= cost:
                    self.gold -= cost
                    self.inventory.append(name)
                    if user_buy == "1":
                        self.potions += 1
                    elif user_buy == "2":
                        self.attack += 10
                    elif user_buy == "3":
                        self.health += 20
                    print(f"You bought {name}!")
                else:
                    print("Not enough gold!")
            else:
                print("Invalid choice, please enter 1, 2, 3, or 4.")
    def status (self):
        print(f"{self.name} has {self.health} health left \nYour level is {self.level} and got {self.gold} gold \nYou got {self.inventory} in your inventory")


    def save(self):
        data = {
            "name": self.name,
            "health": self.health,
            "level": self.level,
            "attack": self.attack,
            "gold": self.gold,
            "potions": self.potions,
            "inventory": self.inventory
        }

        with open("save.json", "w") as file:
            json.dump(data, file)

    def load(self):
        try:
            with open("save.json", "r") as file:
                data = json.load(file)
                self.name = data["name"]
                self.health = data["health"]
                self.level = data["level"]
                self.attack = data["attack"]
                self.gold = data["gold"]
                self.potions = data["potions"]
                self.inventory = data["inventory"]
                self.status()
        except FileNotFoundError:
            print("No saved game found, starting fresh!")



#enemy abilities      


class Enemy :
    def __init__ (self,name, attack, health):
        self.name=name
        self.attack=attack
        self.health=health


    def attacks (self, attack, player):
        player.health-= self.attack


    def kill(self, player):
        if player.health <= 0:
            player.health = 0
            print("_____________\n  YOU DIED \n_____________    ")
            


player = Player(input("Enter your name: "), 10, 100, 1)

load_choice = input("Do you want to load your saved game? (yes/no) ")
if load_choice == "yes":
    player.load()

#Enemy 1
enemy1 = Enemy("Goblin", 10, 90)
while player.health > 0 and enemy1.health > 0:
    player.attacks(30, enemy1)
    if enemy1.health > 0:
        enemy1.attacks(20, player)
    print(f"{player.name}: {player.health} HP | {enemy1.name}: {max(0, enemy1.health)} HP")
player.kill(enemy1, 1)
enemy1.kill(player)

if player.health > 0:
    player.shop()

#Enemy 2
if player.health > 0:

    enemy2 = Enemy("Ork", 20, 200)
    while player.health > 0 and enemy2.health > 0:
        player.attacks(10, enemy2)
        if enemy2.health > 0:
            enemy2.attacks(20, player)
        print(f"{player.name}: {player.health} HP | {enemy2.name}: {max(0, enemy2.health)} HP")
    player.kill(enemy2, 1)
    enemy2.kill(player)

if player.health > 0:
    player.shop()

#Enemy 3
if player.health > 0:

    enemy3 = Enemy("Dragon", 50, 100)
    while player.health > 0 and enemy3.health > 0:
        player.attacks(10, enemy3)
        if enemy3.health > 0:
            enemy3.attacks(20, player)
        print(f"{player.name}: {player.health} HP | {enemy3.name}: {max(0, enemy3.health)} HP")
    player.kill(enemy3, 1)
    enemy3.kill(player)

player.status()
player.save()