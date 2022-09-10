from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/2552021/Python-oror-3-lines-of-code-oror-easy-understanding
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        for i in range(1, len(prices)):
            res.append(prices[i] - prices[i - 1])
        return sum([a for a in res if a > 0])
