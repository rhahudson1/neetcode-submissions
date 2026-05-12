# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subRoot.val:
            return((self.sameTree(subRoot.left, root.left)) or self.sameTree(subRoot.right, root.right))
    def sameTree(self, l, r):
        if not l and not r:
            return True
        if l and r and l.val == r.val:
            return ((self.sameTree(l.left, r.left)) and (self.sameTree(l.right, r.right)))
        return False
        