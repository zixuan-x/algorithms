'''
1. brute force (TLE)
'''
def possibleSums(coins, quantity):
    sums = set()
    search(0, coins, quantity, 0, sums)
    return len(sums)    
    
def search(index, coins, quantity, curSum, sums):
    if curSum != 0:
        sums.add(curSum)
    
    if index == len(coins):
        return
    
    for q in range(quantity[index] + 1):
        search(index + 1, coins, quantity, curSum + coins[index] * q, sums)

'''
2. 
'''
def possibleSums(coins, quantity):
    sums = set([0])
    for i in range(len(coins)):
        coin, q = coins[i], quantity[i]
        curSums = set()
        for sum in sums:
            for j in range(q + 1):
                curSums.add(sum + coin * j)
        sums |= curSums
    return len(sums) - 1

'''
3.
'''

