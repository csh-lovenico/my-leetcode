from typing import List

from sortedcontainers import SortedList


# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/2640383/TC%3A100-SortedList-and-SegmentTree-Explained-Python
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/2321637/Python-or-SortedList-or-5-lines-or-explained-or-for-beginners-or-O(n-logn)-time-or-O(n)-Space
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/2372785/Python-Recursive-Segment-Tree-And-Binary-Indexed-Tree
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # sorted list, TC:100% 2000ms
        # traversing from the right side makes sense because that's the side we are interested in
        # for each element you are interested in knowing how many smaller elements u have already come across
        # so if u have a sortedlist u can do binary search to find idx of where curr_element sits,
        # and everything to the left of idx is smaller than curr and on the right side
        n = len(nums)
        c_nums = SortedList()
        ans = [0] * n
        for idx in range(n - 1, -1, -1):
            i = c_nums.bisect_left(nums[idx])  # i is the index of the first element not smaller than nums[idx]
            ans[idx] = i
            c_nums.add(nums[idx])
        return ans

    def countSmallerSegmentTree(self, nums: List[int]) -> List[int]:
        # 2 * 10 ** 4 + 1 is the number of buckets
        # 4 times number of buckets is size needed for segment tree array
        num_buckets = 2 * 10 ** 4 + 1
        segment_tree = [0] * 4 * num_buckets

        result = [0] * len(nums)

        def update(tree_index, bucket, tree_left, tree_right):
            nonlocal segment_tree

            if tree_left == tree_right:
                segment_tree[tree_index] += 1
                return

            # recurse into left or right subtree
            m = (tree_left + tree_right) // 2
            if bucket <= m:
                update(2 * tree_index + 1, bucket, tree_left, m)
            elif bucket > m:
                update(2 * tree_index + 2, bucket, m + 1, tree_right)

            # finally update this current tree node
            segment_tree[tree_index] += 1

        def query_range_sum(tree_index, tree_left, tree_right, i, j) -> int:
            nonlocal segment_tree

            # current segment has no overlap with query range
            if tree_left > j or tree_right < i:
                return 0

            # current segment is completely enclosed by query range
            if tree_left >= i and tree_right <= j:
                return segment_tree[tree_index]

            # current segment has partial overlap with query range
            m = (tree_left + tree_right) // 2
            return query_range_sum(2 * tree_index + 1, tree_left, m, i, j) + query_range_sum(2 * tree_index + 2, m + 1,
                                                                                             tree_right, i, j)

        offset = 10 ** 4
        # iterate from right to left
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]

            # query and append to result
            result[i] = query_range_sum(0, 0, num_buckets - 1, 0, (num + offset) - 1)

            # update segment tree important to think about what the segments represent, they represent the buckets
            # themselves. Min bucket index is 0, max bucket index is 2 * 10**4
            update(0, num + offset, 0, num_buckets - 1)

        return result
