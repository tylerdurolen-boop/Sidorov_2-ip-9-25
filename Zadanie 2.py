a = float(input())
b = float(input())
temp = a
a = b
b = temp
print(a)
print(b)

a = float(input())
b = float(input())
c = float(input())
temp = c
c = b
b = a
a = temp
print(a)
print(b)
print(c)

a = float(input())
b = float(input())
c = float(input())
temp = a
a = b
b = c
c = temp
print(a)
print(b)
print(c)

x = float(input())
print(3 * x ** 6 - 6 * x ** 2 - 7)

x = float(input())
print(4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2)

a = float(input())
power = a * a
print(power)
power = power * power
print(power)
power = power * power
print(power)

a = float(input())
power = a * a
print(power)
other = power
power = power * a
print(power)
power = power * other
print(power)
other = power * power
print(other)
power = other * power
print(power)

degrees = float(input())
print(degrees * 3.14 / 180)

radians = float(input())
print(radians * 180 / 3.14)

fahrenheit = float(input())
print((fahrenheit - 32) * 5 / 9)

celsius = float(input())
print(celsius * 9 / 5 + 32)

weight = float(input())
cost = float(input())
amount = float(input())
print(cost / weight)
print(cost / weight * amount)

chocolate_weight = float(input())
chocolate_cost = float(input())
toffee_weight = float(input())
toffee_cost = float(input())
print(chocolate_cost / chocolate_weight)
print(toffee_cost / toffee_weight)
print((chocolate_cost / chocolate_weight) / (toffee_cost / toffee_weight))

speed = float(input())
current = float(input())
lake_time = float(input())
river_time = float(input())
print(speed * lake_time + (speed - current) * river_time)

speed1 = float(input())
speed2 = float(input())
distance = float(input())
time = float(input())
print(distance + (speed1 + speed2) * time)

centimeters = int(input())
print(centimeters // 100)

kilograms = int(input())
print(kilograms // 1000)

size = int(input())
print(size // 1024)

segment = int(input())
piece = int(input())
print(segment // piece)

segment = int(input())
piece = int(input())
print(segment % piece)
