n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
print(len(values))
print(values[0])

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
k = int(input())
print(values[k])
print(values[-1])
print(k)

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
total = 0
product = 1
for i in range(len(values)):
    total += values[i]
    if i % 2 == 0:
        product *= values[i]
print(total)
print(product)

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
best = 0
for i in range(1, len(values)):
    if values[i] > values[best]:
        best = i
print(best)
print(values[best])

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
number = int(input())
values.append(number)
print(values)
print(len(values))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
k1 = int(input())
k2 = int(input())
part = values[k1:k2 + 1]
total = 0
for number in part:
    total += number
print(part)
print(total)

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
print(values[::-1])
print(values)

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
number = int(input())
if number in values:
    values.remove(number)
print(values)
print(len(values))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
total = 0
for number in values:
    total += number
average = total / len(values)
result = []
for number in values:
    if number > average:
        result.append(number)
print(result)
print(len(result))

n = int(input())
values = []
for i in range(n):
    values.append(input())
longest = values[0]
shortest = values[0]
for word in values:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(shortest):
        shortest = word
print(longest)
print(shortest)
print(len(longest))
print(len(shortest))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
count = 0
for i in range(len(values)):
    if values[i] < 0:
        values[i] = 0
        count += 1
print(values)
print(count)

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
k = int(input())
values.insert(k, 0)
print(values)
print(len(values))

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
removed = values.pop()
print(removed)
print(values)

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
number = int(input())
print(values.count(number))
if number in values:
    print(values.index(number))
else:
    print(-1)

n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
part = values[::2]
total = 0
for number in part:
    total += number
print(part)
print(total)
