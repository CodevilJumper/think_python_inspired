# Recursive code for Fibonacci number based on fib(n) = fib(n-1) + fib(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(25))