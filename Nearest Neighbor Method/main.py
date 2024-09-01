import random

t = """0.00 12.53 5.10 11.70 3.00
12.53 0.00 10.05 10.00 11.40
5.10 10.05 0.00 13.45 2.24
11.70 10.00 13.45 0.00 13.04
3.00 11.40 2.24 13.04 0.00"""
cities = []
for row in t.split("\n"):
    nums = [float(i) for i in row.strip().split(" ")]
    cities.append(nums)
travel = []
for i in cities:
    print(i)
travel.append(3)  # random.randint(0, len(cities[0]) - 1)
notincludet = [i for i in range(len(cities[0]))]
notincludet.remove(travel[0])
distance = 0
for i in range(len(cities[0]) - 1):
    minc = cities[travel[-1]][notincludet[0]]
    indc = notincludet[0]
    for j in notincludet:
        if cities[travel[-1]][j] < minc:
            minc = cities[travel[-1]][j]
            indc = j
    distance += float(minc)
    travel.append(indc)
    notincludet.remove(indc)
    print(
        f"Шаг номер {i + 1}, путь = {travel}, длина = {distance:.2f}, след = {indc}, расстояние = {minc} ")
print(f"Итоговый цикл {travel}, итоговая длина {distance:.2f}")
