"""
Задача: В ящике имеется 15 деталей, из которых 9 окрашены.
Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?
"""
import math


# Функция для вычисления биномиального коэффициента (сочетаний)
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# Общее количество деталей
total_parts = 15

# Количество окрашенных деталей
painted_parts = 9

# Количество деталей для извлечения
drawn_parts = 3

# Рассчитываем количество способов выбрать 3 окрашенные детали из 9
painted_combinations = binomial_coefficient(painted_parts, drawn_parts)

# Рассчитываем общее количество способов выбрать 3 детали из 15
total_combinations = binomial_coefficient(total_parts, drawn_parts)

# Вероятность того, что все три детали окрашены
probability = painted_combinations / total_combinations

# Округляем вероятность до 5 знаков после запятой
probability = round(probability, 5)

print(f"Вероятность того, что все извлеченные детали окрашены: {probability}")
