class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        sell_p = 0
        for i in reversed(prices):
            if i > sell_p:
                sell_p = i
            if sell_p - i > max_val:
                max_val = sell_p - i
        return max_val