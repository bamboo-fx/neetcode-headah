# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        """
        I think a bfs solution, so level order is doable, but how it would work
        is checking for every given node in a level, if its left node is less
        and if right node is as well, if not return false

        So basically how it works is this, we dont need to actually go level
        by level so no for loop needed, but same structure with most bfs queues
        and we just need to initialize list of node/root but with lower and upper bounds.
        Every step we basically decide whether to go left or right, depending
        on which we do we shift in the left or right boundary to ensure the condition
        that node.val is between left and right, the outer boundary is to ensure global
        that it is less, and the inner boundary is updated every round to ensure that
        the node is valid between left and right in the context of local and global.
        
        q = deque([(root, -float("inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            
            if not (left < node.val < right):
                return False
                
            if node.left:
                q.append([node.left, left, node.val])
            if node.right:
                q.append([node.right, node.val, right])
        return True
        """

        """
        For the dfs solution, recursively check down ensuring the condition that left
        and right nodes are bounds for current node
        """

        if not root:
            return True

        if root.left and root.left.val > root.val:
            return False

        if root.right and root.right.val < root.val:
            return False

        return (self.isValidBST(root.left) and self.isValidBST(root.right))

                    