from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_section_max_profit = 0
        current_min_buy = 10001
        # Scan only once, O(n)
        for i in range(len(prices)):
            # Calculate max profit until it meets a smaller number, then compare with total max profit
            if prices[i] < current_min_buy:
                if current_section_max_profit > max_profit:
                    max_profit = current_section_max_profit
                current_section_max_profit = 0
                current_min_buy = prices[i]
            else:
                profit = prices[i] - current_min_buy
                if profit > current_section_max_profit:
                    current_section_max_profit = profit
        # Flush buffer
        if current_section_max_profit > max_profit:
            max_profit = current_section_max_profit
        return max_profit
