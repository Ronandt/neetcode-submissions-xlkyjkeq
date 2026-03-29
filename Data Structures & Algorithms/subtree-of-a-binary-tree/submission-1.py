# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root == None and  subRoot == None):
            return True
        elif root == None:
            return False
        elif subRoot == None:
            return True

        elif(root.val == subRoot.val):
            if(self.checkSubRoot(root, subRoot)):
                return True
            else:
                return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
          
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        


    def checkSubRoot(self, root, subRoot):
        if root == None and subRoot == None:
            return True
        elif root == None:
            return False
        elif subRoot == None:
            return False
      
        return self.checkSubRoot(root.right, subRoot.right) and self.checkSubRoot( root.left, subRoot.left) and root.val == subRoot.val
        