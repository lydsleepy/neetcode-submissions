# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(node):
            if not node: # node is None
                return 0
            else:
                left = balance(node.left)
                right = balance(node.right)

                if left == -1 or right == -1:
                    return -1
                elif abs(left - right) > 1:
                    return -1
                else:
                    return max(left, right) + 1
        
        return balance(root) != -1