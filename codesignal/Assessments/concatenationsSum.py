def concatenationsSum(a):
    result = 0
    n = len(a)
    totalTimes = sum((10 ** getTimes(num)) for num in a) + n
    for num in a:
        result += num * totalTimes
    return result

def getTimes(n):
    times = 0
    while n > 0:
        n //= 10
        times += 1
    return times

print(concatenationsSum([10, 2]) == 1344)