def fibo(num):
    if num == 0:
        return print(0)
    elif num == 1:
        return print(1)
    elif num == 2:
        return print(1)
    elif num > 2:
        f0 = 1 
        f1 = 1 
        for num in range(2, num):
            f2 = f0 + f1
            f0 = f1
            f1 = f2


        return print(f2)
        
fibo(int(input()))