import ctypes
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = 0
        max_index = [-1]
        visited = set()
        res = 1
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = [i]
            elif nums[i] == max_num:
                max_index.append(i)
            else:
                continue
        for idx in max_index:
            temp = 0
            bitw0 = nums[idx]
            if idx in visited:
                continue
            for i in range(idx, len(nums)):
                visited.add(i)
                bitw1 = bitw0 & nums[i]
                if bitw1 == bitw0:
                    temp += 1
                else:
                    res = max(res, temp)
                    break
            res = max(res, temp)
        return res


if __name__ == '__main__':
    print(Solution().longestSubarray([3, 5, 4]))
