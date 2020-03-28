a = 1717986919
m = 2147483647

for i in range(1233, 200000000):
    if (i * a) % m >> 31 > 0:
        print(i)