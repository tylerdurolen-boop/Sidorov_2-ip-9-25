name = input()
try:
    with open(name, "w", encoding="utf-8") as file:
        pass
except (OSError, ValueError):
    print(False)
else:
    print(True)

name = input()
n = int(input())
with open(name, "w", encoding="utf-8") as file:
    for i in range(1, n + 1):
        file.write(str(2 * i) + "\n")

name = input()
a = float(input())
d = float(input())
with open(name, "w", encoding="utf-8") as file:
    for i in range(10):
        file.write(str(a + i * d) + "\n")

import os

names = [input() for i in range(4)]
count = 0
for name in names:
    if os.path.exists(name):
        count += 1
print(count)

import os

name = input()
if not os.path.exists(name):
    print(-1)
else:
    with open(name, encoding="utf-8") as file:
        count = sum(1 for line in file if line.strip())
    print(count)

k = int(input())
name = input()
with open(name, encoding="utf-8") as file:
    numbers = [int(line) for line in file if line.strip()]
if 1 <= k <= len(numbers):
    print(numbers[k - 1])
else:
    print(-1)

name = input()
with open(name, encoding="utf-8") as file:
    numbers = [int(line) for line in file if line.strip()]
print(numbers[0])
print(numbers[1])
print(numbers[-2])
print(numbers[-1])

name = input()
destination = input()
with open(name, encoding="utf-8") as file:
    numbers = [int(line) for line in file if line.strip()]
with open(destination, "w", encoding="utf-8") as file:
    file.write(str(numbers[0]) + "\n")
    file.write(str(numbers[-1]) + "\n")

import os

first = input()
second = input()
if os.path.exists(first):
    name, destination = first, second
else:
    name, destination = second, first
with open(name, encoding="utf-8") as file:
    numbers = [int(line) for line in file if line.strip()]
with open(destination, "w", encoding="utf-8") as file:
    file.write(str(numbers[-1]) + "\n")
    file.write(str(numbers[0]) + "\n")

name = input()
destination = input()
with open(name, encoding="utf-8") as file:
    numbers = [int(line) for line in file if line.strip()]
with open(destination, "w", encoding="utf-8") as file:
    for number in numbers[::-1]:
        file.write(str(number) + "\n")
