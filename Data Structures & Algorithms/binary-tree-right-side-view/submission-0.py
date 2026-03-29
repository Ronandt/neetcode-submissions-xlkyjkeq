# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []
        main_queue = deque([root])
        result_array = []
        while main_queue:
            last = -1
            for _ in range(len(main_queue)):
                node = main_queue.popleft()
                last = node.val
        
                if node.left != None:
                    main_queue.append(node.left)
                if node.right != None:
                    main_queue.append(node.right)
            result_array.append(last)
        return result_array
                
            