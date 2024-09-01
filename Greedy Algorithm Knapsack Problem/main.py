import random
items = []  # [ценность, вес, номер]
bag = [[0, 0]]
print("Введите количество предметов")
N = int(input())
sum = 0
for i in range(N):
    items.append([random.randint(1, 10), random.randint(1, 10), i+1])
for i in range(N):
    print(items[i])
    sum += items[i][1]
# sum 70% от общего веса предметов будет помещено в рюкзак
wi = sum * 0.7
wmax = 0
items.sort(reverse=True)
print("Отсортированный")
for i in range(N):
    print(items[i])
print(f"sum = {sum}")
print(f"wi = {wi}")
travel = []
# while bag[0][1] < wi and bag[0][1] <= wmax and i < N:
for i in range(N):

    if (bag[0][1] == wi):
        break
    print(f"Шаг номер {i+1}, Предмет ={items[i]}, Ранец={bag}")
    if (items[i][1] + bag[0][1]) <= wi:
        bag[0][0] += items[i][0]  # увеличиваем ценность
        bag[0][1] += items[i][1]  # увеличиваем вес
        print("Добавил")
        travel.append(items[i][2])
        wmax += wi
print(f"Итоговое решение {bag}")
print(f"Мы добавили предметы под такими номерами {travel}")
