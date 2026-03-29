class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q= deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0,1], [0,-1]]
                for dr, dc in directions:
                    if (row + dr) in range(rows) and (col +dc) in range(cols) and grid[row + dr][col +dc] == "1" and (row + dr, col+dc) not in visited:
                        q.append((row + dr, col+dc))
                        visited.add((row + dr, col+ dc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1       
        return islands



   


            
       
    


"""
     def dfs(node, connected):
            nonlocal ans
            if(grid[node[0]][node[1]] == "#"):
                return 0
            if(grid[node[0]][node[1]] =="1"):
                if(connected == 0 ):
                    connected = 1
                    ans += 1
            
            save = int(grid[node[0]][node[1]])
            grid[node[0]][node[1]] = "#"
                
            possible_routes = [(node[0],node[1] -1), (node[0], node[1] + 1), (node[0] + 1, node[1]),(node[0]-1, node[1])]
            total = 0
            for x in possible_routes:
                if(x[0] < 0 or x[1] < 0 or x[0] >= rows or x[1] >= columns):
                    continue
                
                total += 0 if grid[x[0]][x[1]] == "#" else int(grid[x[0]][x[1]])
            if(total == 0 and connected ==1):
                connected = 0
            for x in possible_routes:
                if(x[0] < 0 or x[1] < 0 or x[0] >= rows or x[1] >= columns):
                    continue
                
                int(dfs(x, connected))

            return save
            """