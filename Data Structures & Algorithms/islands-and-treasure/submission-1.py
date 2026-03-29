class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
      # -1 cannot be traversed
      #0 treasure chest
      #can be traversed 
      columns = len(grid)
      rows = len(grid[0])
      copy_of_grid = grid.copy()
      def bfs(root_column, root_row):
        queue = deque([(root_column, root_row)])
        visited = [(root_column, root_row)]
        goal = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                directions = [(0, -1), (0, 1), (-1, 0), (1,0)]
                for dc, dr in directions:
                    res_c = node[0] + dc
                    res_r = node[1] + dr
                    if(res_c in range(columns) and res_r in range(rows) and (res_c, res_r) not in visited):
                        if grid[res_c][res_r] not in [-1, 0]:
                            
                            visited.append((res_c, res_r))
                            queue.append((res_c, res_r))
                        if grid[res_c][res_r] == 0:
                            grid[root_column][root_row] = goal
                            return
            goal += 1

      for column in range(columns):
        for row in range(rows):
            if grid[column][row] == 2147483647:
                bfs(column, row)
      

