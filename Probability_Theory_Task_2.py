"""
Задача: Из колоды в 52 карты извлекаются случайным образом 4 карты.
Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
"""
import math


# Функция для вычисления биномиального коэффициента
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# Общее количество карт
total_cards = 52

# Количество карт, не являющихся тузами
non_aces = total_cards - 4

# Выбираем 4 карты
cards_drawn = 4
