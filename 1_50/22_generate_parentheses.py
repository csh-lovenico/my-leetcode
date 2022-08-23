from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, cpt_open, cpt_closed, listRes):
            if cpt_open == cpt_closed == n:
                listRes.append(s)
            else:
                if cpt_closed < cpt_open:
                    backtrack(s + ")", cpt_open, cpt_closed + 1, listRes)
                if cpt_open < n:
                    backtrack(s + "(", cpt_open + 1, cpt_closed, listRes)

        listRes = []
        backtrack("", 0, 0, listRes)

        return listRes
