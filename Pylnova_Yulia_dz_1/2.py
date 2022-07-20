#1.2 Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X) ...
numbers = []
numbers_increased = []
digit_sum = 0
acc_sum = 0

for i in range(1, 1001, 2):
    number_cube = i ** 3
    numbers.append(number_cube)
print('Список кубов нечетных чисел от 1 до 1000:', numbers)

for i in numbers:
    digit_sum = 0
    i_mod = i
    while i_mod >= 1:
        digit = i_mod % 10
        digit_sum += digit
        i_mod = i_mod // 10
    if digit_sum % 7 == 0:
        acc_sum += i
print ('')
print('Сумма кубов, сумма цифр которых делится на 7:', acc_sum)

for i in numbers:
    number_increased = i + 17
    numbers_increased.append(number_increased)
print ('')
print('Увеличенный на 17 список кубов:', numbers_increased)

acc_sum = 0
for i in numbers_increased:
    digit_sum= 0
    i_mod = i
    while i_mod >= 1:
        digit = i_mod % 10
        digit_sum += digit
        i_mod = i_mod // 10
    if digit_sum % 7 == 0:
        acc_sum += i
print ('')
print('Сумма новых чисел, сумма цифр которых делится на 7:', acc_sum)

#Со звездочкой задание b
for i in range(len(numbers)):
    numbers[i] += 17
print ('')
print('Обновленный список, увеличенный на 17, без создания нового списка:', numbers)

acc_sum = 0
for i in numbers:
    digit_sum = 0
    i_mod = i
    while i_mod >= 1:
        digit = i_mod % 10
        digit_sum += digit
        i_mod = i_mod // 10
    if digit_sum % 7 == 0:
        acc_sum += i
print ('')
print('Сумма новых чисел, сумма цифр которых делится на 7, без создания нового списка:', acc_sum)