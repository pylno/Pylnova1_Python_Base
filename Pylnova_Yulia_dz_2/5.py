#5 Создать список, содержащий цены на товары (10–20 товаров), например:[57.8, 46.51, 97, ...]
import math
prices = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 723.11, 454, 33.33, 999.99, 18.01, 56.25]
out_str = ''
prices_backwards = []
for i in range(len(prices)):
    frac, even = math.modf(prices[i])
    frac_str = str(int(round(frac, 2) * 100))
    if len(frac_str) == 1:
        frac_str = '0' + frac_str
    if i == len(prices) - 1:
        out_str += str(int(even)) + ' руб ' + frac_str + ' коп.'
    else:
        out_str += str(int(even)) + ' руб ' + frac_str + ' коп, '
print('Цены товаров:', str(out_str))

prices.sort()
print('Отсортированный по возрастанию список:', prices)

for i in range(len(prices)):
    prices_backwards.append(prices[len(prices) - (i + 1)])
print('Отсортированный по убыванию список:', prices_backwards)

print('5 самых дорогих товаров:')
i = 0
while i < 5:
    print(prices_backwards[i])
    i += 1

print('Эти же товары по возрастанию:')
i = 4
while i >= 0:
    print(prices_backwards[i])
    i -= 1