n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
print(sum(values))
print(min(values))
print(max(values))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
print(sorted(values))
print(values)

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
values.sort(reverse=True)
print(values)
print(len(values))

n = int(input())
values = []
for i in range(n):
    values.append(input())
print(sorted(values, key=len))
print(max(values, key=len))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
squares = [number * number for number in values]
print(squares)
print(sum(squares))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
positive = [number for number in values if number > 0]
print(positive)
print(len(positive))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
d = int(input())
print([number * d for number in values])
print(len([number for number in values if number == d]))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
print(sorted(values, key=abs, reverse=True))

n = int(input())
values = []
for i in range(n):
    values.append(input())
print(sorted(values, key=len))
print(max(values, key=len))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
print(sorted(values, reverse=True)[1])

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
average = sum(values) / len(values)
print([number for number in values if number > average])
print(f"{average:.1f}")

n = int(input())
rows = []
for i in range(n):
    hero_damage = float(input())
    enemy_damage = float(input())
    rows.append([hero_damage, enemy_damage])
rows.sort(key=lambda row: row[0], reverse=True)
for row in rows:
    print(row)
print(rows[0])

n = int(input())
values = []
for i in range(n):
    values.append(input())
letter = input()
print([word for word in values if word[:1] == letter])

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
k = int(input())
print(sorted(values, reverse=True)[:k])

n = int(input())
values = []
for i in range(n):
    values.append(input())
lengths = [len(word) for word in values]
print(lengths)
print(sum(lengths))
