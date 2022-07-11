# Greedy
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max_profit if max_profit > profit else profit
                right += 1
            else:
                left = right
            right += 1
        return max_profit


sol = Solution()
print("Max profit in  [7,1,5,3,6,4] : ", sol.maxProfit([7,1,5,3,6,4]))
print("Max profit in [7,6,4,3,1] : ", sol.maxProfit([7,6,4,3,1]))
print("Max Profit in [1,2,4,2,5,7,2,4,9,0,9] : ", sol.maxProfit([1,2,4,2,5,7,2,4,9,0,9]))
