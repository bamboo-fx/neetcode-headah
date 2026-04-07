"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # data structure
        # hashmap
        # algorithm
        # dfs

        if not node:
            return None

        alreadyCopied = {}

        def dfs(node):
            if node in alreadyCopied:
                return alreadyCopied[node]

            clone = Node(node.val)
            alreadyCopied[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)

