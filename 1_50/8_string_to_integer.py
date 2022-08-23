class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        is_negative = False
        current_index = 0
        current_sum = 0
        for i in range(len(s)):
            if s[i] == ' ':
                current_index += 1
                continue
            else:
                break
        if current_index == len(s):
            return 0
        if s[current_index] == '-':
            is_negative = True
            current_index += 1
        elif s[current_index] == '+':
            current_index += 1
        if current_index == len(s):
            return 0
        for i in range(current_index, len(s)):
            if ord('0') <= ord(s[i]) <= ord('9'):
                current_sum = current_sum * 10 + (ord(s[i]) - ord('0'))
                if current_sum > pow(2, 31) - 1:
                    if not is_negative:
                        return pow(2, 31) - 1
                    else:
                        if current_sum > pow(2, 31):
                            return -1 * pow(2, 31)
            else:
                break
        if is_negative:
            current_sum *= -1
        return current_sum


if __name__ == '__main__':
    print(Solution().myAtoi("42"))
