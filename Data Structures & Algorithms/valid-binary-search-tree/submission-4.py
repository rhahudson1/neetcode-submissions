# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            if node.val > node.left.val and node.val < node.right.val:
                dfs(node.left)
                dfs(node.right)
            else: 
                return False
            return True
        dfs(root)