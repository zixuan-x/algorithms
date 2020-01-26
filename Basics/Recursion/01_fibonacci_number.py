def fibonacci(n: int) -> int:
    # Base cases:
    if n < 0:
        raise RuntimeError

    if n < 2:
        return n

    # Recursion rulels:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
