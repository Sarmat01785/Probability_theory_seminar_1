"""
Задача: В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того,
что 2 приобретенных билета окажутся выигрышными?
"""
import math


# Функция для вычисления биномиального коэффициента (сочетаний)
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# Общее количество билетов
total_tickets = 100

# Количество выигрышных билетов
winning_tickets = 2

# Количество приобретаемых билетов
purchased_tickets = 2

# Рассчитываем количество способов выбрать 2 выигрышных билета из 2 (только один способ)
winning_combinations = binomial_coefficient(winning_tickets, purchased_tickets)

# Рассчитываем общее количество способов выбрать 2 билета из 100
total_combinations = binomial_coefficient(total_tickets, purchased_tickets)

# Вероятность того, что оба приобретенных билета окажутся выигрышными
probability = winning_combinations / total_combinations

# Округляем вероятность до 5 знаков после запятой
probability = round(probability, 5)

print(f"Вероятность того, что 2 приобретенных билета окажутся выигрышными: {probability}")
