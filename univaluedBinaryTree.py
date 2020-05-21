# A binary tree is univalued if every node in the tree has the same value.

# Return true if and only if the given tree is univalued.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isUnivalTree(self, root):

        checker = []

        def transverse(root):
            if root:
                transverse(root.left)
                checker.append(root.val)
                transverse(root.right)
            else:
                return None
        
        transverse(root)

        if len(list(set(checker))) = 1:
            return True
        else:
            return False
        




