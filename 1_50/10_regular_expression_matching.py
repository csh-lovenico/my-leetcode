# https://leetcode.com/problems/regular-expression-matching/discuss/2532721/Dynamic-programming-or-Python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n_s = len(s)
        n_p = len(p)
        dp = [[False] * (n_p + 1) for _ in range(n_s + 1)]
        dp[0][0] = True

        # dp[i][j] shows if s[0:i] can match p[0:j] (base case is both s and p are empty strings)
        # For empty string but the "*" in pattern might return True
        for i in range(1, n_p + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 2]

        for i in range(1, n_s + 1):
            for j in range(1, n_p + 1):
                # When the character in string matches with the patter or the pattern has '.', which accepts any character
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # When the pattern has "*", this shows that we need to check the [j-2] for the character, which can be the string character or '.'. In this case we will check the [i-1][j], to check if the character except the current one is True.

                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        print(dp)
        return dp[n_s][n_p]


if __name__ == '__main__':
    print(Solution().isMatch("aaa", ".*"))
