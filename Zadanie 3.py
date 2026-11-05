a = int(input())
print(a > 0)

number = int(input())
if number > 0:
    number += 1
print(number)

a = int(input())
print(a % 2 != 0)

number = int(input())
if number > 0:
    number += 1
else:
    number -= 2
print(number)

a = int(input())
print(a % 2 == 0)

number = int(input())
if number > 0:
    number += 1
elif number < 0:
    number -= 2
else:
    number = 10
print(number)

a = int(input())
b = int(input())
print(a > 2 and b <= 3)

a = int(input())
b = int(input())
c = int(input())
print((a > 0) + (b > 0) + (c > 0))

a = int(input())
b = int(input())
print(a >= 0 or b < -2)

a = int(input())
b = int(input())
c = int(input())
print((a > 0) + (b > 0) + (c > 0))
print((a < 0) + (b < 0) + (c < 0))

a = int(input())
b = int(input())
c = int(input())
print(a < b < c)

a = int(input())
b = int(input())
c = int(input())
print(a < b < c or c < b < a)

a = int(input())
b = int(input())
print(a % 2 != 0 and b % 2 != 0)

a = int(input())
b = int(input())
print(a % 2 != 0 or b % 2 != 0)

a = int(input())
b = int(input())
print((a % 2 != 0) + (b % 2 != 0) == 1)

a = int(input())
b = int(input())
print(a % 2 == b % 2)

a = int(input())
b = int(input())
c = int(input())
print(a > 0 and b > 0 and c > 0)

a = int(input())
b = int(input())
c = int(input())
print(a > 0 or b > 0 or c > 0)

a = int(input())
b = int(input())
c = int(input())
print((a > 0) + (b > 0) + (c > 0) == 1)

a = int(input())
b = int(input())
c = int(input())
print((a > 0) + (b > 0) + (c > 0) == 2)
