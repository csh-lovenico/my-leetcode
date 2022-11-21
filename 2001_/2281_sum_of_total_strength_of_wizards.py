from typing import List


# https://leetcode.com/problems/sum-of-total-strength-of-wizards/solutions/2061985/java-c-python-one-pass-solution/
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/solutions/2062017/C++-prefix-+-monotonic-stack-O(N)-solution-with-thought-process/
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        res, ac, mod, stack, acc = 0, 0, 10 ** 9 + 7, [-1], [0]
        strength += [0]
        for r, a in enumerate(strength):
            ac += a
            acc.append(ac + acc[-1])
            while stack and strength[stack[-1]] > a:
                i = stack.pop()
                l = stack[-1]
                lacc = acc[i] - acc[max(l, 0)]
                racc = acc[r] - acc[i]
                ln, rn = i - l, r - i
                res += strength[i] * (racc * ln - lacc * rn) % mod
            stack.append(r)
        return res % mod
