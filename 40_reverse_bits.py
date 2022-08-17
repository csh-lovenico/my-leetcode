class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = n % 2
            result = result * 2 + bit
            n = n // 2
        return result

# use Python features: https://leetcode.com/problems/reverse-bits/discuss/2430279/Easy-to-understand-python-solution-(Runtime-39ms)(Memory-Usage-13.7MB)
