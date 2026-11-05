rest = float(input())
piece = float(input())
count = 0
while rest >= piece:
    rest -= piece
    count += 1
print(rest)

rest = float(input())
piece = float(input())
count = 0
while rest >= piece:
    rest -= piece
    count += 1
print(count)

rest = int(input())
piece = int(input())
count = 0
while rest >= piece:
    rest -= piece
    count += 1
print(count)
print(rest)

n = int(input())
while n % 3 == 0:
    n //= 3
print(n == 1)

n = int(input())
k = 0
while n > 1:
    n //= 2
    k += 1
print(k)

n = int(input())
product = 1.0
while n > 0:
    product *= n
    n -= 2
print(product)

n = int(input())
k = 1
while k * k <= n:
    k += 1
print(k)

n = int(input())
k = 0
while (k + 1) * (k + 1) <= n:
    k += 1
print(k)

n = int(input())
k = 0
power = 1
while power <= n:
    power *= 3
    k += 1
print(k)

n = int(input())
k = 0
power = 1
while power * 3 < n:
    power *= 3
    k += 1
print(k)

n = int(input())
k = 0
total = 0
while total < n:
    k += 1
    total += k
print(k)
print(total)

n = int(input())
k = 0
total = 0
while total + k + 1 <= n:
    k += 1
    total += k
print(k)
print(total)

a = float(input())
k = 0
total = 0.0
while total <= a:
    k += 1
    total += 1 / k
print(k)
print(total)

a = float(input())
k = 0
total = 0.0
while total + 1 / (k + 1) < a:
    k += 1
    total += 1 / k
print(k)
print(total)

percent = float(input())
months = 0
balance = 1000.0
while balance <= 1100:
    balance += balance * percent / 100
    months += 1
print(months)
print(balance)
