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
        def bfs(node, level):
            nonlocal levels
            if not node:
                return
            if level >= len(levels):
                levels.append([node])
            else:
                levels[level].append(node)
            bfs(node.left, level+1)
            bfs(node.right, level+1)
        bfs(root, 0)

        result = []
        for level in levels:
            result.append(level[-1].val)
        return result

