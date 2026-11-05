letter = input()
print(ord(letter))

n = int(input())
print(chr(n))

letter = input()
print(chr(ord(letter) - 1))
print(chr(ord(letter) + 1))

n = int(input())
print("".join(chr(ord("A") + i) for i in range(n)))

n = int(input())
print("".join(chr(ord("z") - i) for i in range(n)))

letter = input()
if "0" <= letter <= "9":
    print("digit")
elif "a" <= letter <= "z" or "A" <= letter <= "Z":
    print("lat")
else:
    print("rus")

text = input()
print(ord(text[0]))
print(ord(text[-1]))

n = int(input())
letter = input()
print(letter * n)

n = int(input())
first = input()
second = input()
print((first + second) * (n // 2))

text = input()
print(text[::-1])

text = input()
print(" ".join(text))

text = input()
n = int(input())
print(("*" * n).join(text))

text = input()
count = 0
for letter in text:
    if letter.isdigit():
        count += 1
print(count)

text = input()
count = 0
for letter in text:
    if "A" <= letter <= "Z":
        count += 1
print(count)

text = input()
count = 0
for letter in text:
    if "a" <= letter <= "z" or "а" <= letter <= "я" or letter == "ё":
        count += 1
print(count)
