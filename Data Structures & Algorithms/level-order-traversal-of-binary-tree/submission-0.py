# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bst
        if(root == None):
            return []
        main_queue = deque([root])
        arr = [[]]
        while main_queue:
            for _ in range(len(main_queue)):
                node = main_queue.popleft()
                arr[-1].append(node.val)
                if(node.left):
                    main_queue.append(node.left)
                if(node.right):
                    main_queue.append(node.right)
            arr.append([]) #another level 
        arr.pop()
        return arr




