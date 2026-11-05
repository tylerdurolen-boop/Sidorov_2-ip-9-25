n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
print(len(data))
for key in data:
    print(key)

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
key = input()
if key in data:
    print(data[key])
else:
    print("нет такого ключа")

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
key = input()
print(data.get(key, 0))

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
key = input()
value = int(input())
data[key] = data.get(key, 0) + value
print(data[key])

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
key = input()
data.pop(key, None)
print(len(data))

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
total = 0
for value in data.values():
    total += value
print(total)

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
best = next(iter(data))
for key in data:
    if data[key] > data[best]:
        best = key
print(best)

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
value = int(input())
print(value in data.values())

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
m = int(input())
other = {}
for i in range(m):
    key = input()
    value = int(input())
    other[key] = value
common = [key for key in data if key in other]
data.update(other)
print(len(data))
print(data[common[0]])

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
for name, price in data.items():
    print(f"{name}: {price}")

n = int(input())
counts = {}
for i in range(n):
    word = input()
    counts[word] = counts.get(word, 0) + 1
for word, count in counts.items():
    print(f"{word}: {count}")

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
inverted = {}
for key, value in data.items():
    inverted[value] = key
for key, value in inverted.items():
    print(f"{key}: {value}")

n = int(input())
stock = {}
for i in range(n):
    name = input()
    price = int(input())
    quantity = int(input())
    stock[name] = [price, quantity]
total = 0
best = next(iter(stock))
for name, (price, quantity) in stock.items():
    total += price * quantity
    if price * quantity > stock[best][0] * stock[best][1]:
        best = name
print(total)
print(best)

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
limit = int(input())
for key in list(data):
    if data[key] < limit:
        del data[key]
print(len(data))

n = int(input())
data = {}
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value
m = int(input())
other = {}
for i in range(m):
    key = input()
    value = int(input())
    other[key] = value
ignored = 0
for key, value in other.items():
    if key in data:
        ignored += 1
    else:
        data[key] = value
print(len(data))
print(ignored)
