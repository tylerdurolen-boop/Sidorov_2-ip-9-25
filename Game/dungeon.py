"""Герой, враги, бой и цены рудника. Случайного врага выбирает game.py."""

prices = {"potion": 10, "torch oil": 15, "war elixir": 40}

enemy_stats = {
    "skeleton": {"hp": 45, "damage": 6, "loot": 25},
    "drowned miner": {"hp": 30, "damage": 4, "loot": 15},
    "cave spider": {"hp": 20, "damage": 3, "loot": 10},
    "pale bat": {"hp": 12, "damage": 2, "loot": 5},
}


class Hero:
    """Хранит характеристики и текущее состояние героя."""

    def __init__(self, name, health, strength, agility, endurance):
        """Задаёт характеристики и вычисляет урон и стартовый запас сил."""
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.damage = 10 + strength * 1.5
        self.crit_damage = self.damage * 2
        self.stamina = health // 10 + endurance

    def __str__(self):
        """Возвращает однострочный формуляр героя."""
        return f"{self.name}: health {self.health}, damage {self.damage:.1f}, stamina {self.stamina}"

    def strike(self, n):
        """Возвращает (урон, крит): каждый третий удар критический."""
        if n % 3 == 0:
            return self.crit_damage, True
        return self.damage, False

    def spend_stamina(self, cost):
        """Тратит силы, затем здоровье; возвращает признак истощения."""
        if self.stamina >= cost:
            self.stamina -= cost
            return False
        self.health -= cost - self.stamina
        self.stamina = 0
        return True

    def heal(self, amount, cap):
        """Лечит в пределах cap; возвращает None."""
        self.health = min(self.health + amount, cap)

    def to_dict(self):
        """Возвращает характеристики и состояние для JSON, ничего не меняет."""
        return {
            "name": self.name,
            "health": self.health,
            "stamina": self.stamina,
            "strength": self.strength,
            "agility": self.agility,
            "endurance": self.endurance,
        }

    @staticmethod
    def from_dict(data):
        """Создаёт героя из словаря, восстанавливая текущий запас сил."""
        hero = Hero(data["name"], data["health"], data["strength"],
                    data["agility"], data["endurance"])
        hero.stamina = data["stamina"]
        return hero


class Enemy:
    """Рабочая копия карточки врага на один бой."""

    def __init__(self, name, stats):
        """Берёт hp, damage и loot из карточки; начинает пустой журнал боя."""
        self.name = name
        self.hp = float(stats["hp"])
        self.damage = stats["damage"]
        self.loot = stats["loot"]
        self.rounds = []


def fight(enemy, hero, bonus=0):
    """Печатает бой; возвращает (rounds, won, loot), меняет обоих участников.

    bonus по умолчанию 0, прибавляется после критического удвоения.
    Карточка Enemy содержит hp, damage, loot. Прерванный бой продолжает
    enemy.rounds: завершённые раунды сохраняются вместе с участниками.
    """
    if not enemy.rounds:
        print(f"You descend the stairs. Out of the darkness comes {enemy.name}!")
    while enemy.hp > 0 and hero.health > 0:
        round_n = len(enemy.rounds) + 1
        hit, crit = hero.strike(round_n)
        hit += bonus
        enemy.hp -= hit
        line = f"Round {round_n}: hero deals {hit:.1f}"
        if crit:
            line += " — critical!"
        if enemy.hp <= 0:
            blow = 0
            line += " Enemy falls."
        else:
            blow = enemy.damage
            hero.health -= blow
            line += f" {enemy.name} health: {enemy.hp:.1f}. {enemy.name} hits for {blow}."
        enemy.rounds.append([round_n, hit, blow])
        print(line)
    won = enemy.hp <= 0
    return enemy.rounds, won, enemy.loot if won else 0


def buy(price, gold, quantity=1):
    """Возвращает (gold_left, ok) для quantity покупок, по умолчанию одной.

    Не меняет переданные значения и ничего не печатает.
    """
    if quantity <= 0:
        return gold, False
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


if __name__ == "__main__":
    hero = Hero("Tester", 100, 7, 5, 4)
    enemy = Enemy("skeleton", enemy_stats["skeleton"])
    rounds, won, loot = fight(enemy, hero)
    print(f"self-test: {len(rounds)} rounds, won={won}, loot={loot}")
