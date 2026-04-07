# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive dfs
        # bottom up
        """
        recursively go down both branches until hit base case, we are
        adding 1 every layer, compute the max between left and right
        

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """

        # Iterative dfs
        # top down
        """
        We iteratively go down, we start at the root, add to stack,
        we pop from stack and we keep track of max depth and we always
        append the children as long as the node is not empty, if its
        empty we exit the loop, we know we have reach leaf node, and
        we return res as that is our counter for the max depth
        

        stack = [[root, 1]]
        counter = 0

        while stack:
            node, depth = stack.pop()

            if node:
                counter = max(counter, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])

        return counter
        """

        # BFS
        """
        So basically whats happening is we make a deque, we check empty
        case then we add root to it, we iteratively just go through every level
        we record the level and add to our counter for level, but also for every given
        level the logic is, we remove every node in the level, and then for every
        given node if it has children node we add to q, if we reach leaves, they
        don't have children to append to q so q will be empty, loop ends, we
        return level counter. So essentially its pretty simple literally just
        go through every level, keep track of that, add the kids, level order
        traversal
        """

        q = deque()
        if root:
            q.append(root)

        counter = 0
        
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            counter += 1
        return counter


