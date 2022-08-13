from typing import List


# use dp
# https://leetcode.com/problems/word-break/discuss/2395861/Python-simple-DP-solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # true if s is empty
        res = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for word in wordDict:
                # if the slice of s matches a word
                if i >= len(word) and s[i-len(word):i] == word:
                    res[i] = res[i-len(word)] or res[i]
        return res[-1]


if __name__ == '__main__':
    print(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))
