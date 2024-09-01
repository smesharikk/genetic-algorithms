import random

# Хэммингово расстояние


def ham_dis(a, b):
    count_differences = 0
    for i in range(len(a)):
        count_differences += (1 if a[i] != b[i] else 0)
    return count_differences


example_list = []
for i in range(2**5):                                  # 2**5  вроде как без +1
    example_list.append(['{:05}'.format(int(bin(i)[2:])), i])
for i in range(32):  # 32
    print(example_list[i])

print("Введите количество шагов")
N = int(input())

t = random.choice(example_list)
max = t[1]  # текущее макс значение приспособленности
maxs = t[0]  # хранит кодировку(решение )

okrmaxs = [i for i in example_list if ham_dis(t[0], i[0]) == 1]

i = 1
print(f"Шаг номер {i}, max={max}, maxs={maxs}, si=0, Окрестность = {okrmaxs} ")
while i < N:
    if len(okrmaxs) > 0:
        i += 1
        si = random.choice(okrmaxs)
        print(
            f"Шаг номер {i}, max={max},maxs={maxs}, si={si}, Окрестность = {okrmaxs} ")
        okrmaxs.remove(si)
        if si[1] > max:
            max = si[1]
            maxs = si[0]
            okrmaxs = [i for i in example_list if ham_dis(si[0], i[0]) == 1]
    else:
        break
print(f"maxs={maxs}, max={max}")
