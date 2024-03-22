from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
        }
        cells = {
            (0, 0): set(),
            (1, 0): set(),
            (2, 0): set(),
            (0, 1): set(),
            (1, 1): set(),
            (2, 1): set(),
            (0, 2): set(),
            (1, 2): set(),
            (2, 2): set(),
        }
        for line in range(9):
            row = set()
            for i in range(9):
                if board[line][i] != ".":
                    if board[line][i] not in row:
                        row.add(board[line][i])
                    else:
                        return False

                    if board[line][i] not in columns[i]:
                        columns[i].add(board[line][i])
                    else:
                        return False

                    if board[line][i] not in cells[(i // 3, line // 3)]:
                        cells[(i // 3, line // 3)].add(board[line][i])
                    else:
                        return False
        return True


case_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

case_2 = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["5", ".", ".", ".", ".", ".", ".", "9", "."],
          [".", ".", ".", "5", "6", ".", ".", ".", "."],
          ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
          [".", ".", ".", "7", ".", ".", ".", ".", "."],
          [".", ".", ".", "5", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", "."]]

r = Solution()
assert r.isValidSudoku(case_1)
r.isValidSudoku(case_1)
# r.isValidSudoku(case_2)
assert not r.isValidSudoku(case_2)
