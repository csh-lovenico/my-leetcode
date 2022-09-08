# https://leetcode.com/problems/wildcard-matching/discuss/2415515/python-solution-using-DP-O(m*n)-59.41-faster-than-other-submissions
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # similar to regular expression matching
        # dp[i][j] means whether s[0:i] can match p[0:j]
        dp = [[False] * (len(p) + 1) for x in range(len(s) + 1)]
        for i in range(0, len(s) + 1):
            for j in range(0, len(p) + 1):
                if i == 0 and j == 0:
                    # true if both are empty strings
                    dp[i][j] = True
                elif i == 0:
                    if p[j - 1] == "*":
                        # empty string can match '*'
                        dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    # non-empty string cannot match an empty pattern
                    dp[i][j] = False
                else:
                    if p[j - 1] == s[i - 1] or p[j - 1] == "?":
                        # match one letter, copy the state of previous string and previous pattern
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == "*":
                        # match '*'
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[len(s)][len(p)]
