# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        def traverse(root):
            if root is None:
                return

            traverse(root.left)
            resultArr.append(root.val)
            traverse(root.right)

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        resultArr = []
        traverse(root)
        return resultArr
