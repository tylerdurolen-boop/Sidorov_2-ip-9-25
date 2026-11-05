number = int(input())
count = int(input())
for i in range(count):
    print(number)

a = int(input())
b = int(input())
count = 0
for number in range(a, b + 1):
    print(number)
    count += 1
print(count)

a = int(input())
b = int(input())
count = 0
for number in range(b - 1, a, -1):
    print(number)
    count += 1
print(count)

price = float(input())
for weight in range(1, 11):
    print(price * (weight / 1))

price = float(input())
for weight in range(1, 11):
    print(price * (weight / 10))

price = float(input())
for weight in range(12, 21, 2):
    print(price * (weight / 10))

a = int(input())
b = int(input())
total = 0
for number in range(a, b + 1):
    total += number
print(total)

a = int(input())
b = int(input())
total = 1
for number in range(a, b + 1):
    total *= number
print(total)

a = int(input())
b = int(input())
total = 0
for number in range(a, b + 1):
    total += number ** 2
print(total)

n = int(input())
total = 0.0
for number in range(1, n + 1):
    total += 1 / number
print(total)

n = int(input())
total = 0
for number in range(n, 2 * n + 1):
    total += number ** 2
print(total)

n = int(input())
total = 1.0
for number in range(1, n + 1):
    total *= 1 + number / 10
print(total)

n = int(input())
total = 0.0
sign = 1
for i in range(1, n + 1):
    total += sign * (1 + i / 10)
    sign = -sign
print(total)

n = int(input())
total = 0
for number in range(1, 2 * n, 2):
    total += number
print(total)

a = float(input())
n = int(input())
power = 1.0
for i in range(n):
    power *= a
print(power)
