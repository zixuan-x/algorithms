def divisorSubstrings(s, k):
    total = int(s)
    result = 0
    divisors = set()
    for i in range(len(s) - k + 1):
        substring = s[i:i + k]
        num = int(substring)
        if (num != 0) and (num not in divisors):
            if total % num == 0:
                result += 1
            divisors.add(num)
    return result

print(divisorSubstrings('120', 2) == 2)
print(divisorSubstrings('555', 1) == 1)
print(divisorSubstrings('2345', 2) == 0)
