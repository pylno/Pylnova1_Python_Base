#5. Реализовать функцию get_jokes()
import random


def get_jokes(number):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(number):
        joke = nouns[random.randint(0, len(nouns) - 1)] + ' ' + adverbs[random.randint(0, len(adverbs) - 1)] + ' ' + \
               adjectives[random.randint(0, len(adjectives) - 1)]
        jokes.append(joke)
    return jokes


print(get_jokes(int(input())))