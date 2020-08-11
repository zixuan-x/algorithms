from typing import List

def brokenKeyboard(s: str, letters: List[str]):
    letters = set(letters)
    count = 0
    for word in s.split(' '):
        isValid = True
        for c in word:
            if not c.isalpha():
                continue
            c = c.lower()
            if c not in letters:
                isValid = False
                break
        if isValid:
            count += 1
    return count

print(brokenKeyboard('Hello, my dear friend!', ['h', 'e', 'l', 'o', 'm']) == 1)