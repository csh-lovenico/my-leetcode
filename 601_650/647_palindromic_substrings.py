# https://leetcode.com/problems/palindromic-substrings/discuss/2602024/94-faster-and-98-space-optimized-oror-Python
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def isPalindrome(left, right):
            counter = 0
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    return counter
                counter += 1
                left -= 1
                right += 1
            return counter

        for index in range(len(s)):
            # for every index in s
            # (index, index) finds odd, (index, index+1) finds even
            result += isPalindrome(index, index) + isPalindrome(index, index + 1)
        return result
