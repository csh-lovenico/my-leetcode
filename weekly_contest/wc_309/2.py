import math


# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/discuss/2527381/JavaC%2B%2BPython-Math-Solution-O(klogk)
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        result = 0

        diff = abs(startPos - endPos)
        if (k - diff) % 2 != 0 or diff > k:
            return 0
        #
        # def dfs(cur: int, left: int):
        #     nonlocal result
        #     if abs(cur - endPos) > left:
        #         return
        #     if left == 0:
        #         if cur == endPos:
        #             result += 1
        #         return
        #     dfs(cur - 1, left - 1)
        #     dfs(cur + 1, left - 1)
        #
        # dfs(startPos, k)
        # print(result)
        # new_result = math.comb(k, diff)
        # print(new_result)
        # s = endPos - 1
        # left = k-diff+1
        # print(s)
        # for i in range(diff):
        #     result = result + (left - (endPos-s))
        #     left += 1
        #     s -= 1
        # return result % (10 ** 9 + 7)
        result = math.comb(k, (diff + k) // 2)

        return result % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().numberOfWays(1, 2, 7))
