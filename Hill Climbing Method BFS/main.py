import random


def ham_dis(a, b):
    ch = 0
    for i in range(len(a)):
        ch += (1 if a[i] != b[i] else 0)
    return ch


example_list = []
for i in range((2**5)+1):
    example_list.append(['{:05}'.format(int(bin(i)[2:])), ((i)-16)**2])
for i in range(32):
    print(example_list[i])
print("Введите количество шагов")
N = int(input())


t = random.choice(example_list)
max_ = t[1]
maxs = t[0]
okrmaxs = [i for i in example_list if ham_dis(t[0], i[0]) == 1]
i = 1
print(f"Шаг номер {i}, max={max_},maxs={maxs}, si=0, Окрестность = {okrmaxs} ")
while i < N:
    if len(okrmaxs) > 0:
        i += 1
        si = max(okrmaxs, key=lambda x: int(x[1]))
        print(
            f"Шаг номер {i}, max={max_},maxs={maxs}, si={si}, Окрестность = {okrmaxs} ")
        okrmaxs.remove(si)
        if si[1] > max_:
            max_ = si[1]
            maxs = si[0]
            okrmaxs = [i for i in example_list if ham_dis(si[0], i[0]) == 1]
        else:
            print(
                f"Шаг номер {i+1}, max={max_} > Окрестность = {max(okrmaxs, key=lambda x: int(x[1]))} ")
            break
    else:
        break
print(f"max={max_}, maxs={maxs}")
