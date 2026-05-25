import random
from abc import ABC, abstractmethod

class Game:
    def __init__(self):
        self.player = Player("Knight")
        self.enemy = Enemy("Goblin")
        self.battle = BattleSystem(self.player, self.enemy)

    def start(self):
        print("=== Arena RPG ===")
        self.battle.start_battle()

class BaseCharacter(ABC):
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.abilities = []

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def is_alive(self):
        return self.hp > 0

    @abstractmethod
    def take_turn(self, opponent):
        """Każda klasa implementuje własną turę"""
        pass

class Ability(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def use(self, caster, target):
        pass

class Attack(Ability):
    def __init__(self):
        super().__init__("Attack")

    def use(self, caster, target):
        base = caster.attack - target.defense
        dmg = max(0, base + random.randint(-2, 5))
        target.take_damage(dmg)
        return f"{caster.name} deals {dmg} damage!"

class Heal(Ability):
    def __init__(self):
        super().__init__("Heal")

    def use(self, caster, target):
        target.heal(10)
        return f"{caster.name} restores 10 HP!"

class Player(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, hp=90, attack=20, defense=5)
        self.abilities = [Attack(), Heal()]

    def show_status(self, opponent):
        print(f"{self.name} HP: {self.hp}/{self.max_hp}")
        print(f"{opponent.name} HP: {opponent.hp}/{opponent.max_hp}")

    def take_turn(self, opponent):
        print("\nYour turn:")
        self.show_status(opponent)
        for i, ability in enumerate(self.abilities):
            print(f"{i+1}. {ability.name}")

        while True:
            choice = input("Choose action: ")

            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(self.abilities):
                    return self.abilities[idx].use(self, opponent)

            print("Invalid input")

class Enemy(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=37, defense=2)
        self.abilities = [Attack(), Heal()]
        self.heal_used = False

    def take_turn(self, opponent):
        LOW_HP_THRESHOLD = 0.3

        if self.hp < self.max_hp * LOW_HP_THRESHOLD and not self.heal_used:
            ability = self.abilities[1]
            self.heal_used = True
        else:
            ability = self.abilities[0]

        return ability.use(self, opponent)


class BattleSystem:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        while self.player.is_alive() and self.enemy.is_alive():

            print(self.player.take_turn(self.enemy))
            if not self.enemy.is_alive():
                break

            print(self.enemy.take_turn(self.player))

        self.end_battle()

    def end_battle(self):
        if self.player.is_alive():
            print("\nYou win!")
        else:
            print("\nYou lose!")



if __name__ == "__main__":
    game = Game()
    game.start()