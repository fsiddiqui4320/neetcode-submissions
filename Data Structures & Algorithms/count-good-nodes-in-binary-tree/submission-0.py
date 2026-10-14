# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        run dfs with a good node counter
        track max node val seen for each path
        for each node visited
            if node none:
                    return 0
            if pathMax <= curr node val:
                increment count or return 1
            return dfs left + dfs right

        return dfs(root, root.val)
        '''
        count = 0
        def dfs(node, pathMax):
            nonlocal count
            if not node:
                return 0
            if node.val >= pathMax:
                count += 1
                pathMax = node.val
            
            return dfs(node.left, pathMax) + dfs(node.right, pathMax)
        dfs(root, -101)
        return count