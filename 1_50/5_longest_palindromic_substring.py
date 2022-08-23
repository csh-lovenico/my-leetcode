

# https://leetcode.com/problems/longest-palindromic-substring/discuss/2423414/Easy-and-Simple-Approach-to-understand-or-orPython
class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len = 0
        res = [0, 1]

        for i in range(len(s)):

            # diff = 0 for odd length palindromes
            # diff = 1 for even length palindromes
            for diff in [0, 1]:

                left = i
                right = i + diff

                # two pointers
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1

                cur_len = right - left - 1
                if cur_len > max_len:
                    max_len = cur_len
                    res = [left + 1, right]  # store the pointer

        return s[res[0]: res[1]]
