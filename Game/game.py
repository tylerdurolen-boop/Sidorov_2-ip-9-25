"""Затопленный рудник, версия 1.0."""

import json
import os
import random
from pathlib import Path

import dungeon

try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

# Fore.CYAN, Fore.MAGENTA, Fore.BLUE; Style.BRIGHT, Style.DIM.
# Равные рекорды остаются в порядке появления; эликсиры дают +2 за штуку.

VERSION = "1.0"
TITLE = "DUNGEON: FLOODED MINE"
FRAME = "=" * (len(TITLE) + 6)
SAVE = Path(__file__).with_name("save.json")
STRIKES = 6

MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", ".", "S", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}
LOOT = {(1, 1): "miner's coin", (2, 3): "copper key", (1, 3): "blue crystal"}
num_to_verb = {
    "1": "look", "2": "go", "3": "rest", "4": "listen", "5": "torch",
    "6": "train", "7": "descend", "8": "leaders", "9": "shop",
    "10": "backpack", "11": "drink", "0": "exit",
}
commands = [
    "look", "go [north/south/west/east]", "rest", "listen", "torch", "train",
    "descend", "leaders", "shop", "backpack", "drink [item]",
    "buy <item> [count]", "map", "scout", "newgame", "exit",
]
MENU = [
    "What do you do? (number or command; help for help)",
    "1 - look around (look)",
    "2 - go forward (go)",
    "3 - rest (rest)",
    "4 - listen to the water (listen)",
    "5 - light a torch (torch)",
    "6 - train (train)",
    "7 - descend deeper (descend)",
    "8 - leaderboard (leaders)",
    "9 - shop (shop)",
    "10 - backpack (backpack)",
    "11 - drink potion (drink)",
    "map - show the mine", "scout - count reachable rooms",
    "newgame - remove the save for the next run",
    "0 - exit the dungeon (exit)",
]


def parse_command(line):
    """Возвращает (verb, words) после нормализации и перевода номера пункта."""
    command = line.strip().lower()
    words = command.split()
    if not words:
        return "", []
    return num_to_verb.get(command, words[0]), words


def new_run():
    """Читает имя и характеристики с проверкой; возвращает состояние забега."""
    print("What is the hero's name?")
    name = input()
    print(f"Welcome, {name}!")
    print("You enter the old mine. Water drips from the beams; rusty rails vanish below it.")
    print("Hero setup.")
    while True:
        print("Health (1-200), strength (0-20), agility and endurance (0-20), one per line:")
        try:
            health = int(input())
            strength = int(input())
            agility = int(input())
            endurance = int(input())
        except ValueError:
            print("Use whole numbers. Enter all four characteristics again.")
            continue
        try:
            if not 1 <= health <= 200:
                raise ValueError(f"Health {health} is outside 1-200")
            if not 0 <= strength <= 20:
                raise ValueError(f"Strength {strength} is outside 0-20")
            if not 0 <= agility <= 20 or not 0 <= endurance <= 20:
                raise ValueError("Agility and endurance must be between 0 and 20")
        except ValueError as error:
            print(f"{error}. Enter all four characteristics again.")
            continue
        break
    hero = dungeon.Hero(name, health, strength, agility, endurance)
    print(hero)
    return {
        "hero": hero, "max_health": hero.health, "max_stamina": hero.stamina,
        "gold": 0, "actions": 0, "ability_bonus": 0, "inventory": {},
        "enemies": list(dungeon.enemy_stats), "position": (3, 2),
        "visited": {(3, 2)}, "loot": set(), "log": [], "battle": None,
    }


def write_save(run):
    """Пишет весь забег и незаконченный бой в JSON; возвращает успех записи."""
    data = {
        "hero": run["hero"].to_dict(),
        "max_health": run["max_health"], "max_stamina": run["max_stamina"],
        "gold": run["gold"], "actions": run["actions"],
        "ability_bonus": run["ability_bonus"], "inventory": run["inventory"],
        "enemies": run["enemies"], "position": list(run["position"]),
        "visited": [list(position) for position in sorted(run["visited"])],
        "loot": sorted(run["loot"]), "log": run["log"], "battle": None,
    }
    if run["battle"] is not None:
        enemy = run["battle"]
        data["battle"] = {"name": enemy.name, "hp": enemy.hp, "rounds": enemy.rounds}
    try:
        with open(SAVE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Could not save progress: {error}.")
        return False
    return True


def load_save():
    """Предлагает продолжить забег; возвращает состояние или None при отказе."""
    if not SAVE.exists():
        return None
    print("A save was found. Continue the run? (yes/no)")
    answer = input().strip().lower()
    if answer not in ("yes", "да"):
        return None
    try:
        with open(SAVE, encoding="utf-8") as file:
            run = json.load(file)
        run["hero"] = dungeon.Hero.from_dict(run["hero"])
        run["position"] = tuple(run["position"])
        run["visited"] = {tuple(position) for position in run["visited"]}
        run["loot"] = set(run["loot"])
        for key in ("max_health", "max_stamina", "gold", "actions", "ability_bonus"):
            if not isinstance(run[key], (int, float)):
                raise ValueError("Invalid saved characteristic")
        if not isinstance(run["inventory"], dict) or not isinstance(run["log"], list):
            raise ValueError("Invalid saved inventory or journal")
        if any(name not in dungeon.enemy_stats for name in run["enemies"]):
            raise ValueError("Unknown saved enemy")
        row, column = run["position"]
        if not (0 <= row < len(MAP) and 0 <= column < len(MAP[row])) or MAP[row][column] == "#":
            raise ValueError("Invalid saved position")
        battle = run["battle"]
        if battle is not None:
            enemy = dungeon.Enemy(battle["name"], dungeon.enemy_stats[battle["name"]])
            enemy.hp = battle["hp"]
            enemy.rounds = battle["rounds"]
            run["battle"] = enemy
        if run["hero"].health <= 0:
            raise ValueError("The saved hero is dead")
    except (OSError, ValueError, KeyError, TypeError):
        print("The save cannot be read. Start a new run.")
        return None
    print(f"Run continued: health {run['hero'].health}, gold {run['gold']}, enemies left {len(run['enemies'])}.")
    return run


def scout(row, column, seen):
    """Рекурсивно считает доступные комнаты, меняет seen, ничего не печатает."""
    if (row, column) in seen or MAP[row][column] == "#":
        return 0
    seen.add((row, column))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(row + dr, column + dc, seen)
    return total


def print_leaderboard(log):
    """Печатает топ-3 и первый максимальный удар врага; возвращает None."""
    if not log:
        print("You haven't fought yet.")
        return
    top = sorted(log, key=lambda row: row[1], reverse=True)[:3]
    print("Leaderboard (hero damage):")
    for i, row in enumerate(top, 1):
        print(f"{i}. Round {row[0]}: {row[1]:.1f}")
    worst = max(log, key=lambda row: row[2])
    print(f"Strongest enemy hit: {worst[2]} (round {worst[0]}).")


def print_run_summary(log):
    """Печатает суммарный и средний урон, безопасно для пустого журнала."""
    total = sum(row[1] for row in log)
    rounds = len(log)
    average = total / rounds if rounds else 0
    print(f"Damage: {total:.1f} across {rounds} rounds, average {average:.1f}.")


def print_state(run):
    """Печатает текущее состояние зелёным при наличии colorama."""
    hero = run["hero"]
    state = f"Health: {hero.health} Stamina: {hero.stamina} Enemies left: {len(run['enemies'])} Gold: {run['gold']}"
    print(Fore.GREEN + state + Style.RESET_ALL if COLOR else state)


def battle(run):
    """Начинает или продолжает бой, переносит журнал и трофеи в забег."""
    if run["battle"] is None:
        if not run["enemies"]:
            print("You descend the stairs. But the dungeon is empty.")
            return
        name = random.choice(run["enemies"])
        run["battle"] = dungeon.Enemy(name, dungeon.enemy_stats[name])
    enemy = run["battle"]
    rounds, won, loot = dungeon.fight(enemy, run["hero"], bonus=run["ability_bonus"])
    run["log"].extend(rounds)
    if won:
        run["gold"] += loot
        run["enemies"].remove(enemy.name)
        line = f"{enemy.name} defeated! {len(run['enemies'])} enemies left in the dungeon. Loot: {loot} gold."
        print(Fore.CYAN + line + Style.RESET_ALL if COLOR else line)
    print(f"Battle: {len(rounds)} rounds.")
    run["battle"] = None


def purchase(run, words):
    """Покупает предмет из команды, возвращает признак состоявшегося действия."""
    quantity = 1
    item_words = words[1:]
    if item_words:
        try:
            quantity = int(item_words[-1])
        except ValueError:
            pass
        else:
            item_words = item_words[:-1]
    item = " ".join(item_words).replace("_", " ")
    if not item:
        print("Buy what? Type: buy <item> [count].")
        return False
    if item not in dungeon.prices:
        print("No such item in the shop.")
        return False
    if quantity <= 0:
        print("The quantity must be positive.")
        return False
    price = dungeon.prices[item]
    if quantity == 1:
        gold, ok = dungeon.buy(price, run["gold"])
    else:
        gold, ok = dungeon.buy(price, run["gold"], quantity=quantity)
    if not ok:
        print(f"Not enough gold: need {price * quantity}, have {run['gold']}.")
        return False
    run["gold"] = gold
    inventory = run["inventory"]
    inventory[item] = inventory.get(item, 0) + quantity
    print(f"Bought {quantity} {item} for {price * quantity} gold. Gold left: {gold}.")
    return True


def drink(run, words):
    """Расходует один предмет рюкзака и применяет его эффект; возвращает None."""
    item = (" ".join(words[1:]) or "potion").replace("_", " ")
    inventory = run["inventory"]
    hero = run["hero"]
    if inventory.get(item, 0) == 0:
        print(f"No {item} in the backpack.")
        return
    if item == "potion":
        hero.heal(10, run["max_health"])
    elif item == "torch oil":
        hero.stamina = min(hero.stamina + 5, run["max_stamina"])
    elif item == "war elixir":
        run["ability_bonus"] += 2
    else:
        print("This item cannot be used.")
        return
    inventory[item] -= 1
    if inventory[item] == 0:
        del inventory[item]
    if item == "potion":
        print(f"You drink a potion. Health: {hero.health}. Potions left: {inventory.get(item, 0)}.")
    else:
        print(f"You use {item}.")


def train(hero):
    """Печатает серию ударов и итог тренировки; возвращает None."""
    print("You test your weapon on a rotten support beam left by the miners.")
    total = 0.0
    critical = 0
    for number in range(1, STRIKES + 1):
        hit, crit = hero.strike(number)
        total += hit
        critical += crit
        line = f"Strike {number}: {hit:.1f}"
        print(line + " — critical!" if crit else line)
    print()
    print(f"Total: {STRIKES} strikes, {critical} critical.")
    print(f"Damage: {total:.1f}.")
    print(f"Average damage: {total / STRIKES:.1f}.")
    cost = 3
    hero.spend_stamina(cost)
    print(f"Training cost: {cost} stamina.")


def main():
    """Ведёт диалог и забег, сохраняет выход и прерывание, печатает итог."""
    print(FRAME)
    print("   " + TITLE + "   ")
    print(f" v{VERSION}")
    print(FRAME)
    run = None
    outcome = "interrupted"
    try:
        run = load_save()
        if run is None:
            run = new_run()
        hero = run["hero"]
        while hero.health > 0:
            if run["battle"] is not None:
                battle(run)
                run["actions"] += 1
                print_state(run)
                if hero.health <= 0:
                    break
            print("\n".join(MENU))
            print()
            line = input()
            verb, words = parse_command(line)
            while not verb:
                print("Empty command. Type a command or number.")
                line = input()
                verb, words = parse_command(line)
            match verb:
                case "exit":
                    print("You climb the rusty ladder back to daylight. Water swallows your footprints.")
                    if not run.get("discard_save", False) and write_save(run):
                        print("Progress saved.")
                    outcome = "exit"
                    break
                case "look":
                    print("Dark water covers the rails. White marks on the beams show the flood level.")
                case "go":
                    if len(words) > 1:
                        direction = words[1]
                        if len(words) != 2 or direction not in DIRECTIONS:
                            print("Choose north, south, west or east.")
                            continue
                        dr, dc = DIRECTIONS[direction]
                        row, column = run["position"]
                        nr, nc = row + dr, column + dc
                        if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                            run["position"] = (nr, nc)
                            run["visited"].add((nr, nc))
                            item = LOOT.get((nr, nc))
                            if item is not None and item not in run["loot"]:
                                run["loot"].add(item)
                                print(f"You found {item}! Unique loot: {len(run['loot'])}.")
                            print(f"You step {direction}. Room ({nr}, {nc}).")
                        else:
                            print(f"Cannot go {direction}: wall or edge.")
                    elif hero.spend_stamina(2):
                        print("Your legs give way. You wade forward on sheer will.")
                    else:
                        print("You go forward carefully. Water splashes over the rails.")
                case "rest":
                    hero.stamina = min(hero.stamina + 1, run["max_stamina"])
                    print("You sit on an overturned cart and catch your breath.")
                case "listen":
                    print("Beyond the dripping water, something taps against a pipe.")
                case "torch":
                    hero.spend_stamina(1)
                    print("Your torch reveals copper veins above the waterline.")
                case "train":
                    train(hero)
                case "descend":
                    battle(run)
                case "leaders":
                    print_leaderboard(run["log"])
                case "shop":
                    print("Shop:")
                    for name, price in dungeon.prices.items():
                        print(f"{name}: {price} gold")
                case "buy":
                    if not purchase(run, words):
                        continue
                case "backpack":
                    if not run["inventory"]:
                        print("Backpack is empty.")
                    else:
                        print("Backpack:")
                        for name, quantity in run["inventory"].items():
                            print(f"{name}: {quantity} pcs")
                case "drink":
                    drink(run, words)
                case "map":
                    print("Map:")
                    for row in range(len(MAP)):
                        cells = ["@" if (row, column) == run["position"] else MAP[row][column]
                                 for column in range(len(MAP[row]))]
                        print(" ".join(cells))
                case "scout":
                    print(f"Scout: {scout(*run['position'], set())} rooms reachable.")
                case "help":
                    print("Commands: " + ", ".join(commands) + ".")
                    print("Numbers 0-11 work as before.")
                case "newgame":
                    if SAVE.exists():
                        os.remove(SAVE)
                        print("Save destroyed. The next run starts fresh.")
                    else:
                        print("No save to destroy.")
                    run["discard_save"] = True
                    continue
                case _:
                    print(f"Don't understand command: '{line.strip()}'. Type 'help'.")
                    continue
            run["actions"] += 1
            print_state(run)
        if hero.health <= 0:
            outcome = "death"
            print(f"{hero.name} falls. The mine claims another seeker.")
            if SAVE.exists():
                os.remove(SAVE)
    except (KeyboardInterrupt, EOFError):
        print()
        print("The player ended the session.")
        if run is not None:
            if run["hero"].health <= 0:
                outcome = "death"
                if SAVE.exists():
                    os.remove(SAVE)
            elif not run.get("discard_save", False) and write_save(run):
                print("Progress saved.")
    finally:
        if run is not None:
            if run["inventory"]:
                print("Left behind in the backpack:")
                for name, quantity in run["inventory"].items():
                    print(f"{name}: {quantity} pcs")
            else:
                print("Left behind in the backpack: nothing.")
            print(FRAME)
            if outcome == "death":
                print(f"You did not make it, {run['hero'].name}. Actions: {run['actions']}.")
            elif outcome == "exit":
                print(f"Run over, {run['hero'].name}. Actions: {run['actions']}.")
            else:
                print(f"Session interrupted, {run['hero'].name}. Actions: {run['actions']}.")
            log = run["log"]
            if run["battle"] is not None:
                log = log + run["battle"].rounds
            print_run_summary(log)
            print(FRAME)


if __name__ == "__main__":
    main()
