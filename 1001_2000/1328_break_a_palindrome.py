# https://leetcode.com/problems/break-a-palindrome/discuss/2278269/78-TC-and-85-SC-easy-python-solution
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''
        n = len(palindrome)
        p = list(palindrome)
        for i in range(n // 2):
            if p[i] != 'a':
                p[i] = "a"
                return "".join(p)
        p[-1] = "b"
        return "".join(p)
