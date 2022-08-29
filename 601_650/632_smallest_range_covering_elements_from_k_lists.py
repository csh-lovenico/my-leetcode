import heapq


# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/2455890/Clean-Easy-to-follow-Python-Heapify-faster-than-67
class Solution(object):
    def smallestRange(self, nums):
        heap = [(li[0], i, 0) for i, li in enumerate(nums)]
        heapq.heapify(heap)

        # find max_value of items entered into heap
        max_value = max([lis[0] for lis in nums])
        min_range, max_range = -1e9, 1e9

        while heap:
            print(heap)
            print(max_value)
            print(min_range, max_range)
            curr_min, list_number, index = heapq.heappop(heap)
            # check if curr_min - max_value is a smaller range
            min_range, max_range = self.smaller_range(curr_min, max_value, max_range, min_range)
            print(min_range, max_range)
            # push next item from list if exists & update max_value
            if index + 1 < len(nums[list_number]):
                max_value = max(max_value, nums[list_number][index + 1])
                heapq.heappush(heap, (nums[list_number][index + 1], list_number, index + 1))
            # at least one list is exhausted so smallest range has been found
            else:
                break

        return [min_range, max_range]

    """
    Function takes two potential ranges and returns the one which is smaller
    """

    def smaller_range(self, curr_min, max_value, max_range, min_range):
        if max_value - curr_min < max_range - min_range:
            return curr_min, max_value
        elif max_value - curr_min == max_range - min_range and curr_min < min_range:
            return curr_min, max_value
        else:
            return min_range, max_range


if __name__ == '__main__':
    print(Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
