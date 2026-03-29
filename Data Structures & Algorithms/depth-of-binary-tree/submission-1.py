# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        maximum = max(self.find(root.left), self.find(root.right))

        return maximum



    def find(self, node):
        if(node == None):
            return 1
        return max(self.find(node.left) +1, self.find(node.right) + 1)