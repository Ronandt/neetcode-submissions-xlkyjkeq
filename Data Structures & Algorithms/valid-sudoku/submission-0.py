class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        column_dict = {}
        square_dict = {}
        rows = len(board)
        columns = len(board[0])
        for row in range(rows):
            for column in range(columns):
                target = board[row][column]
                square = (row // 3) * 3 + (column // 3)
                print(square)
                if target!= ".":
                    if (target in row_dict.get(row, []) or target in column_dict.get(column, [])
                     or target  in square_dict.get(square, [])):
                        print(row_dict, column_dict, square_dict, target, row, column, square)
                        return False
                    row_dict.setdefault(row, []).append(target)
                    column_dict.setdefault(column, []).append(target)
                    square_dict.setdefault(square, []).append(target)
                
        return True