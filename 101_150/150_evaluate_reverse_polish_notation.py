import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif tokens[i] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif tokens[i] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif tokens[i] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()


if __name__ == '__main__':
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
