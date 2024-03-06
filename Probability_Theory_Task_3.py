"""
Задача: На входной двери подъезда установлен кодовый замок, содержащий десять кнопок
с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно.
Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
"""
import math


# Функция для вычисления биномиального коэффициента (сочетаний)
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# Количество кнопок на замке
buttons = 10

# Количество цифр в коде
code_length = 3

# Рассчитываем количество возможных уникальных комбинаций
combinations = binomial_coefficient(buttons, code_length)

# Вероятность угадать код с первой попытки
probability = 1 / combinations

# Округляем вероятность до 5 знаков после запятой
# probability = round(probability, 5)

print(f"Вероятность открыть замок с первой попытки: {probability}")
