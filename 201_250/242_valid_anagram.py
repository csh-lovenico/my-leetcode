class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_list = [0] * 26
        # 97 is the ASCII number of 'a'
        for i in range(len(s)):
            old_num = letter_list[ord(s[i]) - 97]
            letter_list[ord(s[i]) - 97] = old_num + 1

        for i in range(len(t)):
            old_num = letter_list[ord(t[i]) - 97]
            letter_list[ord(t[i]) - 97] = old_num - 1

        for i in range(len(letter_list)):
            if letter_list[i] != 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram("rat", "car"))
