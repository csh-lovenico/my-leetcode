class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        new_str = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new_str = new_str + s[i].lower()
        i = 0
        j = len(new_str) - 1
        while True:
            if i > j:
                break
            if new_str[i] != new_str[j]:
                return False
            i = i + 1
            j = j - 1
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("race a car"))
