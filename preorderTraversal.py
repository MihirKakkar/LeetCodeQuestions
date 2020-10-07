# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        def traversal(root):
            if root is None:
                return 
            resultArr.append(root.val)
            traversal(root.left)
            traversal(root.right)

    resultArr = []
    traversal(root)
    return resultArr
