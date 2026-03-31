# fib(n) = fib(n-1) + fib(n-2)
def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)

result = fib(6)  # Example usage
print(result)  # Output: 5