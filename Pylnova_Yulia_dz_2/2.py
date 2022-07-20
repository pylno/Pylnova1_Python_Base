#2. Дан список:['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'].Каждое целое число обособить кавычками  и дополнить нулём до двух целочисленных разрядов:['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']. СФормировать строку: в "05" часов "17" минут температура воздуха была "+05" градусов
lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbs = ['0','1','2','3','4','5','6','7','8','9']
out_str = ''
print('1) Исходный список:', lst)
length = len(lst)
i = 0
while i < length-1:
  if any(numb in lst[i + 1] for numb in numbs) and lst[i]!= '\"':
    lst.insert(i + 1, '\"')
    length += 1
  elif any(numb in lst[i] for numb in numbs):
    lst.insert(i + 1, '\"')
    length += 1
  if any(numb in lst[i] for numb in numbs) and len(lst[i]) < 2:
    lst.insert(i, '0' + lst.pop(i))
  if lst[i][0] == '+' and len(lst[i])<3:
    lst.insert(i, lst.pop(i).replace('+', '+0'))
  elif lst[i][0] == '-' and len(lst[i])<3:
    lst.insert(i, lst.pop(i).replace('-', '-0'))
  i += 1

for i in range(len(lst)):
  if lst[i] == '\"' and any(numb in lst[i + 1] for numb in numbs) or any(numb in lst[i] for numb in numbs):
    out_str += lst[i]
  else:
    out_str += lst[i] + ' '
print('\t1.Новый список с добавлением кавычек:', lst)
print('\t2.Окончательная строка:', out_str)