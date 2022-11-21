class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        words = s.split(' ')
        for word in words:
            if word:
                stack.append(word)
        stack.reverse()
        return ' '.join(stack)
