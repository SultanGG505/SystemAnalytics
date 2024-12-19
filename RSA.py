def egcd(a, b):
    """Расширенный алгоритм Евклида.
    Возвращает кортеж (g, x, y), где g = gcd(a, b), а x, y удовлетворяют ax + by = g."""
    if a == 0:
        return (b, 0, 1)
    g, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (g, x, y)

def mod_inverse(a, m):
    """Нахождение мультипликативной инверсии a по модулю m, то есть число d такое, что (a*d) mod m = 1."""
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Инверсия не существует')
    return x % m

def mod_exp(base, exponent, modulus):
    """Быстрое возведение в степень по модулю (modular exponentiation)."""
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

# Шаги из примера
p = 11
q = 13
n = p * q          # n = 143
phi_n = (p - 1) * (q - 1)  # phi(143) = 120
e = 7              # Взаимно просто с phi_n
d = mod_inverse(e, phi_n)  # d = 103

print("Открытый ключ: (e={}, n={})".format(e, n))
print("Закрытый ключ: (d={}, n={})".format(d, n))

M = 42
# Подписание: S = M^d mod n
S = mod_exp(M, d, n)
print("Сообщение:", M)
print("Подпись:", S)

# Проверка: M' = S^e mod n
M_check = mod_exp(S, e, n)

print("Проверка подписи:", M_check)
if M_check == M:
    print("Подпись проверена успешно.")
else:
    print("Подпись неверна.")
