from typing import List


# https://leetcode.com/problems/word-break-ii/discuss/2516443/Python-or-backtracking-beats-99.4
class Solution:
    def helper(self, index):
        if index >= len(self.s):
            return ['']
        ans = []
        for word in self.wordDict:
            length = len(word)
            if word == self.s[index:index + length]:
                temp = self.helper(index + length)
                if temp:
                    if len(temp) == 1 and temp[0] == '':
                        ans += [[word]]
                    else:
                        ans += [[word] + s for s in temp]
        return ans

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.s = s
        self.wordDict = wordDict
        ans = self.helper(0)
        ans = [' '.join(s) for s in ans]
        return ans
