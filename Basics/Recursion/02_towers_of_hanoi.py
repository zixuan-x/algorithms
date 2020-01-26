def solveHanoi(n: int) -> int:
    if n < 0:
        raise RuntimeError

    if n <= 1:
        return n
    
    return 2 * solveHanoi(n - 1) + 1 

def solveHanoi_print(n: int) -> None:
    solveHanoi_print_helper(n, 'A', 'B', 'C')

def solveHanoi_print_helper(n: int, source: str, spare: str, target: str) -> None:
    # if n == 1:
    #     print(f"Move {source} to {target}")
    #     return
    
    # solveHanoi_print_helper(n - 1, source, target, spare)
    # print(f"Move {source} to {target}")
    # solveHanoi_print_helper(n - 1, spare, source, target)

    if n > 0:
        solveHanoi_print_helper(n - 1, source, target, spare)
        print(f"Move {source} to {target}")
        solveHanoi_print_helper(n - 1, spare, source, target)


print(solveHanoi(3)) # 7
solveHanoi_print(3)
