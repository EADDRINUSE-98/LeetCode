class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price_ptr = max_price_ptr = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[min_price_ptr] or prices[i] < prices[max_price_ptr]:
                max_profit += prices[max_price_ptr] - prices[min_price_ptr]
                min_price_ptr = i
                max_price_ptr = min_price_ptr
            elif prices[i] > prices[max_price_ptr]:
                max_price_ptr = i
        max_profit += prices[max_price_ptr] - prices[min_price_ptr]
        return max_profit
