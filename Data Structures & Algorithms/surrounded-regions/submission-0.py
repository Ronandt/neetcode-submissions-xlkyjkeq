class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque([])
        rows = len(board)
        columns = len(board[0])
        for row in range(rows):
            for column in range(columns):
                if (row == 0 or row == rows - 1 or column == 0 or column == columns - 1) and board[row][column] == "O":
                    board[row][column] = "T"
                    queue.append((row, column))
        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                directions = [(0,1), (0, -1), (-1, 0), (1,0)]
                for r, c in directions:
                    row_res = node[0] + r
                    column_res = node[1] + c
                    if row_res not in range(rows) or column_res not in range(columns):
                        continue 
                    if board[row_res][column_res] == "O":
                        board[row_res][column_res] = "T"
                        queue.append((row_res, column_res))
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "O":
                    board[row][column] = "X"
                if board[row][column] == "T":
                    board[row][column]  = "O"