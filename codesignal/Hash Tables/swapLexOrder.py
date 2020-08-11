'''
1. Brute force - while loop
'''
def swapLexOrder(str, pairs):
    strs = set([str])
    while 1:
        curStrs = set()
        for s in strs:
            for pair in pairs:
                curStrs.add(swap(s, pair))
        if strs == strs | curStrs:
            break
        strs |= curStrs
    return max(strs)
                        
def swap(str, pair):
    str = list(str)
    i, j = pair[0] - 1, pair[1] - 1
    str[i], str[j] = str[j], str[i]
    return ''.join(str)

'''
2. Brute force - permutation
'''
def swapLexOrder(str, pairs):
    strs = set([str])
    search(0, pairs, str, strs)
    return max(strs)
    
def search(index, pairs, curStr, strs):
    strs.add(curStr)
    if index == len(pairs):
        return
    
    for j in range(len(pairs)):
        pairs[index], pairs[j] = pairs[j], pairs[index]
        search(index + 1, pairs, swap(curStr, pairs[index]), strs)
        pairs[index], pairs[j] = pairs[j], pairs[index]
                        
def swap(str, pair):
    str = list(str)
    i, j = pair[0] - 1, pair[1] - 1
    str[i], str[j] = str[j], str[i]
    return ''.join(str)
    