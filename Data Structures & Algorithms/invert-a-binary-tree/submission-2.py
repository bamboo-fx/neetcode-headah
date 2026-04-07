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

        So basically regardless we are going to start from root and go down until we hit
        the base case and then start unwinding, the difference between top down and bottom
        up just depends on when we perform the swap, during winding or during unwinding
        """

        # top down
        """
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        """

        """
        bfs version:
        Ok so BFS is level ordered traversal with FIFO algorithm and
        queue data structure, so no recursion, rather we are just going
        down level by level swapping children, adding them to queue, swapping
        their children then popping, we go until we reach leaf layer where
        there are no longer any children thus nothing to add to queue so since
        queue is empty we break out, once we break out all that is left is
        just the root where it now has everything added to it, all the children
        nodes which have been swapped, so just return the root
        """

        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.right, node.left = node.left, node.right

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

