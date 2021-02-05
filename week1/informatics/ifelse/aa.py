a, b, c = int(input()), int(input()), int(input())
if(not (a <= b <= c)):
    b, c = c, b
    if(not (a <= b <= c)):
        b, c = c, b
        a, b = b, a
        if(not (a <= b <= c)):
            a, b = b, a
            a, b, c = c, a, b
            if(not (a <= b <= c)):
                a, b, c = b, c, a
                a, b, c = b, c, a
                if(not (a <= b <= c)):
                    a, b, c = c, a, b
                    a, b, c = c, b, a
                    print(a, b, c)
                else:
                    print(a, b, c) 
            else:
                print(a, b, c)
        else:
            print(a, b, c)
    else:
        print(a, b, c)
else:
    print(a, b, c)