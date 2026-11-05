def power_a3(a):
    return a ** 3

for i in range(5):
    a = float(input())
    print(power_a3(a))

def power_a234(a):
    return a ** 2, a ** 3, a ** 4

for i in range(5):
    a = float(input())
    square, cube, fourth = power_a234(a)
    print(square)
    print(cube)
    print(fourth)

def mean(x, y):
    return (x + y) / 2, (x * y) ** 0.5

a = float(input())
b = float(input())
c = float(input())
d = float(input())
for value in (b, c, d):
    arithmetic, geometric = mean(a, value)
    print(arithmetic)
    print(geometric)

def triangle_ps(a):
    return 3 * a, a * a * 3 ** 0.5 / 4

for i in range(3):
    a = float(input())
    perimeter, area = triangle_ps(a)
    print(perimeter)
    print(area)

def rect_ps(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return 2 * (width + height), width * height

for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    perimeter, area = rect_ps(x1, y1, x2, y2)
    print(perimeter)
    print(area)

def digit_count_sum(k):
    count = 0
    total = 0
    while k > 0:
        total += k % 10
        count += 1
        k //= 10
    return count, total

for i in range(5):
    k = int(input())
    count, total = digit_count_sum(k)
    print(count)
    print(total)

def invert_digits(k):
    result = 0
    while k > 0:
        result = result * 10 + k % 10
        k //= 10
    return result

for i in range(5):
    k = int(input())
    print(invert_digits(k))

def add_right_digit(d, k):
    return k * 10 + d

k = int(input())
d1 = int(input())
d2 = int(input())
k = add_right_digit(d1, k)
print(k)
k = add_right_digit(d2, k)
print(k)

def add_left_digit(d, k):
    place = 10
    while place <= k:
        place *= 10
    return d * place + k

k = int(input())
d1 = int(input())
d2 = int(input())
k = add_left_digit(d1, k)
print(k)
k = add_left_digit(d2, k)
print(k)

def swap(x, y):
    return y, x

a = float(input())
b = float(input())
c = float(input())
d = float(input())
a, b = swap(a, b)
c, d = swap(c, d)
b, c = swap(b, c)
print(a)
print(b)
print(c)
print(d)

def minmax(x, y):
    if x <= y:
        return x, y
    return y, x

a = float(input())
b = float(input())
c = float(input())
d = float(input())
a, b = minmax(a, b)
c, d = minmax(c, d)
a, c = minmax(a, c)
b, d = minmax(b, d)
print(a)
print(d)

def sort_inc3(a, b, c):
    return tuple(sorted((a, b, c)))

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
for result in (sort_inc3(a1, b1, c1), sort_inc3(a2, b2, c2)):
    for value in result:
        print(value)

def sort_dec3(a, b, c):
    return tuple(sorted((a, b, c), reverse=True))

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
for result in (sort_dec3(a1, b1, c1), sort_dec3(a2, b2, c2)):
    for value in result:
        print(value)

def shift_right3(a, b, c):
    return c, a, b

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
for result in (shift_right3(a1, b1, c1), shift_right3(a2, b2, c2)):
    for value in result:
        print(value)

def shift_left3(a, b, c):
    return b, c, a

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
for result in (shift_left3(a1, b1, c1), shift_left3(a2, b2, c2)):
    for value in result:
        print(value)
