# https://leetcode.com/problems/reaching-points/discuss/1363473/Python-solution-using-math-with-comments
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:

            if tx == sx and ty == sy:
                return True
            # check how many tx we can deduct
            if ty > tx and (ty - sy) // tx >= 1:
                ty = ty - tx * ((ty - sy) // tx)
            # check how many ty we can deduct
            elif tx > ty and (tx - sx) // ty >= 1:
                tx = tx - ty * ((tx - sx) // ty)
            else:
                break
        return False
