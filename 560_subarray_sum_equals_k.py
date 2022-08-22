from typing import List


# https://leetcode.com/problems/subarray-sum-equals-k/discuss/2355867/PYTHON-HASHMAP-PREFIX-SUM-SOLUTION-EASY
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        hash = {0: 1}
        arr = []
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            arr.append(count)
        for i in arr:
            # if prefSum - k exists, we can use prefSum - (prefSum - k) to get k
            if i - k in hash:
                ans += hash[i - k]
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        return ans


if __name__ == '__main__':
    print(Solution().subarraySum([1, 2, 3, 2, 1], 3))
