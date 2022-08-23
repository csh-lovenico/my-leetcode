class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_dec = int(a, 2)
        b_dec = int(b, 2)
        result_dec = a_dec + b_dec
        return bin(result_dec)[2:]
