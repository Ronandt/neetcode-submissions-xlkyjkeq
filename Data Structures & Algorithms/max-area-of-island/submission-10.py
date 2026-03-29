class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid[0])
        columns = len(grid)
        maximum = 0
        def bfs(root_column, root_row):
            root = (root_column, root_row)
            queue = collections.deque([root])
            grid[root_column][root_row] = "#"
            total = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    
                    total+= 1
                    board = [(0,1), (0,-1), (1,0), (-1,0)]
                    for column, row in board:
                        modified_column = node[0] + column
                        modified_row = node[1] + row
                        if(modified_column  in range(columns) and modified_row in range(rows) and
                        grid[modified_column][modified_row] not in ["#", 0]
                        ):
                            grid[modified_column][modified_row] = "#"
                            queue.append((modified_column, modified_row))
            return total
        for column in range(columns):
            for row in range(rows):
                if grid[column][row] == 1:
                    maximum = max(bfs(column, row), maximum)
      
        return maximum