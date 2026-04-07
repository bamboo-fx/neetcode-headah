"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # data structure: hashmap
        # algorithm: dfs
        
        # connected graph

        if not node:
            return None

        cloned = {}
        def dfs(curr):
            if curr in cloned:
                return cloned[curr]

            clone = Node(curr.val)
            cloned[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
            






