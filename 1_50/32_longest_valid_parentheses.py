# https://leetcode.com/problems/longest-valid-parentheses/discuss/2386596/Python3-Simple-Solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        maxi = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxi = max(maxi, i - stack[-1])

        return maxi

    # dp
    # https://leetcode.com/problems/longest-valid-parentheses/discuss/2279228/89-faster-python
    def longestValidParenthesesDp(self, s: str) -> int:

        if len(s) == 0:
            return 0
        dp = [0]
        for i in range(1, len(s)):
            if s[i] == '(':
                dp.append(0)
            elif s[i - 1] == '(':
                dp.append(2 + dp[i - 2])
            elif i - 1 - dp[i - 1] >= 0:
                if s[i - 1 - dp[i - 1]] == '(':
                    if i - 2 - dp[i - 1] >= 0:
                        dp.append(2 + dp[i - 1] + dp[i - 2 - dp[i - 1]])
                    else:
                        dp.append(2 + dp[i - 1])
                else:
                    dp.append(0)
            else:
                dp.append(0)
        return max(dp)
