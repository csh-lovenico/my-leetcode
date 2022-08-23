class Solution:
    def longestPalindrome(self, s: str) -> int:
        # A-Z a-z
        letter_list = [0] * 52
        length = 0

        for i in range(len(s)):
            char = s[i]
            if ord(char) < ord('a'):
                old_num = letter_list[ord(char) - ord('A')]
                if old_num == 1:
                    length = length + 2
                    letter_list[ord(char) - ord('A')] = 0
                else:
                    letter_list[ord(char) - ord('A')] = old_num + 1
            else:
                old_num = letter_list[ord(char) - ord('a') + 26]
                if old_num == 1:
                    length = length + 2
                    letter_list[ord(char) - ord('a') + 26] = 0
                else:
                    letter_list[ord(char) - ord('a') + 26] = old_num + 1
        for i in range(len(letter_list)):
            if letter_list[i] == 1:
                length = length + 1
                break
        return length
