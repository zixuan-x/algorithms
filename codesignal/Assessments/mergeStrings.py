from collections import Counter

def mergeStrings(s1, s2):
    result = []
    d1, d2 = Counter(s1), Counter(s2)
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        c1, c2 = s1[i], s2[j]
        f1, f2 = d1[c1], d2[c2]
        if f1 < f2:
            result.append(c1)
            i += 1
        elif f1 > f2:
            result.append(c2)
            j += 1
        else:
            if c1 <= c2:
                result.append(c1)
                i += 1
            else:
                result.append(c2)
                j += 1
    
    if i != len(s1):
        return ''.join(result) + s1[i:]
    else:
        return ''.join(result) + s2[j:]

print(mergeStrings("super", "tower") == "stouperwer")