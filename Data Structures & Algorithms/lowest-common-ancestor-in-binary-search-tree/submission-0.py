# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        If i remember correctly, for this problem the way to do it, is we can
        incrementally cut in half like binary search, so we basically hm, let
        me take a sec to think, ok so we basically, well what is an ancestor,
        and ancestor of p and q means that p and q are its children, so essentially
        if node.left and node.right are both p and q, then node is our ancestor
        ok so the other part is that a node can be the ancestor of itself, if
        """

        # recursive top down dfs
        if not root:
            return None

        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)

        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root
