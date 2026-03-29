"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
      
        root = node
        
        if root == None:
            return root
        if root.neighbors == None:
            return root.neighbors
        visited = {}
        def dfs(node):
            build_node = Node()
            build_node.val = node.val
            visited[node] = build_node
            for x in node.neighbors:
                if x in visited:
                    build_node.neighbors.append(visited[x])
                else:
                    build_node.neighbors.append(dfs(x))
            return build_node
        
        return dfs(root)

           



