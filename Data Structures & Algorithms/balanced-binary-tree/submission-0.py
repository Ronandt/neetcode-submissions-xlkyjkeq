# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(not root):
            return True
        globalss = True
        
        def traverse(node):
            nonlocal globalss
            if node == None:
                return 0 
            left = traverse(node.left)
            right = traverse(node.right)
            maximum_height = max(left, right)
            difference = left-right
            print(difference, left, right)
            if difference >= 2 or difference <= -2:
                globalss = False
                
            return maximum_height + 1
        traverse(root)
        return globalss