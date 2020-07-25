class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        res = []
        e = 9
        quantity = {9: 'Billion', 6: 'Million', 3: 'Thousand'}
        while e >= 0:
            threeDigits = num // 10 ** e
            if threeDigits > 0:
                res += [self.transThreeDigits(threeDigits)] + ([quantity[e]] if e > 0 else [])
            num %= 10 ** e
            e -= 3
        return ' '.join(res)
        
    def transThreeDigits(self, n):
        res = []
        oneDigit = {
            1: 'One', 
            2: 'Two', 
            3: 'Three', 
            4: 'Four', 
            5: 'Five', 
            6: 'Six', 
            7: 'Seven', 
            8: 'Eight',
            9: 'Nine'
        }
        
        startWithOne = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        startWithOthers = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }    
        
        if n >= 100:
            res += [oneDigit[n // 100]] + ['Hundred']
        
        n %= 100
        
        if n // 10 == 0:
            res += [oneDigit[n]] if n > 0 else []
        elif n // 10 == 1:
            res += [startWithOne[n]]
        else:
            res += [startWithOthers[n // 10]] + ([oneDigit[n % 10]] if n % 10 > 0 else [])
    
        return ' '.join(res)
            
            
        