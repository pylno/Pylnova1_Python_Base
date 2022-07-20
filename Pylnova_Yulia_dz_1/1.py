### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
duration = 400153
time_d = duration//86400
time_h = duration % 86400 //3600
time_m = duration % 86400 % 3600 //60
time_s = duration % 60
if duration >= 86400:
    print(time_d, 'дн', time_h, 'час', time_m, 'мин', time_s, 'сек')
elif 3600 < duration < 86400:
    print(time_h, 'час', time_m, 'мин', time_s, 'сек')
elif 60 <= duration < 3600:
    print(time_m, 'мин', time_s, 'сек')
else:
    print(time_s, 'сек')