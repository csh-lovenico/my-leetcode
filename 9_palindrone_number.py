class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_list = []
        while x:
            num_list.append(x % 10)
            x = x // 10
        if len(num_list) % 2 == 0:
            l = len(num_list) // 2 - 1
            r = len(num_list) // 2
        else:
            l = len(num_list) // 2 - 1
            r = len(num_list) // 2 + 1

        while r < len(num_list):
            if num_list[l] != num_list[r]:
                return False
            r += 1
            l -= 1
        return True

    # another solution using O(1) space: https://leetcode.com/problems/palindrome-number/discuss/2433237/94-Faster-Easy-Python-Solution
