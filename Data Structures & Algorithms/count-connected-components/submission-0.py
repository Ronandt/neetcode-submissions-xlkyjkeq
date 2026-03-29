class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
    
        if n == 0:
            return 0
        res = 0
        connections = {x:[] for x in range(n)}
        for edge in edges:
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for x in connections[node]:
                dfs(x)
        for x in connections:
            if x not in visited:
                res += 1 
                dfs(x)
        return res 
            
