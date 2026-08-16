# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            else:
                q.append(node.left) 
            res.append(node)
        return res
        