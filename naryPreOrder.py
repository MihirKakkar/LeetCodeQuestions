# Given an n-ary tree, return the preorder traversal of its nodes' values.

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def traverse(root):
            if root is None:
                return
            result.append(root.val)
            for child in root.children:
                traverse(child)
            return 


        traverse(root)
        return result