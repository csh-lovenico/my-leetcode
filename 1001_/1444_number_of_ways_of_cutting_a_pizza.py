from functools import lru_cache
from typing import List


# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/discuss/967112/Python-3-straightforward-DFS
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        M = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])

        arr = [[0] * n for _ in range(m)]
        # keep track of total apples from left top corner to right down corner
        for i in range(m):
            for j in range(n):
                arr[i][j] = ''.join(x[j:] for x in pizza[i:]).count('A')

        @lru_cache(None)
        def dp(r, c, k, cnt):
            # base case
            if k == 1:
                return 1
            ans = 0
            for i in range(m):
                # cuts must be either right or down
                if i <= r:
                    continue
                # rest apples should have at least one but less than previous sum
                if 0 < arr[i][c] < cnt:
                    ans += dp(i, c, k - 1, arr[i][c])
            for j in range(n):
                if j <= c:
                    continue
                if 0 < arr[r][j] < cnt:
                    ans += dp(r, j, k - 1, arr[r][j])
            return ans % M

        return dp(0, 0, k, arr[0][0])
