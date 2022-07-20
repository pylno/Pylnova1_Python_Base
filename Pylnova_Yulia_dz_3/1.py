#1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык
def num_translate(number):
    num_dic = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    # for key, val in num_dic.items():
    #     print(val)

    if number in num_dic:
        return num_dic[number]
    else:
        return None

key = input()
print(num_translate(key))