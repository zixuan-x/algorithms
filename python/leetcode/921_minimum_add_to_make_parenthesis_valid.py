class Solution:
    """
    # Clarification / Edge Case
    s: str -> num: int
    
    # High Level Thought Process
    input: )())
    ))
    (())) -> )
    )
    
    )(
    
    ))((
    

    # Time/Space Trade off
    Time: O(n)
    Space:O(1)

    # Code
    
    """
    def minAddToMakeValid(self, S: str) -> int:
        leftDiff, rightDiff = 0, 0
        for c in S:
            if c == '(':
                leftDiff += 1
            else:
                if leftDiff > 0:
                    leftDiff -= 1
                else:
                    rightDiff += 1
    
        return leftDiff + rightDiff
                