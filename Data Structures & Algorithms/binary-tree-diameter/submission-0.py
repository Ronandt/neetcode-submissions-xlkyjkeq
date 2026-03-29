# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        self.res = 0

        def find(node):
            if(node == None):
                return 0
            right = find(node.right)
            left = find(node.left)
            self.res = max(self.res, right + left)
            return 1 + max(left,right)
        find(root)
        return self.res


            




