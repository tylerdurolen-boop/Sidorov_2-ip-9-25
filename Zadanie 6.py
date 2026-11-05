try:
    number = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    print(number)

a = int(input())
b = int(input())
try:
    result = a / b
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(f"{result:.1f}")

try:
    a = int(input())
    b = int(input())
    result = a / b
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(result)

try:
    number = int(input())
    result = 100 / number
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(result)
finally:
    print("Вычисление завершено")

word = input()
index = int(input())
try:
    letter = word[index]
except IndexError:
    print("Нет такого символа")
else:
    print(letter)

word = input()
try:
    index = int(input())
    letter = word[index]
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")
else:
    print(letter)

while True:
    try:
        number = int(input())
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")
print(number)

total = 0
skipped = 0
while True:
    line = input()
    if line == "":
        break
    try:
        number = int(line)
    except ValueError:
        print("Пропущено: не число")
        skipped += 1
    else:
        total += number
print(total)
print(skipped)

try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
except ValueError as error:
    print("Отклонено:", error)
else:
    print("Принято:", age)

while True:
    try:
        choice = int(input())
    except ValueError:
        print("Введите число")
        continue
    if 1 <= choice <= 5:
        break
    print("Такого пункта нет")
print(choice)

try:
    a = float(input())
    b = float(input())
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")

try:
    number = int(input())
except ValueError as error:
    print(error)
    print(type(error))
else:
    print(number)

try:
    a = float(input())
    b = float(input())
except ValueError:
    print("Ошибка ввода")
else:
    print((a + b) / 2)

try:
    number = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    if number > 0:
        number += 1
    elif number < 0:
        number -= 2
    else:
        number = 10
    print(number)

try:
    n = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    k = 0
    total = 0
    while total < n:
        k += 1
        total += k
    print(k)
    print(total)
