# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #basically dfs, if leaf nodes are same all the way till root of subRoot
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSametree(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))

        # helper function if trees are same

    def isSametree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        elif root.val != subRoot.val:
            return False
        return (self.isSametree(root.left, subRoot.left) and 
        self.isSametree(root.right, subRoot.right))
        