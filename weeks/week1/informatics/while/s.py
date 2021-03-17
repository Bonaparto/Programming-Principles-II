b, a = int(input()), int(input())
while(a != b):
    if(b // 2 >= a and b % 2 == 0):
        b //= 2
        print(':2')
    else:
        b -= 1
        print('-1')