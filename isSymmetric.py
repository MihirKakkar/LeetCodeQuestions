# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.symmetry(root.left, root.right)
    
    def symmetry(self, l, r):
        if l and r:
            return l.val == r.val and self.symmetry(l.left, r.right) and self.symmetry(l.right, r.left)
        return leftroot == righroot

