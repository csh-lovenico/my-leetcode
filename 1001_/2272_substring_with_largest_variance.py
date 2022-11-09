import itertools


class Solution:
    # My solution in interview, TLE on LeetCode
    # Time complexity: O(n^2)
    def largestVariance(self, s: str) -> int:
        occurrence_list = [0] * 26
        prefix_sum = [occurrence_list]
        for i in range(1, len(s) + 1):
            curr_sum = prefix_sum[i - 1].copy()
            curr_sum[ord(s[i - 1]) - ord('a')] += 1
            prefix_sum.append(curr_sum)

        res = 0
        for i in range(1, len(s) + 1):
            for j in range(i):
                curr_i = prefix_sum[i].copy()
                curr_j = prefix_sum[j].copy()
                for k in range(26):
                    curr_i[k] -= curr_j[k]
                curr_i.sort(reverse=True)
                max_val = curr_i[0]
                min_val = 0
                for k in range(26):
                    if k == 25 or curr_i[k + 1] == 0:
                        min_val = curr_i[k]
                        break
                res = max(res, max_val - min_val)

        return res

    # https://leetcode.com/problems/substring-with-largest-variance/solutions/2412313/python-kadene-algo-with-explanation/
    # Time complexity: O(n)?
    def largestVarianceOptimized(self, s: str):
        # Create a dictionary with the count of all chars of s
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1

        # Calculate the possible permutations
        permutations = itertools.permutations(chars, 2)

        # Calculate the max subarray count with kadane algo
        count = 0
        for a, b in permutations:
            count = max(self.kadane(a, b, s, chars), count)
        return count

    def kadane(self, a, b, s, chars):
        count = 0
        max_local = 0

        # Keep track if c has become a or b
        is_a = False
        is_b = False

        # Keep track of characters for a and b
        val_a = chars[a]
        val_b = chars[b]
        for c in s:

            # No need to continue if c is not a or b
            if c != a and c != b:
                continue

            # Reset the max_local if there are no chars left or max_total
            # is negative
            if max_local < 0 and val_a != 0 and val_b != 0:
                max_local = 0
                is_a = False
                is_b = False

            # Add 1 to the local max if c is the expected char
            if c == a:
                max_local += 1
                val_a -= 1
                is_a = True

            # Remove 1 from the local max if c is the expected char
            if c == b:
                max_local -= 1
                val_b -= 1
                is_b = True

            # Only calculate the count if a and b appeared
            if is_a and is_b:
                count = max(count, max_local)
        return count


if __name__ == '__main__':
    s = "icexiahccknibwuwgi"
    print(Solution().largestVarianceOptimized(s))
