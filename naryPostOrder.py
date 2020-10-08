# Given an n-ary tree, return the postorder traversal of its nodes' values.

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def traverse(root):
            if root is None:
                return
            for child in root.children:
                traverse(child)
            result.append(root.val)
            return 


        traverse(root)
        return result