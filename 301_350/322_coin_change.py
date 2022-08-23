from typing import List


# https://leetcode.com/problems/coin-change/discuss/2407208/Python-or-DP-or-Easy-To-Understand
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]: minimum coin to get that amount
        dp = [amount + 1] * (amount + 1)

        # 0 coin to get 0 amount
        dp[0] = 0
        for a in range(amount + 1):
            for c in coins:
                # if the amount is large enough for adding a coin
                # pick the smallest sum
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':
    print(Solution().coinChange([186, 419, 83, 408], 6249))
