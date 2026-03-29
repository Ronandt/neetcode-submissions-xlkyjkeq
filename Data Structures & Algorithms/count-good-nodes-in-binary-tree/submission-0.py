# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.findGoodNodes(root.right, root) + self.findGoodNodes(root.left, root) + 1

    def findGoodNodes(self, root, maxPrevNode):
        #plus and update prev node
        good_nodes_status = 0 
        if root == None:
            return 0 #if somehow it gets here 
        if(root.val >= maxPrevNode.val):
            return self.findGoodNodes(root.right,root) + self.findGoodNodes(root.left, root) + 1
            
        else:
            return self.findGoodNodes(root.right,maxPrevNode) + self.findGoodNodes(root.left, maxPrevNode
            ) 
            
        