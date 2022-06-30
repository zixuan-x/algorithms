class Solution:
    def intToRoman(self, num: int) -> str:
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 3, 2, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'III', 'II', 'I']

        result = []
        for i, v in enumerate(ints):
            result.extend([romans[i]] * (num // v))
            num %= v
        return ''.join(result)
            

class Solution:
    def intToRoman(self, num: int) -> str:
        ints = [1, 2, 3, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romans = ['I', 'II', 'III', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        result = []
        while num > 0:
            for i in range(14, -1, -1):
                if num >= ints[i]:
                    num -= ints[i]
                    result.append(romans[i])
                    break
        return ''.join(result)
            
# mapping = {
#     1: 'I',
#     2: 'II',
#     3: 'III',
#     4: 'IV',
#     5: 'V',
#     9: 'IX',
#     10: 'X',
#     40: 'XL',
#     50: 'L',
#     90: 'XC',
#     100: 'C',
#     400: 'CD',
#     500: 'D',
#     900: 'CM',
#     1000: 'M'
# }