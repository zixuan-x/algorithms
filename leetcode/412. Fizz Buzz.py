class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                word = 'FizzBuzz'
            elif i % 3 == 0:
                word = 'Fizz'
            elif i % 5 == 0:
                word = 'Buzz'
            else:
                word = str(i)
            result.append(word)
        return result