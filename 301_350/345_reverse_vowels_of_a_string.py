class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                stack.append(i)
                vowels.append(s[i])

        stack.reverse()
        for i in range(len(stack)):
            s_list[stack[i]] = vowels[i]

        return ''.join(s_list)
