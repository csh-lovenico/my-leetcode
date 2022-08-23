from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict = dict()
        row_dict = dict()
        for i in range(9):
            col_dict[i] = []
            row_dict[i] = []

        for i in range(9):
            for j in range(9):
                col = col_dict[i]
                row = row_dict[j]
                if board[i][j] != '.':
                    if board[i][j] in col:
                        return False
                    col.append(board[i][j])
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])

        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                cell_num = []
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if board[i + k][j + l] != '.' and board[i + k][j + l] not in cell_num:
                            cell_num.append(board[i + k][j + l])
                        elif board[i + k][j + l] in cell_num:
                            return False

        return True
