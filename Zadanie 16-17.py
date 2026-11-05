class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

x = int(input())
y = int(input())
point = Point(x, y)
print(point.x)
print(point.y)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

x = int(input())
y = int(input())
dx = int(input())
dy = int(input())
point = Point(x, y)
point.shift(dx, dy)
print(point.x)
print(point.y)

class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def dec(self):
        self.count -= 1

    def value(self):
        return self.count

counter = Counter()
for i in range(3):
    command = input()
    if command == "inc":
        counter.inc()
    elif command == "dec":
        counter.dec()
    elif command == "value":
        print(counter.value())

class Potion:
    def __init__(self, name, price, heal):
        self.name = name
        self.price = price
        self.heal = heal

    def describe(self):
        return f"{self.name}: {self.price} gold, +{self.heal} health"

name = input()
price = int(input())
heal = int(input())
potion = Potion(name, price, heal)
print(potion.describe())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = int(input())
points = []
for i in range(n):
    x = int(input())
    y = int(input())
    points.append(Point(x, y))
best = max(points, key=lambda point: point.x)
print(best.x)
print(best.y)

class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, name, qty):
        self.items[name] = self.items.get(name, 0) + qty

    def total(self):
        return sum(self.items.values())

inventory = Inventory()
for i in range(3):
    name = input()
    quantity = int(input())
    inventory.add(name, quantity)
print(inventory.total())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

x = int(input())
y = int(input())
point = Point(x, y)
print(point)

class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self):
        return {"name": self.name, "health": self.health, "damage": self.damage}

    @staticmethod
    def from_dict(data):
        return Hero(data["name"], data["health"], data["damage"])

name = input()
health = int(input())
damage = float(input())
hero = Hero(name, health, damage)
data = hero.to_dict()
restored = Hero.from_dict(data)
print(restored.health)
