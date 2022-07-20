#Задание 1.3 Склонение слова Процент
for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        print(i, 'процент')
    elif (i % 10 == 2 or i % 10 == 3 or i % 10 == 4) and (20 < i or i < 10):
        print(i, 'процентa')
    else:
        print(i, 'процентов')