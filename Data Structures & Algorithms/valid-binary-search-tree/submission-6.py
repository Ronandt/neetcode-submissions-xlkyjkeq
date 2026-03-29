# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            prev = [float('-inf')] 
            def inorder(node):
                if not node:
                    return True
                
                # Traverse left subtree
                if not inorder(node.left):
                    return False
                
                # Check current node: must be strictly greater than previous
                if node.val <= prev[0]:
                    return False
                prev[0] = node.val
                
                # Traverse right subtree
                return inorder(node.right)
            
            return inorder(root)