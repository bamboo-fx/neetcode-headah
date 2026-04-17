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
        """
        q = deque([root])

        total = len(q)
        while q:
            for i in range(total):
                node = q.popleft()

                if node.left:
                    if node.left.val >= node.val:
                        return False
                    else:
                        q.append(node.left)

                if node.right:
                    if node.right.val <= node.val:
                        return False
                    else:
                        q.append(node.right)
        
        return True

                    