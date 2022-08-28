from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        sum_l = [0]
        re = []
        for i in range(1, len(nums)+1):
            sum_l.append(sum_l[i - 1] + nums[i-1])

        print(sum_l)
        for query in queries:
            if query < nums[0]:
                re.append(0)
                continue
            if query >= sum_l[-1]:
                re.append(len(nums))
                continue
            for i in range(len(sum_l)):
                if sum_l[i] > query:
                    re.append(i-1)
                    break
        return re


if __name__ == '__main__':
    print(Solution().answerQueries([76478,102343,247573,477461,430399,260435,250631,785081,904724,392720],
[63736,339518,37262,108251,216825]))
