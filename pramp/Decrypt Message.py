def decrypt(word):
  ''' str -> str '''  
  if not word:
    return ""
  
  chars = map(ord, word)
  prefixSum = chars[0]
  chars[0] -= 1
  for i in range(1, len(chars)):
    chars[i] -= prefixSum
    while chars[i] < 97:
      chars[i] += 26
    prefixSum += chars[i]
  return ''.join(map(chr, chars))

def decrypt(word):
  if not word:
    return ''
  
  res = []
  prefix_sum = 0
  for i in range(len(word)):
    cur = ord(word[i])
    if i > 0:
      cur -= prefix_sum
      while not (97 <= cur <= 97 + 26):
        cur += 26
    prefix_sum += cur 
    res.append(cur)
  res[0] -= 1
  return ''.join(map(chr,res))

"""
a, b ,c

97 <= a <= 97 + 26
97 <= b <= 97 + 26
97 <= c <= 97 + 26

a + 1, b, c

a + 1, b + a + 1, c + b + a + 1

a + 1, b + a + 1 - n1 * 26, c + b + a + 1 - n2 * 26

[a + 1, ]
"""
    