n = int(input())
sum_of_digs = 0
product_of_digs = 1
while n > 0:
    sum_of_digs += (n % 10)
    product_of_digs *= (n % 10)
    n //= 10
print(product_of_digs - sum_of_digs)        