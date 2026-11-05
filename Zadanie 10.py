def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1

a = float(input())
b = float(input())
print(sign(a) + sign(b))

def roots_count(a, b, c):
    discriminant = b * b - 4 * a * c
    if abs(discriminant) < 1e-9:
        return 1
    if discriminant > 0:
        return 2
    return 0

for i in range(3):
    a = float(input())
    b = float(input())
    c = float(input())
    print(roots_count(a, b, c))

def circle_s(r):
    return 3.14 * r * r

for i in range(3):
    radius = float(input())
    print(circle_s(radius))

def circle_s(r):
    return 3.14 * r * r

def ring_s(r1, r2):
    return circle_s(r1) - circle_s(r2)

for i in range(3):
    r1 = float(input())
    r2 = float(input())
    print(ring_s(r1, r2))

def triangle_p(a, h):
    side = ((a / 2) ** 2 + h * h) ** 0.5
    return a + 2 * side

for i in range(3):
    a = float(input())
    h = float(input())
    print(triangle_p(a, h))

def sum_range(a, b):
    total = 0
    for number in range(a, b + 1):
        total += number
    return total

a = int(input())
b = int(input())
c = int(input())
print(sum_range(a, b))
print(sum_range(b, c))

def calc(a, b, op):
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b
    return a + b

a = float(input())
b = float(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())
print(calc(a, b, n1))
print(calc(a, b, n2))
print(calc(a, b, n3))

def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    return 4

for i in range(3):
    x = float(input())
    y = float(input())
    print(quarter(x, y))

def even(k):
    return k % 2 == 0

count = 0
for i in range(10):
    k = int(input())
    if even(k):
        count += 1
print(count)

from math import isqrt

def is_square(k):
    root = isqrt(k)
    return root * root == k

count = 0
for i in range(10):
    k = int(input())
    if is_square(k):
        count += 1
print(count)

def is_power5(k):
    while k % 5 == 0:
        k //= 5
    return k == 1

count = 0
for i in range(10):
    k = int(input())
    if is_power5(k):
        count += 1
print(count)

def is_power_n(k, n):
    while k % n == 0:
        k //= n
    return k == 1

n = int(input())
count = 0
for i in range(10):
    k = int(input())
    if is_power_n(k, n):
        count += 1
print(count)

def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

count = 0
for i in range(10):
    k = int(input())
    if is_prime(k):
        count += 1
print(count)

def digit_count(k):
    count = 0
    while k > 0:
        count += 1
        k //= 10
    return count

for i in range(5):
    k = int(input())
    print(digit_count(k))

def digit_n(k, n):
    position = 1
    while k > 0:
        if position == n:
            return k % 10
        position += 1
        k //= 10
    return -1

for i in range(5):
    k = int(input())
    for n in range(1, 6):
        print(digit_n(k, n))

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_loop(n):
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result

def digit_sum_recursive(n):
    if n < 10:
        return n
    return n % 10 + digit_sum_recursive(n // 10)

def digit_sum_loop(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n = int(input())
print(factorial_recursive(n))
print(factorial_loop(n))
print(digit_sum_recursive(n))
print(digit_sum_loop(n))
