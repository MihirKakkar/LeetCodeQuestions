# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        def traverse(root):
            
            if root is None:
                return 0
            
            if root.left is None and root.right is None:
                return 1
            
            if root.left is None:
                return traverse(root.right) + 1
            
            if root.right is None:
                return traverse(root.left) + 1
            return min(traverse(root.left), traverse(root.right)) + 1
        
        return traverse(root)
        