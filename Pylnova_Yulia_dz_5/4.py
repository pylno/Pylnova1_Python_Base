#4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего
from itertools import islice

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Списком:
result = []
i = 1
while i < len(src):
    if src[i] > src[i-1]:
        result.append(src[i])
    i += 1
print(result)


# С использованием множеств:
result_set = set()
i = 1
while i < len(src):
    if src[i] > src[i-1]:
        result_set.add(src[i])
    else:
        result_set.discard(src[i])
    i += 1
print(result_set)


# Через генераторное выражение
result_gen = (src[j] for j in range(len(src)) if j > 0 and src[j] > src[j-1])
print(*islice(result_gen, len(src)-1))