import random

t = """0.00 12.53 5.10 11.70 3.00
12.53 0.00 10.05 10.00 11.40
5.10 10.05 0.00 13.45 2.24
11.70 10.00 13.45 0.00 13.04
3.00 11.40 2.24 13.04 0.00"""

# матрица расстояний между городами
cities = []
for row in t.split("\n"):
    nums = [float(i) for i in row.split(" ")]
    cities.append(nums)

for i in cities:
    print(i)

# индексы всех городов
notincludet = [i for i in range(len(cities[0]))]

travel = [random.choice(notincludet)]
print(travel)
notincludet.remove(travel[0])


def get_dist(travel, cities):
    dist = 0
    for i in range(len(travel) - 1):
        dist += float(cities[travel[i]][travel[i + 1]])
    return (dist)


ch = 0
while len(notincludet) > 0:
    pairs = []
    # ближайший непосещенный город
    for i in travel:
        pairs.append([i, min(notincludet, key=lambda x: cities[i][x])])

    nextC = min(pairs, key=lambda x: cities[x[0]][x[1]])

    # расстовяние до след города
    distNextGorod = cities[nextC[0]][nextC[1]]

    travel.insert(travel.index(nextC[0]) + 1, nextC[1])

    notincludet.remove(nextC[1])
    ch += 1

    dist = int(get_dist(travel, cities))
    print(f"Шаг номер {ch}, {[[i, cities[i[0]][i[1]]] for i in pairs]}, Следующий город {nextC[1]}, Дистанция до след города {distNextGorod}, путь {travel}, Дистанция {dist}")

print(f"Путь {travel}, дистанция {dist}")
