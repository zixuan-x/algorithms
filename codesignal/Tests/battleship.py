'''
given N = 4, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A", your function should return
"1,1", as explained above.

Given N = 3, S = "1A 1B,2C 2C" and T = "1B", your function should return "0,1", because one ship
was hit but not sunk.

Given N = 12, S = "1A 2A,12A 12A" and T = "12A", your function should return "1,0", because one
ship was hit and sunk.

N is an integer within the range [1..26];
string S contains the descriptions of rectangular ships of area not greater than 4 cells;
there can be at most one ship located on any map cell (ships do not overlap);
each map cell can appear in string T at most once;
string S and string T contains only valid positions given in specified format.
In your solution, focus on correctness. The performance of your solution will not be the focus of the
assessment.
'''

def battleship(N: int, s: str, t: str):
    sunk, hit_not_sunk = 0, 0
    ships = s.split(',')
    hits = set(t.split(' '))
    for ship in ships:
        shipComponents = set()
        topLeft, bottomRight = ship.split(' ')
        # 数字可能有两位，而字母肯定只有一位
        x1, y1 = int(topLeft[:-1]), ord(topLeft[-1]) - ord('A')
        x2, y2 = int(bottomRight[:-1]), ord(bottomRight[-1]) - ord('A')
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                print(x, y)
                shipComponents.add(str(x) + chr(y + ord('A')))
        print(shipComponents)
        if shipComponents.issubset(hits):
            sunk += 1
        else:
            for component in shipComponents:
                if component in hits:
                    hit_not_sunk += 1
                    break
    return f'{sunk},{hit_not_sunk}'

print(battleship(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A") == '1,1')
print(battleship(3, "1A 1B,2C 2C", "1B") == '0,1')
print(battleship(12, "1A 2A,12A 12A", "12A") == '1,0')

