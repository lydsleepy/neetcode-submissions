# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def height(node):
            if not node:
                return 0
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        
        height(root)
        return self.maxDiameter