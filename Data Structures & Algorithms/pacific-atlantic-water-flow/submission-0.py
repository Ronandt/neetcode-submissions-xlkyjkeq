class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        pacific = set() #do pacfici first if atlanctic hits pacific
        pacific_visited = []

        #pacific
        queue = deque([])
        for row in range(rows):
            queue.append((row, 0 ))
            pacific.add((row, 0 ))
            pacific_visited.append((row, 0))

        for column in range(columns):
            queue.append((0, column))
            pacific.add((0, column))
            pacific_visited.append((0, column))
        print(queue)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                print(node)
                directions = [(0,1), (0,-1), (-1, 0), (1,0)]
                for dr, dc in directions:
                    res_row = node[0] + dr
                    res_column = node[1] + dc
                    if(res_row in range(rows) and res_column in range(columns) and (res_row, res_column) not in pacific_visited):
                        
                        if heights[res_row][res_column] >= heights[node[0]][node[1]]:
                            pacific_visited.append((res_row, res_column))
                            pacific.add((res_row, res_column))
                            queue.append((res_row, res_column))
        atlantic_visited = []
        res_atlantic = set()
        queue.clear()
        for row in range(rows):
            queue.append((row, columns-1 ))
            res_atlantic.add((row, columns-1))
            atlantic_visited.append((row, columns-1))

        for column in range(columns):
            queue.append((rows -1, column  ))
            res_atlantic.add((rows -1, column))
            atlantic_visited.append((rows -1, column))

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                print(node)
                directions = [(0,1), (0,-1), (-1, 0), (1,0)]
                for dr, dc in directions:
                    res_row = node[0] + dr
                    res_column = node[1] + dc
                    if(res_row in range(rows) and res_column in range(columns) and (res_row, res_column) not in atlantic_visited):
                        
                        if heights[res_row][res_column] >= heights[node[0]][node[1]]:
                            atlantic_visited.append((res_row, res_column))    
                            res_atlantic.add((res_row, res_column))
                            queue.append((res_row, res_column))
        
        return [list(x) for x in res_atlantic  & pacific]


                   