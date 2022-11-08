from typing import List


# https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/2475570/Sliding-window-(HashmapTwo-pointer)-with-details-Python
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # hard to compute exactly k, but easy to compute at most k
        # answer is (at most k) - (at most (k-1))
        def atMostKDistinct(nums, k):
            niceSubarray = 0
            hashmap = {}
            left, right = 0, 0

            # sliding window
            while right < len(nums):
                if nums[right] in hashmap:
                    hashmap[nums[right]] += 1
                else:
                    hashmap[nums[right]] = 1

                while len(hashmap) > k:
                    hashmap[nums[left]] -= 1
                    if hashmap[nums[left]] == 0:
                        del hashmap[nums[left]]
                    left += 1

                # why right - left + 1 ???
                niceSubarray += right - left + 1

                # move right pointer
                right += 1

            return niceSubarray

        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)
