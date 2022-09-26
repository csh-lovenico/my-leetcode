class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        appear = set()
        while True:
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n = n // 10
            if res == 1:
                return True
            if res not in appear:
                appear.add(res)
                n = res
                continue
            else:
                return False
