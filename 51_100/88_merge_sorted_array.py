from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp_n1 = nums1[0:m]
        idx_1 = 0
        idx_2 = 0
        idx = 0
        while idx_1 < m or idx_2 < n:
            if idx_2 == n:
                nums1[idx] = temp_n1[idx_1]
                idx_1 += 1
                idx += 1
                continue
            elif idx_1 == m:
                nums1[idx] = nums2[idx_2]
                idx_2 += 1
                idx += 1
                continue
            else:
                if temp_n1[idx_1] < nums2[idx_2]:
                    nums1[idx] = temp_n1[idx_1]
                    idx_1 += 1
                    idx += 1
                else:
                    nums1[idx] = nums2[idx_2]
                    idx_2 += 1
                    idx += 1
