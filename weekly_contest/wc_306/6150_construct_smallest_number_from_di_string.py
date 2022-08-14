

# https://leetcode.com/problems/construct-smallest-number-from-di-string/discuss/2422408/Python-3-Stack-solution
# DNF
class Solution:
    def smallestNumber(self, p: str) -> str:
        ans = ""
        s = []
        n = 1
        for i in range(len(p)):
            s.append(n)
            n += 1
            if p[i] != 'D':
                # if p[i] == 'I', pop all items in s to ans
                # n consecutive Ds means n+1 numbers in reversed order
                while s:
                    k = s.pop()
                    ans += str(k)
        s.append(n)
        while s:
            k = s.pop()
            ans += str(k)
        return ans
