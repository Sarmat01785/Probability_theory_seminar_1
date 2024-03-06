"""
Задача:
В колоде 52 карты, и 13 из них крести. Нам нужно выяснить,
какова вероятность того, что все 4 вытянутые карты будут крестями.
"""

import math


# Функция для вычисления биномиального коэффициента
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# Общее количество карт
total_cards = 52

# Количество крестей в колоде
clubs = 13

# Выбираем 4 карты
cards_drawn = 4

# Рассчитываем количество способов выбрать 4 крести из 13
clubs_ways = binomial_coefficient(clubs, cards_drawn)

# Рассчитываем общее количество способов выбрать 4 карты из 52
total_ways = binomial_coefficient(total_cards, cards_drawn)

# Вероятность того, что все 4 карты будут крестями
probability = clubs_ways / total_ways

# Округляем вероятность до 5 знаков после запятой
probability_rounded = round(probability, 5)

print(f"Вероятность того, что все 4 вытянутые карты будут крестями: {probability_rounded}")
