# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Hmm, I think we should... maybe we should dfs, top down to log counter
        Ok so if we do an inorder traversal then after k nodes visited we just return the value
        of the node at the kth node, so to perform an inorder traversal of a bst, just perform dfs.
        The only thing is as we recurse through, we should check the condition, that if count == k: return node
        
        Iterative bottom up dfs, create a stack, go through always go left first, after hitting leaf
        keep go back up, decrement k, keep track, after going left, go right then go left as much as possible
        do this until we hit k
        """
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right
        