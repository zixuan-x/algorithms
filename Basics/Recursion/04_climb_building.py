def climb(n: int) -> int:
    if n <= 0:
        raise RuntimeError

    if n <= 2:
        return n
    
    return climb(n - 1) + climb(n - 2)

def climb_print(n: int) -> None:
    if n <= 0:
        raise RuntimeError

    climb_print_helper(n, '')

def climb_print_helper(n: int, preway: str) -> None:
    # Base cases:
    if n == 1:
        print(preway + '1')
        return
    elif n == 2:
        print(preway + '2')
        print(preway + '1 1')
        return

    # Recursion rules:
    climb_print_helper(n - 1, preway + '1 ')
    climb_print_helper(n - 2, preway + '2 ')

print(climb(3))

print('Print:')
climb_print(3)