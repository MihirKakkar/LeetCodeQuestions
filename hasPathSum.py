# Given a binary tree and a sum, determine if the tree has a 
# root-to-leaf path such that adding up all the values along the path equals the given sum.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        
        if root.val == sum and not root.left and not root.right:
            return True
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
