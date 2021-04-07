# объявление функции
def get_next_prime(num):
    while True:
        num += 1
        for i in range(2, round(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            return num
        
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))