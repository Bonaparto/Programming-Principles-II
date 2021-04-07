# объявление функции

def factorial(n):
    res = 1
    for i in range(res, n + 1):
        res *= i
    return res

def compute_binom(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))