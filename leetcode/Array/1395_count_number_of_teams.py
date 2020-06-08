class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # edge case
        if not rating or len(rating) < 3:
            return 0

        # transform
        n = len(rating)
        ascending = [[0, 0] for i in range(n)]
        for i in range(n):
            less, larger = 0, 0
            for j in range(n):
                if j < i and rating[j] < rating[i]:
                    less += 1
                if j > i and rating[j] > rating[i]:
                    larger += 1
            ascending[i] = [less, larger]

        descending = [[0, 0] for i in range(n)]
        for i in range(n):
            descending[i][0] = i - ascending[i][0]
            descending[i][1] = (n - i - 1) - ascending[i][1]

        # count
        count = 0
        for i in range(n):
            count += ascending[i][0] * ascending[i][1]
            count += descending[i][0] * descending[i][1]

        # return
        return count

