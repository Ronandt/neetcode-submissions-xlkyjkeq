# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #this is just an inorder traversal 
        if root == None:
            return -1
        track = []
        def traverse(node):
            if node == None:
                return
            traverse(node.left)
            #higher node 
            track.append(node.val)
            traverse(node.right)
        traverse(root)
        print(track)
        return track[k-1]