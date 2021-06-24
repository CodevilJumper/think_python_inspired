# Find factorial of a number n with use of recursion
# Based on the idea that 3! is 3 * 2! OR 5! is 5 * 4! which is --> n! = n * (n-1)!   etc.

def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)

    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        result = n * factorial(n-1)
        print(space, 'returning', result)
        return result

factorial(4)
