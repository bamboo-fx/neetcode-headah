# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        I think its like recursive, the question is, is it dfs or bfs, alright because
        i feel like ive already done this problem before lets just says its dfs, in
        that case, hm i am more bullish on bfs, level order traversal, at every level
        just swap??

        Ok so this can be done dfs and bfs, ill do dfs first

        ok so for dfs it can be bottom up or top down, the difference is just when
        we actually perform the invert function, as we go down to base case, or hit base
        case then undwind back up
        """

        # top down

        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


