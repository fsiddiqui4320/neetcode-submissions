# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        levels = []
        
        while queue:
            level_size = len(queue)
            level = []
            for i in range(level_size):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            if level:
                levels.append(level)

        return levels