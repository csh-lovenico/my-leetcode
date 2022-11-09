class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if stack and len(stack) > 1:
                if abs(ord(stack[-1]) - ord(stack[-2])) == 32:
                    stack.pop()
                    stack.pop()
        return ''.join(stack)
