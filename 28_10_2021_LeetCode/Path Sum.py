# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0

        def target(root, sum):
            if root:
                sum += root.val
                if not root.left and not root.right and sum == targetSum:
                    return True
                return target(root.left, sum) or target(root.right, sum)

        return target(root, sum)
