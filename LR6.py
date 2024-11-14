import numpy as np

# Данные из таблицы 6.8
profits = [
    [0, 5, 9, 12, 14, 15, 18, 20, 24, 27],  # Прибыль для предприятия 1 при вложении от 0 до 9 ед.
    [0, 7, 9, 11, 13, 16, 19, 21, 22, 25],  # Прибыль для предприятия 2 при вложении от 0 до 9 ед.
    [0, 6, 10, 13, 15, 16, 18, 21, 22, 25]   # Прибыль для предприятия 3 при вложении от 0 до 9 ед.
]

# Начальные средства
total_capital = 9
num_companies = 3

# Инициализация таблицы максимальной прибыли
# Оптимальные значения для каждого числа доступного капитала
dp = np.zeros((num_companies + 1, total_capital + 1))

# Восстановление оптимальных решений
allocation = [[0] * (total_capital + 1) for _ in range(num_companies + 1)]

# Динамическое программирование для нахождения оптимального распределения капитала
for i in range(1, num_companies + 1):
    for j in range(total_capital + 1):
        max_profit = 0
        for x in range(j + 1):  # Перебираем все возможные вложения в текущее предприятие
            current_profit = profits[i - 1][x] + dp[i - 1][j - x]
            if current_profit > max_profit:
                max_profit = current_profit
                allocation[i][j] = x
        dp[i][j] = max_profit

# Определение оптимального распределения капитала
capital_left = total_capital
investments = [0] * num_companies
for i in range(num_companies, 0, -1):
    investments[i - 1] = allocation[i][capital_left]
    capital_left -= investments[i - 1]

# Вывод результатов
print(f"Оптимальное распределение капитала: {investments}")
print(f"Максимальная прибыль: {dp[num_companies][total_capital]}")
