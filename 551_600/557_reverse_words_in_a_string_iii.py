class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        res = []
        for word in words:
            stack = list(word)
            stack.reverse()
            res.append(''.join(stack))
        return ' '.join(res)
