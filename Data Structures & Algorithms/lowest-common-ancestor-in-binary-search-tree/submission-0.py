# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or (not p and not q):
            return
        if not p:
            return q
        if not q:
            return p
        
        found = [p, q]
        # if both p and q are on the same lvl - its the parent
        # if one is higher than the other, its the higher node
        def find(node):
            if not node:
                return
            if node == p or node == q:
                return node

            left = find(node.left)
            right = find(node.right) 
            if left and right:
                return node
            elif not left and right:
                return right
            elif not right and left:
                return left
            else:
                return
        
        return find(root)