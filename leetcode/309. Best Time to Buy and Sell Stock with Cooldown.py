class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, notHold, notHold_cuz_cooldown = float('-inf'), 0, float('-inf')
        for price in prices:
            prev_hold, prev_notHold, prev_notHold_cuz_cooldown = hold, notHold, notHold_cuz_cooldown
            
            hold = max(prev_hold, prev_notHold - price)
            notHold = max(prev_notHold, prev_notHold_cuz_cooldown)
            notHold_cuz_cooldown = hold + price
        # return max(hold, notHold, notHold_cuz_cooldown)
        return max(notHold, notHold_cuz_cooldown)