class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            num = ord(columnTitle[i]) - ord('A') + 1
            result = result * 26 + num
        return result
