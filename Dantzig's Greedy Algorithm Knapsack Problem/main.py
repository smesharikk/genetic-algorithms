import random

items = []  # [ценность, вес, номер]
bag = [[0, 0]]
print("Введите количество предметов")
N = int(input())
sum = 0
yi = 0  # удельная ценность предмета
for i in range(N):
    # вместо yi у нас был 0
    items.append([random.randint(1, 10), random.randint(1, 10), yi, i+1])
    items[i][2] = items[i][0] / items[i][1]
for i in range(N):
    print(items[i])
    sum += items[i][1]
wi = sum * 0.6


def custom_key(items):
    return items[2]


items.sort(reverse=True, key=custom_key)
print("______________________________")
travel = []
for i in range(N):
    if (bag[0][1] == wi):
        break
    print(f"Шаг номер {i + 1}, Предмет ={items[i]}, Ранец={bag}")
    if (items[i][1] + bag[0][1]) <= wi:
        bag[0][0] += items[i][0]
        bag[0][1] += items[i][1]
        print("Добавил")
        travel.append(items[i][3])
print(f"Итоговое решение {bag}")
print(f"Мы добавили предметы под номерами {travel}")
