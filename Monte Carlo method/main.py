import random
example_list = []  # ландшафт приспособленности
for i in range((2**15)+1):
    example_list.append(
        ['{:015}'.format(int(bin(i+1)[2:])), random.randint(1, 100000)])
for i in range(32):
    print(example_list[i])
print("Введите количество шагов")
N = int(input())
random.shuffle(example_list)  # перемешиваем
max = 0
maxs = 0
for i in range(N):
    print(
        f"Номер шага={i+1}, Кодировка={max}, Приспособленность={maxs}, Выбираемая кодировка={example_list[i][0]}, Выбираемая приспособленность={example_list[i][1]}")
    if example_list[i][1] > max:
        max = example_list[i][1]
        maxs = example_list[i][0]
        print("Смена максимума")
print(f"Кодировка {maxs}, приспособленность {max}")
