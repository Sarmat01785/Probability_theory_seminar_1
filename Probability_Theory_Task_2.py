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

# Рассчитываем количество способов выбрать 4 карты без тузов из оставшихся
non_aces_ways = binomial_coefficient(non_aces, cards_drawn)

# Рассчитываем общее количество способов выбрать 4 карты из 52
total_ways = binomial_coefficient(total_cards, cards_drawn)

# Вероятность того, что среди 4 карт не будет ни одного туза
probability_no_aces = non_aces_ways / total_ways

# Вероятность того, что среди 4 карт будет хотя бы один туз
probability_at_least_one_ace = 1 - probability_no_aces

# Округляем вероятность до 4 знаков после запятой
probability_at_least_one_ace = round(probability_at_least_one_ace, 4)

print(f"Вероятность того, что среди 4 вытянутых карт будет хотя бы один туз: {probability_at_least_one_ace}")
