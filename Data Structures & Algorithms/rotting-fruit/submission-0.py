class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        columns = len(grid)
        rows = len(grid[0])
        queue = deque([])
        
        total = 0
        fresh = 0
        for column in range(columns):
            for row in range(rows):
                if grid[column][row] == 2:
                    queue.append((column, row))
                elif grid[column][row] == 1:
                    fresh += 1
        while queue and fresh > 0:
            
            for _ in range(len(queue)):
                node = queue.popleft()
                directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
                for dc, dr in directions:
                    res_col = node[0] + dc
                    res_row = node[1] + dr
                    if(res_col in range(columns) and res_row in range(rows)):
                        if grid[res_col][res_row] == 1:
                             queue.append((res_col, res_row))
                             fresh -=1
                             grid[res_col][res_row] = 2
            total += 1
        if(fresh > 0):
            return -1
        return total 