def queue_system_metrics(lambda_rate, mu_rate):
    # Среднее число заказов в системе (Ls)
    Ls = lambda_rate / (mu_rate - lambda_rate)

    # Среднее время ожидания начала обработки заказа (Wq)
    Wq = lambda_rate / (mu_rate * (mu_rate - lambda_rate))

    # Среднее время, которое заказ проводит в системе (Ws)
    Ws = 1 / (mu_rate - lambda_rate)

    return Ls, Wq, Ws

# Параметры задачи
lambda_rate = 6  # средняя скорость поступления заказов в день
mu_rate = 8      # средняя скорость обслуживания заказов в день

# Вычисление характеристик системы
Ls, Wq, Ws = queue_system_metrics(lambda_rate, mu_rate)

# Вывод результатов
print(f"Среднее число заказов в системе (Ls): {Ls}")
print(f"Среднее время ожидания начала обработки заказа (Wq): {Wq} дня")
print(f"Среднее время, которое заказ проводит в системе (Ws): {Ws} дня")
