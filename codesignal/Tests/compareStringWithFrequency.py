from collections import Counter, defaultdict

def compareStringWithFrequency(word1: str, word2: str):
    c1, c2 = Counter(word1), Counter(word2)
    if c1.keys() != c2.keys():
        return False
    return Counter(c1.values()) == Counter(c2.values())

print(compareStringWithFrequency('babzccc', 'abbzczz') == True)
print(compareStringWithFrequency('babzcccm', 'bbazzczl') == False)

