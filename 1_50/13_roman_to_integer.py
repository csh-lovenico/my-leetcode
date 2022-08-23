class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'I':
                if i != len(s) - 1 and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    result -= 1
                else:
                    result += 1
            elif s[i] == 'V':
                result += 5
            elif s[i] == 'X':
                if i != len(s) - 1 and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    result -= 10
                else:
                    result += 10
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'C':
                if i != len(s) - 1 and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    result -= 100
                else:
                    result += 100
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'M':
                result += 1000

        return result
