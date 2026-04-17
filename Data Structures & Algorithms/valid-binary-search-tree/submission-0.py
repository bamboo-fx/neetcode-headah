# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # everything left must be smaller
        # everything right must be bigger
        # if not return false
        if not root:
            return False
        
        curr = root
        while curr:
            if curr.val < curr.left.val:
                return False
            
            elif curr.val > curr.right.val:
                return False
            return (self.isValidBST(curr.left) and self.isValidBST(curr.right))