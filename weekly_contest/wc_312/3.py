from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        print(nums)
        good_front = [0] * len(nums)
        f_bool = [True] * len(nums)
        good_back = [0] * len(nums)
        b_bool = [True] * len(nums)
        res = []

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if f_bool[i - 1]:
                    good_front[i] = good_front[i - 1] + 1
                else:
                    good_front[i] = 1
            else:
                if f_bool[i - 1]:
                    good_front[i] = good_front[i - 1] + 1
                    f_bool[i] = False
                    if good_front[i - 1] == 0:
                        good_front[i] = 1
                else:
                    f_bool[i] = False
                    good_front[i] = 1

        print(good_front, f_bool)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                if b_bool[i + 1]:
                    good_back[i] = good_back[i + 1] + 1
                else:
                    good_back[i] = 1
            else:
                if b_bool[i + 1]:
                    good_back[i] = good_back[i + 1] + 1
                    b_bool[i] = False
                    if good_back[i + 1] == 0:
                        good_back[i] = 1
                else:
                    b_bool[i] = False
                    good_back[i] = 1
        print(good_back, b_bool)
        for i in range(len(nums)):
            if good_front[i] >= k and good_back[i] >= k:
                res.append(i)
        return res


if __name__ == '__main__':
    print(Solution().goodIndices(
        [34250, 751275, 914297, 51571, 32780, 4335, 1424, 1131, 49, 3, 3, 3, 2, 2, 2, 1, 1, 1, 585223, 838005, 986277,
         994420, 997144, 999009, 999792, 999903, 999976, 999989, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000,
         1000000], 16))
