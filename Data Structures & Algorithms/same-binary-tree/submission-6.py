# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative bfs
        """
        Basically just make two queues, compare at every level if
        the nodes are the same
        p1 = deque([p])
        q1 = deque([q])

        while p1 and q1:
            for i in range(len(q1)):
                nodep = p1.popleft()
                nodeq = q1.popleft()

                if not nodep and not nodeq:
                    continue
                if not nodep or not nodeq or nodep.val != nodeq.val:
                    return False

                p1.append(nodep.left)
                p1.append(nodep.right)
                q1.append(nodeq.left)
                q1.append(nodeq.right)

        return True
        """
        # recursive dfs
        """
        """

        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))



