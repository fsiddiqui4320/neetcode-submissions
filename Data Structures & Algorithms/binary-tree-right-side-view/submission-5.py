# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        run bfs, organizing nodes by level
        we want the farthest right node at every level aka last node in the level list
        '''
        levels = []
        def dfs(node, level):
            nonlocal levels
            if not node:
                return
            if level >= len(levels):
                levels.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
            
        dfs(root, 0)
        return levels

