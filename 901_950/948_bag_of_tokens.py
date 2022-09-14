from typing import List


# https://leetcode.com/problems/bag-of-tokens/discuss/2564497/C%2B%2B-oror-JAVA-oror-PYTHON-oror-Easy-solution-Explained-oror-Beginner-Friendly-oror-Best-Method
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        i, j = 0, n
        while i < j:
            if tokens[i] <= power:
                power -= tokens[i]
                i += 1
            elif i - (n - j) and j > i + 1:
                j -= 1
                power += tokens[j]
            else: break
        return i - (n - j)