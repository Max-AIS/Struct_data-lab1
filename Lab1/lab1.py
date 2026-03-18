def res(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = res(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y

a = int(input())
b = int(input())

d, x, y = res(a, b)

print(d, x, y)
print("Автор: Голиков М.А.")
print("Группа: 020303-АИСа-025")