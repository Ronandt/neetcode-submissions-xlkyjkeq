"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        hash_table = {} #should be the val: linked linked_list

        
        
        def copyFromList(node):
            if node == None:
                return None
            build= Node(node.val)
            hash_table[node] = build
        
            

            build.next = copyFromList(node.next) if node.next not in hash_table else hash_table[node.next]
            build.random = copyFromList(node.random) if node.random not in hash_table else hash_table[node.random]
            return build
        return copyFromList(head)
        

        

            
