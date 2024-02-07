from collections import defaultdict


class Solution:
    def check_valid_diagonal(self, diagonal_index: int, board: list[list[str]]) -> bool:
        row_seen = set()
        column_seen = set()
        for index in range(9):
            row_value = board[diagonal_index][index]
            column_value = board[index][diagonal_index]
            if row_value in row_seen or column_value in column_seen:
                return False
            if row_value != ".":
                row_seen.add(row_value)
            if column_value != ".":
                column_seen.add(column_value)
        return True

    def check_valid_square(self, row_start_index: int, column_start_index: int, board: list[list[str]]) -> bool:
        seen = set()
        for row in range(3):
            for column in range(3):
                value = board[row_start_index + row][column_start_index + column]
                if value in seen:
                    return False
                if value != ".":
                    seen.add(value)
        return True

    # cleaner implementation
    # def isValidSudoku(self, board: list[list[str]]) -> bool:
    #     for diagonal_index in range(9):
    #         if self.check_valid_diagonal(diagonal_index, board) is False:
    #             return False
    #     for row_start_index in range(0, 9, 3):
    #         for column_start_index in range(0, 9, 3):
    #             if not self.check_valid_square(row_start_index, column_start_index, board):
    #                 return False
    #     return True

    # single loops
    # def isValidSudoku(self, board: list[list[str]]) -> bool:
    #     row_seen = defaultdict(set)
    #     column_seen = defaultdict(set)
    #     square_seen = defaultdict(set)
    #     for row in range(9):
    #         for column in range(9):
    #             value = board[row][column]
    #             if value == ".":
    #                 continue
    #             square_index = ((row // 3), column // 3)
    #             if value in row_seen[row] or value in column_seen[column] or value in square_seen[square_index]:
    #                 return False
    #             row_seen[row].add(value)
    #             column_seen[column].add(value)
    #             square_seen[square_index].add(value)
    #     return True

    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
def main():
    answer = Solution()
    assert answer.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is True
    assert answer.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is False
    assert answer.isValidSudoku(
        [[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."],
         [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]) is False
    print('All test cases passed.')


if __name__ == "__main__":
    main()
