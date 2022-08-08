class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_list = [0] * 26
        for i in range(len(magazine)):
            old_num = letter_list[ord(magazine[i]) - ord('a')]
            letter_list[ord(magazine[i]) - ord('a')] = old_num + 1
        for i in range(len(ransomNote)):
            old_num = letter_list[ord(ransomNote[i]) - ord('a')]
            if old_num == 0:
                return False
            letter_list[ord(ransomNote[i]) - ord('a')] = old_num - 1
        return True
