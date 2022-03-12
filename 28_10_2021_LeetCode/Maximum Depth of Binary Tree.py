# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        return self.Depth(root, 0)

    def Depth(self, root, k):
        if not root:
            return k
        else:
            return max(self.Depth(root.left, k + 1), self.Depth(root.right, k + 1))
