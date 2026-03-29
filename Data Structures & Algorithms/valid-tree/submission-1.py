class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connected = {x : [] for x in range(n)}
        for x,y in edges:
            connected[x].append(y)
            connected[y].append(x)
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            if connected[node] == []:
                return True
            visited.add(node)
            for x in connected[node]:
                if x == prev:
                    continue
                if(not dfs(x, node)):
                    return False
            visited.remove(node)
            connected[node] = []
            return True
        res = dfs(0, -1)
        for x in connected:
            if len(connected[x]) > 0:
                return False
        return res 