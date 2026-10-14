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
        if not root:
            return []
        result = []
        queue = [root]
        level_size = len(queue)
        while queue:
            for i in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == level_size - 1:
                    result.append(node.val)
            level_size = len(queue)

        return result

