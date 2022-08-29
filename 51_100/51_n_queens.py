from typing import List


# https://leetcode.com/problems/n-queens/discuss/2410027/Easiest-solution-you-will-ever-see!
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        valid_boards = []

        def check(row, banned_cols, banned_diag_sum, banned_diag_diff, board):
            if row == n:
                # means we have placed n queens (as we are using 0 based index), lets store the solution in the
                # global list valid_boards.
                valid_boards.append(board)
                return

            for col in range(n):
                # can we place a queen given our banned columns and diagonals due to previous placements?
                can_place_at_row_col = (col not in banned_cols) and \
                                       (row + col not in banned_diag_sum) and \
                                       (row - col not in banned_diag_diff)
                # if yes, we place a queen at (row, col) and move to next row, update the banned column set and banned diagonal sets and add a rown in the board and check all the possibilities.
                if can_place_at_row_col:
                    check(row + 1,
                          banned_cols.union({col}),
                          banned_diag_sum.union({row + col}),
                          banned_diag_diff.union({row - col}),
                          board + ['.' * col + 'Q' + '.' * (n - col - 1)])
            return

        # initially nothing is banned
        check(0, banned_cols=set(), banned_diag_sum=set(), banned_diag_diff=set(), board=[])

        # return all the valid boards that we sotored
        return valid_boards
