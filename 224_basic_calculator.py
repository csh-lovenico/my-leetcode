

# https://leetcode.com/problems/basic-calculator/discuss/2287586/Python-Easy-solution-using-stack-oror-Easy-oror-O(n)-Time-Complexity
class Solution:
    def calculate(self, s: str) -> int:
        # sign is the sign of previous number
        curr, output, sign, stack = 0, 0, 1, []

        for ch in s:
            if ch.isdigit():
                curr = curr * 10 + int(ch)

            elif ch == '+':
                output += sign * curr
                sign = 1
                curr = 0

            elif ch == '-':
                output += sign * curr
                sign = -1
                curr = 0

            elif ch == '(':
                # push the result and then the sign
                stack.append(output)
                stack.append(sign)
                sign = 1
                output = 0

            elif ch == ')':
                output += sign * curr
                output *= stack.pop()
                output += stack.pop()
                curr = 0
        return output + sign * curr
