# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         """
#         This is a two pointer approach.
#         """
#         min_price_ptr = max_price_ptr = 0
#         max_profit = 0
#         for i in range(len(prices)):
#             if prices[i] < prices[min_price_ptr]:
#                 min_price_ptr = i
#                 max_price_ptr = min_price_ptr
#             elif prices[i] > prices[max_price_ptr]:
#                 max_price_ptr = i
#             max_profit = max(prices[max_price_ptr] - prices[min_price_ptr], max_profit)
#         return max_profit


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        This is a dp approach.
        """
        best_buy_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(price - best_buy_price, max_profit)
            best_buy_price = min(price, best_buy_price)
        return max_profit
