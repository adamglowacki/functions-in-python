def fib(i):
    if i == 0 or i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)

print(fib(40))