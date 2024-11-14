from scipy.optimize import linprog

# Зададим входные данные задачи
# Стоимости (единичные затраты) производства для каждой комбинации станок-продукт
costs = [
    [12, 13, 11],  # Стоимость для А
    [14, 13, 15],  # Стоимость для B
    [11, 10, 13],  # Стоимость для C
    [0, 0, 0]      # Стоимость для мнимого станка A4
]

# Потребности в каждом из пунктов назначения
demands = [2000, 3000, 3000]

# Запасы для каждого пункта отправления
supplies = [4000, 2400, 1000, 600]

# Разворачиваем матрицу стоимости в плоский список для использования в linprog
c = [cost for row in costs for cost in row]

# Ограничения на поставки
A_eq = []
for i, supply in enumerate(supplies):
    row = [1 if j // len(demands) == i else 0 for j in range(len(c))]
    A_eq.append(row)

# Ограничения на потребности
for j in range(len(demands)):
    row = [1 if k % len(demands) == j else 0 for k in range(len(c))]
    A_eq.append(row)

# Вектор ограничений для запасов и потребностей
b_eq = supplies + demands

# Решаем задачу
result = linprog(c, A_eq=A_eq, b_eq=b_eq, method='highs')

# Выводим результат
if result.success:
    print("Оптимальное распределение заказов:")
    x = result.x.reshape((len(supplies), len(demands)))
    for i, supply in enumerate(x):
        print(f"Станок {i+1}: {supply}")
    print(f"Минимальная стоимость производства: {result.fun}")
else:
    print("Задача не имеет решения")