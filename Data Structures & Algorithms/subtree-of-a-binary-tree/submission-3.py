# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # recursive dfs
        """
        So for recursive dfs hm whats the approach, i gotta find where/if
        there is a node that the root and subroot match, then iteratively
        recurse through and check that

        So the easiest way to solve this problem is with a helper function which allows
        us to detect and compare two trees to see if they are the same.
        So essentially we can just iterate through root until one of its nodes is the
        same as subroot, then from there we iterate through both and see if they are the same
        tree.
        """
        def isSametree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False

            return (isSametree(root.left, subRoot.left) and isSametree(root.right, subRoot.right))

        
        # base case
        if not subRoot:
            return True
        if not root:
            return False

        if isSametree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
