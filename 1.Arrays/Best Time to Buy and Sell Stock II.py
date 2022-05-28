class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        share = False
        total = 0
        for i in range(n):
            if not share:
                sp = prices[i]
                share = True
            if i == n-1 or prices[i] > prices[i+1]:
                total += (prices[i] - sp)
                share = False
        return total